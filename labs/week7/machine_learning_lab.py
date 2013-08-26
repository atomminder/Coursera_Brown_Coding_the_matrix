from mat import *
from vec import *
from cancer_data import *
from vecutil import *
from matutil import *
from math import *

## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    v = Vec(u.D,{})
    for key in u.D:
        if u[key] >= 0:
            v[key] = 1
        else:
            v[key] = -1
    return v

# test
# print(signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1}))

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    '''
    v = signum(A * w)
    total = len(b.D)
    differs = 0
    for key in b.D:
        if b[key] != v[key]:
            differs = differs + 1
    return differs * 1.0 / total 

# test
#A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])
#b1 = list2vec([1, 1, -1, -1, 1])
#print(fraction_wrong(A1, b1, Vec(A1.D[1], {})))

## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    '''
    return (A * w - b) * (A * w - b)

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    '''
    return  2 * (A * w  - b) * A

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    '''
    return w - sigma * find_grad(A, b, w)

