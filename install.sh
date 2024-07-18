#!/bin/bash

cd "`dirname $(readlink -f ${0})`"
sudo ln -sf $(pwd)/barcode-scanner-server.sh /usr/local/bin/barcode-scanner-server
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
