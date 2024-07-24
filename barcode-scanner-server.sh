#!/bin/bash

cd "`dirname $(readlink -f ${0})`"

source ./venv/bin/activate
python3 barcode-scanner-server-v2.py