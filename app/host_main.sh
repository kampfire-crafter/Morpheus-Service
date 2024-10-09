#!/bin/bash

pipe="/home/pi/morpheus-service/app/morpheus_pipe"

while true; do
    if [ -p "$pipe" ]; then
        eval "$(cat $pipe)"
    fi

    sleep 1
done
