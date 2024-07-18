#!/bin/bash

cd "`dirname $(readlink -f ${0})`"
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
