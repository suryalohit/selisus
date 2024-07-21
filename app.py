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
    for i in range(6):
        print(i)
        time.sleep(3)
    print("end")
        
    
    return '200'


if __name__ == "__main__":
  app.run(host='0.0.0.0', use_reloader=False,port=8000)
