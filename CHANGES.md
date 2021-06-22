# Change log

This page describes the changes in each release.

To update your kit, see the [system updates guide][system-updates].
All system images can be downloaded from the [GitHub releases page][github-releases].

## AIY Kits Release 2021-04-02

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

Based on the [Raspberry Pi OS with desktop][raspberry-pi-os] from March 4th 2021.

**Fixes**

* Sound driver compilation errors on the latest Raspberry Pi OS
* Upgrade Colab TF version to 1.13.1
* Driver source code added to this repository

## AIY Kits Release 2020-11-20

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

Based on the [Raspberry Pi OS with desktop][raspberry-pi-os] from August 20th 2020.

**Fixes**

* Driver compilation errors on the latest Raspberry Pi OS
* HACKING.md instructions for Vision Bonnet and Voice HAT

## AIY Kits Release 2019-11-13

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

Based on the [Raspbian Buster with desktop][raspbian].

**Fixes**

* Fix driver compilation errors on the latest Raspbian
* Fix HACKING.md instructions
* Fix gpiozero integration

**Improvements**

* Debian packages are now hosted at https://packages.cloud.google.com/
* Original Raspbian image is modified in the minimal way (no unnecessary packages)

## AIY Kits Release 2018-11-16

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

**Fixes**

* Fix tts engine click sound
* Fix `assistant_grpc_demo.service`: add DISPLAY environment variable and proper
systemd dependencies
* Fix various linter findings: python3 compatibility, wrong variable names, etc.

**Improvements**

* New `board.py` to access button and LED on all boards
* New audio API in `voice/audio.py`
* Direct python support for iNaturalist models
* Load anchors/labels directly from text files
* Add `get_inference_state()` and `resest()` to Vision Bonnet protocol
* Add Voice HAT schematic in `docs` folder
* Add sparse representation for output tensors to increase data transfer rate
* SVG-image overlay for video streaming (experimental)

## AIY Kits Release 2018-08-03

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

**Fixes**

* Fix PulseAudio infinite loop with Voice Bonnet
* Fix PulseAudio volume control
* Fix gpiozero LED on/off bug
* Fix local USB networking on macOS, no driver required
* Fix check_audio.py

**Improvements**

* Add Makefile for common shortcuts
* Add vision unit tests for all models and examples
* Add video streaming support (experimental)
* Add Google Cloud IoT support (experimental)
* Add more documentation (pinouts, drivers, troubleshooting, etc.)
* Add new code examples and update existing ones
* Add CHANGES.md to track release changes
* Remove unnecessary files (e.g. ALSA configs)
* Update vision driver to support mmap syscall
* Update sound driver to support latest Raspbian image
* Update HACKING.md

## AIY Kits Release 2018-04-13

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

## AIY Kits Release 2018-02-21

Compatible with Voice HAT, Voice Bonnet, and Vision Bonnet.

## AIY Kits Release 2017-12-18

Compatible with Voice HAT and Vision Bonnet.

## VoiceKit Classic Image 2017-09-11

Compatible with Voice HAT.

[github-releases]: https://github.com/google/aiyprojects-raspbian/releases
[system-updates]: https://github.com/google/aiyprojects-raspbian/blob/aiyprojects/HACKING.md
[raspbian]: https://www.raspberrypi.org/downloads/raspbian/
[raspberry-pi-os]: https://www.raspberrypi.org/software/operating-systems/
