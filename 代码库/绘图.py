import wordcloud
import matplotlib.pyplot as plt

def vis(word_list, path):
    '''说明
    绘制词云图，并且保存到本地
    word_list
        词汇列表
    path
        要保存的词云图的路径
    '''
    myCloudword = wordcloud.WordCloud(font_path='simkai.ttf',
      width=400, height=200,
      scale=1,  # 比例
      max_words=1000,  # 最大字数
      min_font_size=10,  # 最小字体
      random_state=50,  # 随机角度
      background_color='white',  # 背景颜色
      max_font_size=50  # 最大字体
      ).generate(' '.join(word_list))
    plt.figure(figsize=(9, 6))
    plt.imshow(myCloudword)
    # plt.show()
    plt.savefig(path, dpi=400)  # 保存图片


# pyecharts词云图
from pyecharts import WordCloud
wordcloud = WordCloud(width=800,height=500)
wordcloud.add('',
              keyword_list,
              value_list,
              word_size_range=[20,100])
wordcloud.render('wc.html')


def show_img(img,path=''):
    '''说明
    显示图片
    '''
    plt.figure(figsize=(9,6))
    plt.imshow(img, cmap='gray')
    plt.show()
    #plt.savefig(path)


# 乱码问题
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号