#!/usr/bin/env python
#coding:utf-8
import jieba
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

back_color = imread('test1.jpg')  # 解析该图片

wc = WordCloud(background_color='white',  # 背景颜色
               max_words=250,  # 最大词数
               mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=100,  # 显示字体的最大值
               # stopwords=STOPWORDS.add('好评'),  # 使用内置的屏蔽词
               font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可更换字体
               random_state=61,  # 为每个词返回一个PIL颜色
               # width=1000,  # 图片的宽
               # height=860  #图片的长
               )
# 添加自己的词库分词，就会直接将'点个赞'当作一个词,也可以加载文件
# jieba.add_word('点个赞')
jieba.load_userdict('userword.txt')

# 打开词源的文本文件
text = open('reviews.txt').read()


# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    with open('stopwords.txt','rb') as f:
        str_text = f.read()
        unicode_text = str_text.decode()  # 把str格式转成unicode格式
        f.close()  # stopwords文本中词的格式是'一词一行'
    for word in word_generator:
        if word.strip() not in unicode_text:
            words_list.append(word)
    return ' '.join(words_list)


text = stop_words(text)

wc.generate(text)
# 基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(back_color)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
# 保存图片
wc.to_file('1.png')