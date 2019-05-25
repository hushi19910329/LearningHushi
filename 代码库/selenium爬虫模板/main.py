from selenium.webdriver import Chrome
from crawler import craw
from handleUrls import *
import time

nThreads = 5
driver_list = [Chrome('H:\\chromedriver.exe') for _ in range(nThreads)]

ticks = 0
while True:
    unvisited_urls = load_unvisited_urls()
    len(unvisited_urls)
    for i in range(nThreads):
        url = unvisited_urls[i]
        driver = driver_list[i]
        try:
            craw(driver, url)
        except:
            print('Failed!')
            pass

    ticks += 1
    if ticks >= 100:
        print('Restarting drivers......')
        ticks = 0
        for driver in driver_list:
            driver.quit()
        time.sleep(15 * 60)
        driver_list = [Chrome('H:\\chromedriver.exe') for _ in range(nThreads)]

