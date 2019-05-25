# 主要有3个文件
# all_urls
# visited_urls

# unvisited_urls = all_urls-visited_urls+err_urls
import numpy as np

def rewrite_urls(path, data):
    with open(path, 'w') as f:
        for line in data:
            f.write(line + '\n')

def load_urls(path):
    with open(path, 'r') as f:
        data = [i.strip('\n') for i in f.readlines()]
    return data


def update_urls(path, data):
    with open(path, 'a') as f:
        for line in data:
            f.write(line + '\n')


def update_all_urls(new_urls):
    # new_urls 是一个 列表
    update_urls('urlsData/all_urls', new_urls)


def update_visited_urls(url):
    # url 是一个 单独的链接
    update_urls('urlsData/visited_urls', [url])


def load_unvisited_urls():
    # 加载所有的urls和浏览过的urls，然后从所有的urls中去掉浏览过的urls
    all_urls = set(load_urls('urlsData/all_urls'))
    rewrite_urls('urlsData/all_urls', list(all_urls))
    visited_urls = set(load_urls('urlsData/visited_urls'))
    rewrite_urls('urlsData/visited_urls', list(visited_urls))
    all_urls.difference_update(visited_urls)
    return np.random.permutation(list(all_urls))
