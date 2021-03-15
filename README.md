# AIY Voice for BCI

This repository contains an easy-to-use Python API for the [AIY Vision Kit][aiy-vision]
and [AIY Voice Kit][aiy-voice]. The code for all AIY kits is in the `aiyprojects` branch,
and is included in images starting with `aiyprojects-2017-12-18.img`.

This repo has been repurposed for BCI studies at LIINC..

## Additional steps

To set up AIY for Google Text to Speech applications, you need to:
1. pip3 install google-cloud-texttospeech
2. add GOOGLE_APPLICATION_CREDENTIALS named "cloud_speech.json" into your home folder
3. ```wget https://github.com/labstreaminglayer/liblsl/releases/download/1.12/liblsl-1.12.0-Linux-ARM7.deb; sudo apt-get install ./liblsl-1.12.0-Linux-ARM7.deb```

## Documentation

If you're just getting started with the Vision or Voice kit, see the
assembly guide and other maker guides at [aiyprojects.withgoogle.com].

If you just need the Python API reference, see [aiyprojects.readthedocs.io].
Also have a look at the [example code][aiy-github-examples].

If you want to flash the latest AIY system image or install AIY packages on an existing
Raspbian system, read the [system updates guide][HACKING.md].

## Releases

* [Image downloads][downloads]
* [Change log][changelog]

## Bugs & Support

If you've found a bug, please [review the known issues and report a new one][aiy-github-issues].

If you've fixed a bug yourself, please send us a pull request!
For details, read [CONTRIBUTING.md].

If you're having trouble assembling your kit or running the demos, try the following links:

* [AIY Help docs][help-docs]
* [AIY Forums][aiy-forums]
* [AIY Stack Overflow][aiy-stack-overflow]
* [AIY GitHub Issues][aiy-github-issues]
* support-aiyprojects@google.com

If you've found a problem with the Assistant API (for example, it crashes
or provides incorrect responses), try the following:

* [Assistant Stack Overflow][assistant-stack-overflow]
* [Assistant GitHub Issues][assistant-github-issues]

##

<p align="center">
  <img width="15%" src="https://aiyprojects.withgoogle.com/static/images/icons/aiy-circular-logo.svg">
</p>

[HACKING.md]: HACKING.md
[CONTRIBUTING.md]: CONTRIBUTING.md
[downloads]: https://github.com/google/aiyprojects-raspbian/releases
[changelog]: CHANGES.md

[aiyprojects.withgoogle.com]: https://aiyprojects.withgoogle.com
[aiyprojects.readthedocs.io]: https://aiyprojects.readthedocs.io
[aiy-vision]: https://aiyprojects.withgoogle.com/vision/
[aiy-voice]: https://aiyprojects.withgoogle.com/voice/

[help-docs]: https://aiyprojects.withgoogle.com/help
[aiy-forums]: https://www.raspberrypi.org/forums/viewforum.php?f=114
[aiy-stack-overflow]: https://stackoverflow.com/questions/tagged/google-aiy
[aiy-github-issues]: https://github.com/google/aiyprojects-raspbian/issues
[aiy-github-examples]: https://github.com/google/aiyprojects-raspbian/tree/aiyprojects/src/examples

[assistant-stack-overflow]: https://stackoverflow.com/questions/tagged/google-assistant-sdk
[assistant-github-issues]: https://github.com/googlesamples/assistant-sdk-python/issues
