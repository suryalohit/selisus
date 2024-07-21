import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask


app=Flask(__name__)

app.debug = True

@app.route('/')
def main():
    print("pdgdx")
        
    
    return 'hi'


if __name__ == "__main__":
  app.run(host='0.0.0.0')
