from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def fiveStore():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver=webdriver.Chrome(r"C:\Users\ASUS\Studio-workspace\Python\chromedriver.exe",chrome_options=chrome_options)
    driver.get("https://www.5music.com.tw/ListArt.asp?art=440475678678")
    clickList=[]
    clickList2=[]
    productList=[]
    final1=""
    time.sleep(0.5)
    for x in range(1,11):
        for y in range(1,5):
            path="#Form1 > table:nth-child(2) > tbody > tr:nth-child("+str(x)+") > td:nth-child("+str(y)+")"
            clickList.append(path)
    for i in range(1,6):
        for j in range(1,5):
            path2="#Form1 > table:nth-child(2) > tbody > tr:nth-child("+str(i)+") > td:nth-child("+str(j)+")"
            clickList2.append(path2)
    for each in clickList:
        product=driver.find_element_by_css_selector(each)
        product.click()
        time.sleep(0.05)
        try:
            productInfo=driver.find_element_by_class_name("font04").text
        except:
            continue
        productList.append(productInfo)
        driver.back()
        time.sleep(0.05)
    page=driver.find_element_by_name("btselchg")
    page.click()
    pageTwo=driver.find_element_by_css_selector("#Table3 > tbody > tr > td > font > select > option:nth-child(2)")
    pageTwo.click()
    for each in clickList2:
        product=driver.find_element_by_css_selector(each)
        product.click()
        time.sleep(0.05)
        try:
            productInfo=driver.find_element_by_class_name("font04").text
        except:
            continue
        productList.append(productInfo)
        driver.back()
        time.sleep(0.05)
    num=1
    for each in productList:
        final1=final1+str(num)+".\n"+each+"\n"
        num=num+1
    return final1
        