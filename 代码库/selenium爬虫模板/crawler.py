from parseData import *
from handleUrls import *
from mongoUtils import get_collection
import time

def craw(driver, url):
    collection = get_collection()
    driver.get(url)
    web_data = driver.page_source
    try:

        # 获取新的链接并且更新链接库
        new_urls = get_new_urls(web_data)
        if new_urls is not None:
            update_all_urls(new_urls)
    except:
        pass


    for i in range(len(driver.find_elements('class name','prdmod'))):
        driver.find_elements('class name', 'prdmod')[i].click()
        # 获取商品信息，保存商品信息数据
        item_info = get_item_info(driver)
        print(item_info)
        if item_info is not None:
            collection.insert_many([item_info])
    time.sleep(1)
    update_visited_urls(url)

