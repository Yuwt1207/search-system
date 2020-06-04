from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag

deleteSignal = [',', '.', ';', '&', ':', '>', "'", '`', '(', ')', '+', '!', '*', '"', '?']

#获得word词性，以便lemmatizer更好的还原单词
def get_wordnet_pos(tag: str):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

#将带有标签的单词集tokens还原至初始形态
def stemmer_lemma(tokens_tag: []):
    # porter = PorterStemmer()
    lemma = WordNetLemmatizer()
    res = []
    for word, pos in tokens_tag:
        _pos = get_wordnet_pos(pos) or wordnet.NOUN
        # word = porter.stem(word)
        word = lemma.lemmatize(word, pos=_pos)
        res.append(word)
    # print(res)
    return res
