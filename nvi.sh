#!/bin/bash
sudo zypper in nvidia-bumblebee
sudo systemctl enable dkms
sudo zypper in nvidia-bumblebee-32bit
