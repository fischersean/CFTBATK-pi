#!/bin/bash

# Enable SPI interface

# Setup venv
python3 -m venv venv
source venv/bin/acivate
pip install --upgrade pip
pip install -r requirements.txt

# Download and install waveshare drivers
git clone https://github.com/waveshare/e-Paper
pip install e-Paper/RaspberryPi\&JetsonNano/python

sudo apt-get install libopenjp2-7
