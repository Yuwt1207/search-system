import nltk
import os
import json

#{word:{txttitle:countnum}}字典套字典

def getindex():
    if os.path.exists("index.txt"):
        with open("index.txt","r") as fp:
            data=fp.read()
            idx=json.loads(data)
        # print(idx)
        # print(idx["only"])
        return idx
    else:
        dir="英文文档"
        filelist=os.listdir(dir)
        print(filelist)
        print(len(filelist))
        index = dict()
        for filename in filelist:
            with open(dir+"/"+filename,encoding="UTF-8") as fp:
                title = fp.readline()[:-1]#读一行并去掉最后的换行符
                time = fp.readline()[:-1]
                url = fp.readline()[:-1]

                data = fp.read()#主体

            result = nltk.word_tokenize(data)
            for words in result:
                words = words.lower()
                if words[0] >= 'a' and words[0] <= 'z':
                    if words in index:
                        index[words][title] = index[words][title] + 1 if title in index[words] else 1
                    else:
                        index[words] = dict()
                        index[words][title] = 1
        # print(index)
        # print(len(index))
        idxjson=json.dumps(index)
        # print(idxjson)
        with open("index.txt","w") as fp:
            fp.write(idxjson)
        return index

print("getting index...")
index=getindex()
print("index build ok!")
print(index)
print(index["true"])