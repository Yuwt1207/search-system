import os
import nltk
import loading
import stemming
import searching
import getscore
from nltk import word_tokenize, pos_tag

if __name__ == '__main__':
    #获取路径
    path = os.getcwd()
    print(path)
    fileNum = 50
    print("---------------loading--------------")
    #获取单词表wordkey（后续可能会用到）、单词倒排索引wordindex
    wordkey, wordindex = loading.getIndex(path)
    print(len(wordkey))
    print("loading complete!")

    print("------------Search Start------------")
    while True:
        print("Please input the query statement:")
        #获取输入
        statement = input()
        #分词，并标记词性
        tokens_tag = pos_tag(nltk.word_tokenize(statement))
        #输入单词预处理
        tokens = stemming.stemmer_lemma(tokens_tag)
        tokens=[word.lower() for word in tokens if word.isalpha()]
        print(tokens)
        #查询相关文件集合
        docset = searching.search(wordindex, tokens)
        #获取文件对应的分数（最高分的k个）
        scorelist = getscore.topK(10, wordindex, fileNum, tokens, docset)
        #无相关返回
        if len(scorelist) == 0:
            print("无相关结果")
            #打印结果
        for doc, score in scorelist:
            doc=doc.rstrip()
            time, url, context = loading.getfile(path, doc,tokens)
            print("------------------------------------")
            print("文章名： "+doc)
            print("分数为： "+"%.3f" % score)
            print("时间为： "+time)
            print("地址为： "+url)
            print("相关内容为：")
            for i in range(len(context)):
                print("第"+str(i+1)+"条内容："+context[i])
        print(tokens)
