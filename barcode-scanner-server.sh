#!/bin/bash

cd "`dirname $(readlink -f ${0})`"

echo $(pwd )
source ./venv/bin/activate
python3 barcode-scanner-server.py