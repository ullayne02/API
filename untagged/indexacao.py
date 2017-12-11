import os
import pickle

chars = {'!', '"', '(', ')', ',', '/', \
             ':', ';', '?', '[', ']', \
              '`', '{', '|', '}', '.'}
dic = {}
negative_words = {'doesnt','doesnt','should','shouldnt', 'not'} 



def blocking (sentence):
    aux = ''
    block.append(0)
    for i in range(0, len(sentence)):
        aux1 = sentence[i]
        if (aux1 in chars):
            block.append(i+1)
        elif (i == len(sentence)-1):
            aux += aux1
            block.append(i+1)
            print(i)
        else:
            aux += aux1
    return block 
        
dic = {}

def semantic (block, normalization):
    normalization1 = normalization
    normalization = normalization.split()
    index = 0
    words = ''
    i = 0
    for word in normalization: 
        size = len(word)
        if(word[size-1] in chars):
            word = word[:-1]
        dic[word] = []
    for i in range(0, len(block)-1):
        index += 1
        aux1 = block[i]
        aux2 = block[i+1]
        j = aux1
        i = 0
        while(j<aux2):
            blocks = normalization1[aux1:aux2]
            blocks = blockx.split()
            block_word = blocks[i]
            size = len(block_word)
            if(block_word[size-1] in chars):
                block_word = block_word[:-1]
            if(block_word not in negative_words):
                print(block_word)
                dic[block_word].append(index) 
            else: 
                index = -index
                dic[block_word].append(index) 
            j += len(block_word) + 1
            i += 1
            if(i == len(blocks)):
                break
        if (index < 0):  
            index  = -index

sentenca = 'ullayne, nao sou obrigado a conviver com voce. Tchau'
block1 = blocking(sentenca)
semantic(block1, sentenca)
print(dic)