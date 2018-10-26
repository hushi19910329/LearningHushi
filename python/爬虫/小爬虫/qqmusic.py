# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 02:47:37 2018

@author: Administrator
"""

from selenium import webdriver
import requests

import time
song_list = [
        '私奔(live)',
        '男孩',
        '变了',
        '鬼',
        '一往深情',
        '喜剧',
        '给我一点温度',
        '给我一点温度 (Live) Yoyo岑宁儿＆梁博·专场',
        '弯弯的月亮',
        '我爱你中国',
        '回来',
        '像个孩子',
        '长安长安',
        '日落大道'
        ]

for song in song_list[:]:
    try:
        driver=webdriver.Chrome(r'd:/chromedriver.exe')
        song_name = song + '-梁博'
        url = 'https://y.qq.com/'
        driver.get(url)
        time.sleep(10)
        ele = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/input')
        ele.clear()
        ele.send_keys(song_name)
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/button/i').click()
        time.sleep(10)
        txt = driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li/div/div[2]/span/a/span').text
        title0 = driver.current_window_handle 
        
        driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li/div/div[2]/span/a/span[1]').click()
        time.sleep(10)
        play_url = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[1]').get_attribute('href')
        
        # 先跳转至播放页面，获得缓存
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[1]').click()
        time.sleep(10)
        driver.switch_to.window(title0)
        driver.get(play_url)
        time.sleep(10)
        target = driver.find_element_by_xpath('//*[@id="h5audio_media"]')
        fnl_url = target.get_attribute('src')
        data = requests.get(fnl_url)
        with open('D:\\BTSystem\\myCrawler\\liangbo\\'+txt+'.m4a','wb') as f:
            f.write(data.content)
        time.sleep(3)
        driver.quit()
    except:
        print(song_name)
        driver.quit()

dir(driver)
dir(driver.title)
