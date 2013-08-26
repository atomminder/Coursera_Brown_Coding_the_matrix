# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from vec import *
from independence import is_independent
from itertools import combinations

## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        u = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
        if a0 * u == s and b0 * u == t:
            return u
# test
# print(choose_secret_vector(0,1))


## Problem 2
# Give each vector as a Vec instance
secret_a0 = a0
secret_b0 = b0
# just initialize the values
secret_a1 = a0
secret_b1 = a0
secret_a2 = a0
secret_b2 = a0
secret_a3 = a0
secret_b3 = a0
secret_a4 = a0
secret_b4 = a0
while True:
    secret_a1 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
    secret_b1 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
    secret_a2 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
    secret_b2 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
    vecs_3 = [(secret_a0, secret_b0),(secret_a1,secret_b1),(secret_a2,secret_b2)]
    if all(is_independent(list(sum(x,()))) for x in combinations(vecs_3,3)) == True:
        #print(vecs_3)
        break
while True:
    secret_a3 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
    secret_b3 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
    vecs_4 = [(secret_a0, secret_b0),(secret_a1,secret_b1),(secret_a2,secret_b2),(secret_a3,secret_b3)]
    if all(is_independent(list(sum(x,()))) for x in combinations(vecs_4,3)) == True:
        #print(vecs_4)
        break
while True:
    secret_a4 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
    secret_b4 = list2vec([randGF2(),randGF2(),randGF2(),randGF2(),randGF2(),randGF2()])
    vecs_5 = [(secret_a0, secret_b0),(secret_a1,secret_b1),(secret_a2,secret_b2),(secret_a3,secret_b3),(secret_a4,secret_b4)]
    if all(is_independent(list(sum(x,()))) for x in combinations(vecs_5,3)) == True:
        #print(vecs_5)
        break
