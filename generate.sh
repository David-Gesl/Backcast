#!/bin/bash

source env/bin/activate

while true
do
    python src/show.py
    sleep 900           # 15 minutes
done