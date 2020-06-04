import cmath

#利用tf*idf对文章doc进行打分
def tfidf(index: dict, fileNum: int, tokens:list, doc:str):
    score = 0
    for word in tokens:
        if word not in index.keys() or doc not in index[word]:
            continue

        tf = index[word][doc]
        df = len(index[word])
        idf = cmath.log10(fileNum+1 / df).real
        score += tf * idf

    return score

#调用tfidf函数，将doclist中的所有文章打分并排序
def getscorelist(index: dict, fileNum: int, tokens:list, doclist:set):
    scorelist = []
    for doc in doclist:
        score = tfidf(index, fileNum, tokens, doc)
        if score != 0:
            scorelist.append([doc, score])

    scorelist.sort(key=lambda s: s[1], reverse=True)
    # for doc, score in scorelist:
    #    print(doc + " 分数为： " + str(score))

    return scorelist

#如果doclist中文章过多，则只返回分数最高的k个
def topK(k:int, index: dict, fileNum: int, tokens:list, doclist:set):
    scorelist = getscorelist(index, fileNum, tokens, doclist)
    size = len(scorelist)
    if size == 0:
        return []
    if size < k:
        return [scorelist[i] for i in range(0, size)]
    else:
        return [scorelist[i] for i in range(0, k)]
