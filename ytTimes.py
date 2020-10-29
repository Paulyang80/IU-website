from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def watch_times(video_clip):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver=webdriver.Chrome(r"C:\Users\ASUS\Studio-workspace\Python\chromedriver.exe",chrome_options=chrome_options)
    driver.get("https://www.youtube.com/?gl=TW&hl=zh-TW")
    time.sleep(2)
    search_input=driver.find_element_by_name('search_query')
    search_input.send_keys(video_clip)
    time.sleep(2)
    start_search_btn=driver.find_element_by_id('search-icon-legacy')
    start_search_btn.click()
    time.sleep(2)
    start_video=driver.find_element_by_class_name('style-scope ytd-video-renderer')
    start_video.click()
    time.sleep(2)
    watching_times=driver.find_element_by_css_selector('#count > yt-view-count-renderer > span.view-count.style-scope.yt-view-count-renderer').text
    driver.close()
    driver.quit()
    return watching_times
    
