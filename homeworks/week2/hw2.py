# version code 761
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from GF2 import one


## Problem 1
def vec_select(veclist, k): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    result_list = []
    for vector in veclist:
        if vector[k] == 0:
            result_list.append(vector)
    return result_list
  

def vec_sum(veclist, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    result = Vec(D,{})
    return sum(veclist,result)
# test
#D = {'a','b','c'}
#v1 = Vec(D, {'a': 1})
#v2 = Vec(D, {'a': 0, 'b': 1})
#v3 = Vec(D, {        'b': 2})
#v4 = Vec(D, {'a': 10, 'b': 10})
#print(vec_sum([], D))


def vec_select_sum(veclist, k, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    select_list =  vec_select(veclist, k)
    return vec_sum(select_list, D)



## Problem 2
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,3}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
    True
    '''
    result =[]
    for key in vecdict:
        vector = vecdict[key]
        for domain in vector.D:
            vector[domain] = vector[domain] * 1.0 / key
        result.append(vector)
    return result

#test
#v1 = Vec({1,2,3}, {2: 9})
#v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
#print(scale_vecs({3: v1, 5: v2}))
    


## Problem 3
def GF2_span(D, L):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
    >>> len(GF2_span(D, L))
    4
    >>> Vec(D, {}) in GF2_span(D, L)
    True
    >>> Vec(D, {'b': one}) in GF2_span(D, L)
    True
    >>> Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
    True
    >>> Vec(D, {x:one for x in D}) in GF2_span(D, L)
    True
    '''
    result = []
    count = 2 ** len(L)
    # iterate each item by the binary encoding things
    for i in range(count):
        num = i
        list = []
        iter = 0
        while num != 0:
            if num % 2 == 1:
                list.append(L[iter])
            iter += 1
            num = int(num / 2) # using int(), or the num will be double num
        result.append(vec_sum(list, D))   
    return result       

# test
#D = {'a', 'b', 'c'}
#L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
#print(GF2_span(D, L))
#print(len(GF2_span(D, L)))
#print(Vec(D, {}) in GF2_span(D, L))
#print(Vec(D, {'b': one}) in GF2_span(D, L))
#print(Vec(D, {'a':one, 'c':one}) in GF2_span(D, L))
#print(Vec(D, {x:one for x in D}) in GF2_span(D, L))

## Problem 4
# Answer with a boolean, please.

is_it_a_vector_space_1 = True
is_it_a_vector_space_2 = False



## Problem 5
is_it_a_vector_space_3 = True
is_it_a_vector_space_4 = False


## Problem 6

is_it_a_vector_space_5 = True
is_it_a_vector_space_6 = False
