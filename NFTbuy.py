
from ast import While
from email import message
from lib2to3.pgen2.driver import Driver
from multiprocessing import Condition
from operator import truediv
from pickle import TRUE
import sys

from platformdirs import AppDirs
import API
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service


opt = webdriver.ChromeOptions()
opt.add_argument(f"--user-data-dir={API.ChromeID}")
opt.add_experimental_option( 'excludeSwitches',['disable-sync']) 
opt.add_argument('--enable-sync')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
services = Service(API.driverPath)
driver = webdriver.Chrome(service = services,options=opt)
driver.maximize_window()
driver.get(API.Loginlink)
driver.implicitly_wait(60)
time.sleep(3)


def apiCaller():
 listOfCoin=requests.get(API.apiLink).json()

 succesOrFail = listOfCoin["success"]
 print(succesOrFail)

 #This block will fetch data and if fails tells why it failed 
 if succesOrFail == False:
    reasson = listOfCoin["message"]
    print("process failed due to reason = " + reasson)
 else:
    print("We were able to fetch the data")    

 #Now we will get prices of coins by sales Id 
 Coin = listOfCoin["data"]
 for price in Coin:
     WAX = price["price"]
     print("price of the NFT now = "+WAX[ "amount"])
     amtOfAllCoins = WAX[ "amount"]
 totalamt =int(amtOfAllCoins) 
 amtOfOnecoin = totalamt /100000000
 print("PriceOfOneCoin = " + str(amtOfOnecoin) )
 return amtOfOnecoin

#Now we will buy the coins from Website

#Now We will create a buyfunction 
def Buyfunction():
   for index in range(1,20):
        # index = 1
       try:
        buttonXPATH = f'//*[@id="app"]/div/div[4]/main/div/div/div[4]/div[2]/div/div/div/div[{index}]/a/div/div[7]/div/div/button'
        buyButton = f'//*[@id="app"]/div[{index+2}]/div/div/div[3]/button[2]'
        cancelButton = f'//*[@id="app"]/div[{index+2}]/div/div/div[3]/button[1]'
        
        mainBtn = driver.find_element(By.XPATH,buttonXPATH)
        driver.implicitly_wait(60)
        time.sleep(0.27)
        mainBtn.click()
        
        buy = driver.find_element(By.XPATH,buyButton)
        driver.implicitly_wait(60)
        time.sleep(0.27)
        buy.click()
        cancel = driver.find_element(By.XPATH,cancelButton)
       
        time.sleep(0.27)
        cancel.click()
       except NoSuchElementException:
                
                print("-"*30 + f"{index} |  didn't work trying again " + "-"*30)

                continue
#now we will create a condition if its true we if false price was so high 
weAreBuying = True

while  weAreBuying == True:
    apiCaller()
    Buyfunction()
    time.sleep(17)
    driver.close()
    driver.quit()
    driver = webdriver.Chrome(service = services,options=opt)
    driver.maximize_window()
    driver.get(API.Loginlink)
    driver.implicitly_wait(60)
    time.sleep(3)
    
  
    print("We are going to rerun the file")
    
    
  
     
   
 


           

    


    
    













    




