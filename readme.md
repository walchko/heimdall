![](pics/heimdall.jpg)

# Heimdall

Heimdall is named after the Norse god who has the ability to see and hear everything.
This is a small monitoring device. Ultimately I would like it to do:

- monitor a room with the camera
- monitor wifi and log devices/APs found
- monitor bluetooth and log devices found

## BOM

| Name | Cost | Source |
|---|---|---|
| Pi Zero W | $10 | https://www.adafruit.com/product/3400 |
| RPi Camera | $29 | https://www.adafruit.com/ |

# Setup

You will need a Raspberry Pi (this was designed for a Zero) with wifi access
(or at least internet access). It should work with a normal Raspberry Pi, but
I haven't tested that.

## Apt-Get

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get -y intall python-dev python3-dev build-essential swig cmake
    sudo apt-get -y install libatlas-base-dev gfortran

## Python

    pip install -U pip setuptools wheel
    pip install -U -r requirements.txt

## Service

To enable heimdall to run as a service on your Raspberry Pi, do:

    sudo ./install-heimdall-service.sh
