#!/bin/bash

scp -r -i ~/.ssh/mac_pi_rsa ~/Documents/local-repo/pi-ink scp://pi@192.168.1.5:22/~

