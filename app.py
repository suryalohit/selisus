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
      
      chrome_options = Options()
      chrome_options.add_argument("--no-sandbox")
      chrome_options.add_argument("--headless")
      chrome_options.add_argument("--disable-gpu")
      chrome_options.add_argument("--disable-dev-shm-usage") 
      chrome_options.add_argument('--remote-debugging-pipe')
      
      service = Service(ChromeDriverManager().install())
      
      driver = webdriver.Chrome(service=service, options=chrome_options)
     
      driver.quit()
      return '200'


if __name__ == "__main__":
  app.run(host='0.0.0.0', use_reloader=False,port=8000)
