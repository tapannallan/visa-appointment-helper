#!/bin/bash

#echo Before you run this setup file, do the following
#echo 1. Run chmod +x for setenv, run.sh, and lib/deathbycaptcha, lib/extract_captcha.py lib/fetch_value.py 
#echo 2. Edit the settings in setenv before you run this setup file.
#echo 3. Once edited, remove/comment the line below this (exit) as well as these echo lines 

#exit

#Load Environment
source ./setenv
cd $root_folder

#Create log folder
mkdir log

#Install pip and python requirements
sudo apt install python3-pip
pip3 install -r requirements.txt