#!/bin/bash

sudo rm -rfv /usr/share/comic_reader 
sudo mkdir -v /usr/share/comic_reader
sudo cp -rv api/ /usr/share/comic_reader
sudo cp -rv app/ /usr/share/comic_reader
sudo cp -rv run.sh /usr/local/bin/comic_reader
