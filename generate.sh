#!/bin/bash

source env/bin/activate

while true
do
    python src/show.py
    sleep 840           # 14 minutes
done