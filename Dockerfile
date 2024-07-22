FROM python:3.8 AS builder

RUN apt-get update; apt-get clean
RUN pip install Flask gunicorn selenium==4.17.2 selenium-wire==5.1.0 pyotp webdriver-manager  blinker==1.7.0 requests==2.32.3

# Install chrome dependencies
RUN apt-get install -y x11vnc xvfb fluxbox wget wmctrl unzip

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable

# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 114.0.5735.90
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR

# Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/win64/chromedriver-win64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR

# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY . /app

    

# Install Python dependencies


EXPOSE 8000

CMD exec gunicorn --bind 0.0.0.0:8000 --workers 1 --timeout 0 app:app
