import os
from os import path
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import jieba
import chardet

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
#print(path.join(d, 'test.txt'))
#text = open(path.join(d,'test.txt'),'rb').read()
#text_charInfo = chardet.detect(text)
#print(text_charInfo)


def cut_words():
    text = open(path.join(d, 'test.txt'), encoding='UTF-16').read()
    #seg_list = ' '.join(jieba.cut_for_search(text))
    seg_list = jieba.cut_for_search(text)
    content = ''
    for item in seg_list:
        content += item
        content += " "
    return content


def loadstopwords():
    filepath = path.join(d, '../stopwords/stopwords_cn.txt')
    stopwords = [line.strip() for line in open(filepath, encoding='UTF-8').readlines()]
    return stopwords


def move_stopwords(content, stopwords):
    content_after = ''
    for word in content:
        if word not in stopwords:
            if word != '\t' and '\n':
                content_after += word
    content_after = content_after.replace("   ", " ").replace("  ", " ")
    with open('new_test.txt','w',encoding='UTF-16') as f:
        f.write(content_after)
    return content_after


cut_cotent = move_stopwords(cut_words(),loadstopwords())

seg_list = ' '.join(jieba.cut_for_search(cut_cotent))
wc = WordCloud(scale=2, max_font_size=100, font_path='ttffile/simhei.ttf')
wc.generate_from_text(seg_list)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()

wc.to_file('1900_basic.png')
plt.show()





