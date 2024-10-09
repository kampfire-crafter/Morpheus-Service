FROM balenalib/rpi-debian-python:3.11-buster

WORKDIR /app

RUN sudo apt update && sudo apt install gcc python3-dev

RUN pip install psutil python-dotenv

CMD ["python", "/app/main.py"]
