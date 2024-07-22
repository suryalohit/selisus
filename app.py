import time
import json
import requests

from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





app=Flask(__name__)

app.debug = True

@app.route('/')
def main():
    
      chrome_options = Options()
      
      chrome_options.add_argument("--no-sandbox")
     
      chrome_options.add_argument("--disable-gpu")
      chrome_options.add_argument("--disable-dev-shm-usage") 
      chrome_options.add_argument('--remote-debugging-pipe')
      
      
      service = Service(ChromeDriverManager().install())
      
      driver = webdriver.Chrome( options=chrome_options)
      veg_dict = {}
      veg_dict["width"] = 430
      veg_dict["height"] = 932
      veg_dict["deviceScaleFactor"] = 0
      veg_dict["mobile"] = True
      driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride",veg_dict)
      driver.get("https://x.com/i/flow/login")
      time.sleep(15)
     
      print("1")
      print(driver.get_screenshot_as_base64())
      username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "text")))
      username.click()
      username.send_keys('devikagoud245@gmail.com')
      WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'))).click()
      time.sleep(10)
      
      try:
            print("2")
            print(driver.get_screenshot_as_base64())
            check = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "text")))
            check.click()
            check.send_keys('retiredHippo')
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button'))).click()
            time.sleep(3)
          

      except:
            print("except")

 
    
      password =WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
      password.click()
      password.send_keys('Asailohit30@')
      WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'))).click()
      print(driver.get_screenshot_as_base64())
      
      
      print("login done")
      results={}
      #for i in range(1,10):
      for i in range(1):
           
            print(f"running round:{i}")
            try:
                 
                  driver.get('https://x.com/home/')
              
                  
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
                  
                  print("10")
                  driver.set_window_size(1920, 780)
                  driver.get('https://x.com/home/')
                  print("1") 
                  time.sleep(10)
                  print(driver.get_screenshot_as_base64())
                  available_spaces = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-175oi2r.r-1habvwh.r-eqz5dr.r-1wtj0ep.r-1mmae3n.r-3pj75a.r-lrvibr.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l')))
                  print("2")
                  print(f"total spaces available : {len(available_spaces)}")
    
                  for spaces in available_spaces:
                        driver.set_window_size(1920, 980)
                        print("3")
                        spaces.click()
                        print("4")
                        time.sleep(6)
                        print("5")
                        print("open the space")
                        
                        parts = driver.current_url.split('/')
                        spaceid = parts[5]
                        print(spaceid)
                        print("6")
                        if spaceid not in  list(results.keys()):
                              print("13")
                              ##
                              
                              pf=WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.css-1jxf684.r-dnmrzs.r-1udh08x.r-3s2u2q.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3.r-1wvb978.r-1vr29t4')))
                              print("7")
                              print(f"profiles nummber is : {len(pf)}")
                              print("8")
                             
                              
                              results[spaceid]={'host': "ajhgfd", 'speaker': set(), 'url': "z"}
                              print("1.2")
                              
                             
                              host=pf[0].text
                              results[spaceid]['host']=host
                              print(results[spaceid]['host'])
                              print("1.2.1")
                              
                              results[spaceid]['host']=str(pf[0].text)
                              print("1.3")
                              
                              
                              for p in range(1,len(pf)):
                                    results[spaceid]['speaker'].add(pf[p].text)
                                    print(pf[p].text)
                                    
                              print("1.5.0")   
                              #annaon
                              time.sleep(10)
                              print(driver.get_screenshot_as_base64())
                              WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.r-30o5oe.r-1p0dtai.r-1pi2tsx.r-1d2f490.r-crgep1.r-t60dpp.r-u8s1d.r-zchlnj.r-ipm5af.r-13qz1uu.r-1ei5mc7'))).click()
                              #listen
                              print("1.5.1")  
                              WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.css-175oi2r.r-1udnf30.r-1uusn97.r-h3s6tt.r-1udh08x.r-13qz1uu.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l.r-105ug2t'))).click()
                              print("1.5.2")  
                              
                              time.sleep(10)
                              results[spaceid]['url']=driver.wait_for_request('prod-fastly', timeout=12).url
                              
                              print("1.7")
                              #end listen
                              WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l'))).click()

             
            except:
                  print("except")
               
      print(results)    
      driver.quit()
      return '200'


if __name__ == "__main__":
  app.run(host='0.0.0.0', use_reloader=False,port=8000)
