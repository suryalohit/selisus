import time
import json
import requests

from seleniumwire import webdriver
from selenium.webdriver.common.by import By
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
      driver.set_window_size(1920, 780)
      driver.get("https://x.com/i/flow/login")
      
      time.sleep(5)
      print(driver.get_window_size())
      print("1")
      username = driver.find_element("name", "text")
      username.click()
      username.send_keys('devikagoud245@gmail.com')
      driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').click()
      time.sleep(5)
      try:
            print("2")
            check = driver.find_element("name", "text")
            check.click()
            check.send_keys('retiredHippo')
            driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()
            time.sleep(4)

      except:
            print("except")

      print("3")
      print(driver.get_screenshot_as_base64()) 
      password = driver.find_element("name", "password")
      password.click()
      password.send_keys('Asailohit30@')
      driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button').click()
      
      
      time.sleep(4)
      driver.get('https://x.com/home/')
      time.sleep(6)
      results={}
      #for i in range(1,10):
      for i in range(1):
           
            print(f"running round:{i}")
            try:
                  driver.get('https://x.com/home/')
                  time.sleep(8)
                  print(driver.get_screenshot_as_base64()) 
                  print("4")
                  
                  driver.set_window_size(1920, 780)
                  for space in list(results.keys()):
                        print(f"space name is : {space}")
                        print("5")
                        driver.set_window_size(1920, 780)
                        try:
                              print("6")
                              
                              driver.get(f'https://x.com/i/spaces/{space}/peek')
                              time.sleep(15)
                              print("7")
                              pf=driver.find_elements(By.CSS_SELECTOR, 'span.css-1jxf684.r-dnmrzs.r-1udh08x.r-3s2u2q.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3.r-1wvb978.r-1vr29t4')
                              print("8")
                              for p in range(1,len(pf)):
                                    print("9")
                                    results[space]["speaker"].add(pf[p].text)
                                    print(pf[p].text)


                        except:
                              print("except")  
                              print(results[space])
                              del results[space]
                  time.sleep(4)
                  print("10")
                  driver.set_window_size(1920, 780)
                  driver.get('https://x.com/home/')
                  time.sleep(39)
                  print(driver.get_screenshot_as_base64()) 
                  available_spaces=driver.find_elements(By.CLASS_NAME, 'css-175oi2r.r-1habvwh.r-eqz5dr.r-1wtj0ep.r-1mmae3n.r-3pj75a.r-lrvibr.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l')
                  print(f"total spaces available : {len(available_spaces)}")

                  for spaces in available_spaces:
                        driver.set_window_size(1920, 780)
                        spaces.click()
                        time.sleep(5)
                        print(driver.get_screenshot_as_base64()) 
                        parts = driver.current_url.split('/')
                        spaceid = parts[5]
                        print(spaceid)

                        if spaceid not in  list(results.keys()):
                              print("13")
                              pf=driver.find_elements(By.CSS_SELECTOR, 'span.css-1jxf684.r-dnmrzs.r-1udh08x.r-3s2u2q.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3.r-1wvb978.r-1vr29t4')
                              print(f"profiles nummber is : {len(pf)}")
                              print("1.0")
                              print(driver.get_screenshot_as_base64()) 
                              lis=driver.find_element(By.CSS_SELECTOR, 'button.css-175oi2r.r-1udnf30.r-1uusn97.r-h3s6tt.r-1udh08x.r-13qz1uu.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l.r-105ug2t')
                              
                              print("1.1")
                              print(pf[0].text)
                              
                              driver.save_screenshot("spaceopendddd.png")
                              results[spaceid]={'host': "ajhgfd", 'speaker': set(), 'url': "z"}
                              print("1.2")
                              print(pf[0].text)
                              a="sf"
                              print(type(a))
                              print("1.2")
                              print(type(str(pf[0].text)))
                              host=pf[0].text
                              results[spaceid]['host']=host
                              print(results[spaceid]['host'])
                              print("1.2.1")
                              
                              results[spaceid]['host']=str(pf[0].text)
                              print("1.3")
                              
                              print("1.4")
                              for p in range(1,len(pf)):
                                    results[spaceid]['speaker'].add(pf[p].text)
                                    print(pf[p].text)

                              print("1.5")
                              print(lis.text)
                              annon=driver.find_element(By.CSS_SELECTOR, 'input.r-30o5oe.r-1p0dtai.r-1pi2tsx.r-1d2f490.r-crgep1.r-t60dpp.r-u8s1d.r-zchlnj.r-ipm5af.r-13qz1uu.r-1ei5mc7')
                              annon.click()
                              time.sleep(13)
                              lis.click()
                              
                              time.sleep(5)
                              
                              
                              
                              print(len(driver.requests))
                              results[spaceid]['url']=driver.wait_for_request('prod-fastly', timeout=12).url
                              print("1.7")

                              enddd=driver.find_element(By.CSS_SELECTOR, 'button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l')
                              
                              
                              print("1.8")
                              enddd.click()
                              time.sleep(4)
                              print(driver.get_screenshot_as_base64()) 

                              


                          

            except:
                  print("except")
               
      print(results)    
      driver.quit()
      return '200'


if __name__ == "__main__":
  app.run(host='0.0.0.0', use_reloader=False,port=8000)
