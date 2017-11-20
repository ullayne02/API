import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

sent = 'i cant understanding walking was were is are'
lm = WordNetLemmatizer()
a = sent.split()
b = [lm.lemmatize(x, pos='v') for x in a]
for x in b:
    print(x)
    
    