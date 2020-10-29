from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Five import fiveStore
import time

def Shopee(Shop):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    a=0
    final=""
    nameList=[]
    priceList=[]
    sellList=[]
    driver=webdriver.Chrome(r"C:\Users\ASUS\Studio-workspace\Python\chromedriver.exe",chrome_options=chrome_options)
    driver.get("https://shopee.tw/")
    inputBar=driver.find_element_by_class_name("shopee-searchbar-input__input")
    inputBar.send_keys(Shop)
    time.sleep(0.5)
    adBtn=driver.find_element_by_class_name("shopee-popup__close-btn")
    adBtn.click()
    inputBtn=driver.find_element_by_class_name("btn.btn-solid-primary.btn--s.btn--inline")
    inputBtn.click()
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, 150)") 
    time.sleep(1)
    for i in range(10):
        name=driver.find_elements_by_class_name("_1NoI8_._16BAGk")[i].text
        nameList.append(name)
        price=driver.find_elements_by_class_name("_1w9jLI._37ge-4._2ZYSiu")[i].text
        priceList.append(price)
        sellAmount=driver.find_elements_by_class_name("_18SLBt")[i].text
        sellList.append(sellAmount)
        driver.execute_script("window.scrollTo(0, 15)") 
        time.sleep(0.05)
    for i in range(10):
        a=a+1
        final=final+str(a)+"."+"\n"+"商品名稱:"+"\n"+nameList[i]+"\n"+"商品價錢:"+"\n"+priceList[i]+"\n"+"商品已售:"+"\n"+sellList[i]+"\n"
    finalStore=fiveStore()
    final=final+finalStore
    return final
    driver.close()
    driver.quit()

