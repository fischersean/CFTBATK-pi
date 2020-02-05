# CFTBATK-pi

*Claire From the Bon-Appetite Test Kitchen*

## About

This repo contains the source code and necessary scripts to run a simple board to display what baked good is available. This project assumes that you have a RaspberryPi and [this](https://www.waveshare.com/2.7inch-e-paper-hat-b.htm) Waveshare 2.7" e-ink display.

## Usage

The key map is as follows:

 - Key 1 - Clear Screen
 -  Key 2 - Cycle picture up 
 - Key 3 - Cycle picture down 
 - Key 4 - Refresh Screen

You will need to setup the RaspberryPi before you can properly use the script. The most time consuming of these steps is building Python 3.7 from source. 
1) Run the `build_py.sh` script. This will take a long time. Make sure you have properly installed the binaries (adding to path, creating aliases, etc.)

2) Create a python venv
	`python3 -m venv venv`
	`source venv/bin/acivate`

3) Install requirements.txt
	`pip install --upgrade pip`
	`pip install -r requirements.txt`
 
 4) Clone and install the Waveshare drivers
	 `git clone https://github.com/waveshare/e-Paper`
	`pip install e-Paper/RaspberryPi\&JetsonNano/python`
 
 5) Enable SPI interfacing through `raspi-config`
 
 6) Install the libopenjp2-7 libraries
	`sudo apt-get install libopenjp2-7`

After that you should be good to go. Simple run `pyhon pi_screen.py` and test if it works.
