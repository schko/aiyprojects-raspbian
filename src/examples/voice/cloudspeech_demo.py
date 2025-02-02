#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""
import argparse
import locale
import logging

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/cloud_speech.json"

from aiy.voice import tts
from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
from pylsl import StreamInfo, StreamOutlet, local_clock


#  to interpret the content
info = StreamInfo('AIYVoice', 'Markers', 1, 0, 'string', 'aiyvoice')

# next make an outlet
outlet = StreamOutlet(info)

def get_hints(language_code):
    if language_code.startswith('en_'):
        return ('turn on the light',
                'turn off the light',
                'blink the light',
                'goodbye')
    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', args.language)
    hints = get_hints(args.language)
    client = CloudSpeechClient()
    with Board() as board:
        while True:

            if hints:
                logging.info('Say something, e.g. %s.' % ', '.join(hints))
            else:
                logging.info('Say something.')
            text = client.recognize(language_code=args.language,
                                    hint_phrases=hints)
            if text is None:
                logging.info('You said nothing.')
                continue

            logging.info('You said: "%s"' % text)
            text = text.lower()
            if 'turn on the light' in text:
                board.led.state = Led.ON
            elif 'turn off the light' in text:
                board.led.state = Led.OFF
            elif 'blink the light' in text:
                board.led.state = Led.BLINK
            elif 'confident' in text or 'confidence' in text:
                # Remove "confidence" from the text to be repeated
                to_repeat = text.replace('confidence', '', 1)
                to_repeat = text.replace('confident', '', 1)
                tts.google_tts_say('You are ' + to_repeat + ' confident')
                stamp = local_clock()-0.5
                outlet.push_sample([text],stamp)
            elif 'hard' in text or 'ard' in text or 'easy' in text: # note ard was determined through testing
                stamp = local_clock()-0.5
                outlet.push_sample([text],stamp)
            elif 'goodbye' in text:
                break

if __name__ == '__main__':
    main()
