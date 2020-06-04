#获取含有单词word的文章集合doclist
def searchOne(index:dict, word:str):
    if word in index:
        doclist = [doc for doc in index[word].keys()]
        return set(doclist)
    else:
        return set([])

#遍历tokens, 并调用searchOne,汇总获得docset
def search(index:dict, tokens:list):
    docset = set()
    if len(tokens) == 0:
        return []
    else:
        for word in tokens:
            docset.update(searchOne(index, word))

    #for doc in doclist:
    #    print(doc)
    return docset




