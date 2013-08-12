from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,len(review_options) - 1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    inverse_index = {}
    for (id,document) in enumerate(strlist):
        words = document.split()
        for word in words:
            if word not in inverse_index:
                inverse_index[word] = {id}
            else:
                inverse_index[word].add(id)  
    return inverse_index

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    result = set()
    all_documents =  dict2list(inverseIndex, query)
    for documents in all_documents:
        result |= documents
    return result

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """

    all_documents =  dict2list(inverseIndex, query)
    result = all_documents[0]
    for documents in all_documents[1:]:
        result &= documents
    return result
    return ... 

# test
f = open('stories_small.txt')
stories = list(f)
length = len(stories)
Index = makeInverseIndex(stories)
print(Index)
print(orSearch(Index,['hopelessly','questionable']))
print(andSearch(Index,['suffocatingly','questionable']))