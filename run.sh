#!/bin/bash

COMIC_READER_DIR="/usr/share/comic_reader"

sudo docker-compose -f "${COMIC_READER_DIR}/api/production.yml" up -d
sudo docker-compose -f "${COMIC_READER_DIR}/app/production.yml" up -d
