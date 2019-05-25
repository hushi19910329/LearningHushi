from bs4 import BeautifulSoup
import re


def get_new_urls(web_data):
    new_urls = re.findall('item.gome.com.cn/\w+-\w+\\.html', web_data)
    if len(new_urls) > 0:
        new_urls = ['http://' + url for url in new_urls]
        return new_urls
    else:
        return None


def get_item_info(driver):
    try:
        info = {}
        name = driver.find_element_by_xpath('//*[@id="gm-prd-main"]/div[1]/h1').text
        price = driver.find_element_by_id('prdPrice').text
        try:
            version = driver.find_element_by_class_name('select').text
            info['version'] = version
        except:
            pass
        info['ItemName'] = name
        info['ItemPrice'] = price


        all_param_panels = driver.find_elements('class name', 'param-panel')

        # 商品详情
        driver.find_element_by_xpath('//*[@id="prd_tbox"]/li[1]').click()
        for panel in all_param_panels:
            txt = panel.text
            for line in txt.split('\n'):
                if '：' in line:
                    key = line.split('：')[0]
                    value = line.split('：')[1]
                    info[key] = value
        # 评价数据
        driver.find_element_by_xpath('//*[@id="prd_tbox"]/li[3]/a').click()

        praising = driver.find_element_by_class_name('appraiseType').text
        comments_num = re.findall('全部评价\(\d+\+?\)', praising)
        shaitu = re.findall('晒图\(\d+\+?\)', praising)
        haoping = re.findall('好评\(\d+\+?\)', praising)
        zhongping = re.findall('中评\(\d+\+?\)', praising)
        chaping = re.findall('差评\(\d+\+?\)', praising)
        info['commentsNumber'] = comments_num[0] if len(comments_num)==1 else None
        info['shaitu'] = shaitu[0] if len(shaitu)==1 else None
        info['haoping'] = haoping[0] if len(haoping)==1 else None
        info['zhongping'] = zhongping[0] if len(zhongping)==1 else None
        info['chaping'] = chaping[0] if len(chaping)==1 else None

        # 评论关键词
        spots = driver.find_element_by_class_name('spots').text
        info['commentsSpots'] = spots


    except:
        info = None

    return info
