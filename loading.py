import json
import os
import nltk
from nltk import pos_tag

# 加载倒排索引文件，转换为字典index
import stemming


def getIndex(path: str):
    # path += "\index.json"
    # file = open("index.json", 'r')
    # index = json.load(file)
    # word = index.keys()
    if os.path.exists("index.json"):
        file = open("index.json", 'r')
        index = json.load(file)
        word = index.keys()
    else:
        dir = "data"
        filelist = os.listdir(dir)
        index = dict()
        for filename in filelist:
            with open(dir + "/" + filename, encoding="UTF-8") as fp:
                title = fp.readline()[:-1]  # 读一行并去掉最后的换行符
                time = fp.readline()[:-1]
                url = fp.readline()[:-1]

                data = fp.read()  # 主体

            result = stemming.stemmer_lemma(pos_tag(nltk.word_tokenize(data)))
            for words in result:
                words = words.lower()
                if words[0] >= 'a' and words[0] <= 'z':
                    if words in index:
                        index[words][title] = index[words][title] + 1 if title in index[words] else 1
                    else:
                        index[words] = dict()
                        index[words][title] = 1

        idxjson = json.dumps(index)
        with open("index.json", "w") as fp:
            fp.write(idxjson)
        word = index.keys()
    return word, index


# 加载doc对应的文章，获取time、url、context
def getfile(path: str, doc: str,tokens:list):
    path += "\data\\"
    with open(path + doc + ".txt", encoding="UTF-8") as file:
        file.readline()
        time = file.readline()
        time = time.strip('\n')
        time = time.strip()
        url = file.readline()
        url = url.strip('\n')
        url = url.strip()
        data=file.read()
        initdata=nltk.word_tokenize(data)
        stemdata=stemming.stemmer_lemma(pos_tag(initdata))
        context=list()
        for word in tokens:
            idx=[index for (index,value) in enumerate(stemdata) if value==word]
            for i in idx:
                leftidx=i-5 if i-5>0 else 0
                rightidx=i+5 if i+5<len(initdata) else len(initdata)
                string=""
                for j in range(leftidx,rightidx):
                    string+=" "+initdata[j] if initdata[j][0].isalnum() else initdata[j]
                context.append(string)
    return time, url, context
