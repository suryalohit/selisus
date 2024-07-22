# Base Image
FROM ubuntu:20.04

# Environment variables, setting app home path and copy of the python app in the container
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Update/upgrade the system
RUN apt -y update
RUN apt -y upgrade

# Install App dependencies and chrome webdriver
RUN apt install -yqq unzip curl wget python3-pip
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y --no-install-recommends ./google-chrome-stable_current_amd64.deb
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Install Python dependencies
RUN pip install Flask gunicorn selenium==4.17.2 selenium-wire==5.1.0 pyotp webdriver-manager blinker==1.7.0 requests==2.32.3
EXPOSE 8000

CMD exec gunicorn --bind :10000  --timeout 0 app:app
