from ..ranker import *
import math
import json
# function that returns a vector of a document based on a query 
# a query with duplicate elements will remove the duplicates to build the vector
# example query = ["cat","bad","cat","bad"] will return a vector with two elements like [0.30102999566398114, 0.15051499783199057]
# because the second "cat" and the second "bad" will be eliminated
def vectorFile(query, text, invertedFile, fileTotalNumber, fileRecoveredNumber):
    query = ranking.removeDuplicates(query)
    for q in query:
        result.append(ranking.weightFileTDIDF(q, text, invertedFile, fileTotalNumber, fileRecoveredNumber))
    return result
    
# function that returns a vector of a query
# a query with duplicate elements will remove the duplicates to build the vector
# example query = ["cat","bad","cat","bad"] will return a vector with two elements like [0.30102999566398114, 0.30102999566398114]
# because the second "cat" and the second "bad" will be eliminated  
def vectorQuery(query, fileTotalNumber, fileRecoveredNumber):
    queryM = ranking.removeDuplicates(query)
    for q in queryM:
        result.append(ranking.weightQueryTDIDF(q, query, fileTotalNumber, fileRecoveredNumber))
    return result


#this function recives a vector 
#return the vector divided by its norm
def cossine (document, query):
    normalizedDoc = normalize(document)
    normalizedQuery = normalize(query)
    for i in range (2):
        result += normalizedDoc[i]*normalizedQuery[i]
    return result
    
# function that return the size of the vector 
def norma (vector): 
    norma = [x**2 for x in vector]
    norma = sum(norma)
    norma = math.sqrt(norma)
    return norma

# function that return the correspondent vector that has the norma equals to 1
def normalize(vector):
    normal = norma(vector)
    result = [x/normal for x in vector]
    return result

# function that gives the similareties between the query and the documents using the cossine as base 
def similarities (query, documents):
    result = [cossine(query, x) for x in documents]
    return result
    
def inverted_file (file, id):
    inv_fil = {}
    result = {}
    file = file.split()
    voc = removeDuplicates(file)
    size = len(file)
    for q in voc:
        result[q] = []
    for q in voc:
        for i in range(size):
            if q == file[i]:
                result[q].append(i)
    inv_fil[id] = result
    with open('data.json', 'a') as outfile:
        json.dump(inv_fil, outfile)
    return inv_fil
