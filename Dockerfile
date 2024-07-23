FROM python:3.8 AS builder

RUN apt-get update; apt-get clean

RUN pip install Flask gunicorn selenium selenium-wire==5.1.0 pyotp webdriver-manager  blinker==1.7.0 requests

FROM python:3.8

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable

Copycopy code to clipboard
# Installing Unzip
RUN apt-get install -yqq unzip

# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`
curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE
`/chromedriver_linux64.zip

# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

WORKDIR /app
COPY . /app

    

# Install Python dependencies


EXPOSE 8000

CMD exec gunicorn --bind 0.0.0.0:8000 --workers 1 --timeout 0 app:app
