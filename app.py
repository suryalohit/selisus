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
      print("start1")
      chrome_options = Options()
      chrome_options.add_argument("--no-sandbox")
    # Important Arguments won't eun without them in Gitpod
      chrome_options.add_argument("--headless")
      chrome_options.add_argument("--disable-gpu")
      
      
      chrome_options.add_argument("--disable-dev-shm-usage") 
      chrome_options.add_argument('--remote-debugging-pipe')
      
      # Setup ChromeDriver
      service = Service(ChromeDriverManager().install())
      driver = webdriver.Chrome(service=service, options=chrome_options)
      
      driver.get("https://www.cricbuzz.com/")
      print("start2")
      print(driver.title)
      print(driver.title, flush=True)
      print(driver.current_url)
      print(driver.current_url, flush=True)
      driver.quit()
      return '200'


if __name__ == "__main__":
  app.run(host='0.0.0.0', use_reloader=False,port=8000)
