from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask


app=Flask(__name__)

def main():
  chrome_options = Options()
# Important Arguments won't eun without them in Gitpod
  chrome_options.add_argument("--disable-dev-shm-usage") 
  chrome_options.add_argument("--headless")  
  
  # Setup ChromeDriver
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=chrome_options)
  
  driver.get("https://www.cricbuzz.com/")
  print(driver.title)
  print(driver.title, flush=True)
  print(driver.current_url)
  print(driver.current_url, flush=True)
  driver.quit()

if __name__ == "__main__":
  main()
