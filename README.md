# Morpheus Service

## Description

The Morpheus Service is a Python application designed to monitor CPU activity on a Raspberry Pi and trigger a shutdown when the system has been inactive for a specified period. The system collects CPU usage statistics and, if the inactivity threshold is exceeded, sends a shutdown command through a named pipe.

## Components

- **Morpheus** : Main service that monitors CPU activity and manages shutdowns.
- **CPUChecker** : Monitors CPU usage and determines if the system is busy or inactive.
- **Pipe** : Handles writing commands (such as shutdown) to a named pipe, which a separate shell script reads and executes.

## Prerequisites

- A Raspberry Pi (tested on Pi Zero W)
- Python 3
- psutil library for CPU monitoring
- .env file with the following variables:
    - **PIPE_DIR**: Directory path to the named pipe used for sending commands.
    - **CPU_THRESHOLD**: CPU usage percentage to consider the system as active.
    - **CHECK_INTERVAL**: How often (in seconds) to check CPU activity.
    - **INACTIVITY_TIME_THRESHOLD**: Time (in seconds) before the system is considered inactive and triggers shutdown.

## Install and run the container

Install the project directory into folder : /home/pi/morpheus-service

```bash
docker compose up -d
```

## Install the crontab

Install a new crontab :

```bash
crontab -e
@reboot /home/pi/morpheus-service/app/host_main.sh >> /home/pi/morpheus-service/morpheus.log &2>1
```
