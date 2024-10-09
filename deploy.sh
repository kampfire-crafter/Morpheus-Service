#!/bin/bash

read -sp "Enter password: " PASSWORD
echo

sshpass -p $PASSWORD ssh cyclopowl "docker compose -f /home/pi/morpheus-service/docker-compose.yaml down"
sshpass -p $PASSWORD ssh cyclopowl sudo rm -r /home/pi/morpheus-service/*
sshpass -p $PASSWORD scp -r ./* cyclopowl:/home/pi/morpheus-service
sshpass -p $PASSWORD ssh cyclopowl "docker compose -f /home/pi/morpheus-service/docker-compose.yaml up --build"
