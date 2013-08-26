from vecutil import list2vec
from orthogonalization import orthogonalize,aug_orthogonalize
from math import sqrt
from matutil import listlist2mat, coldict2mat, rowdict2mat, mat2coldict, mat2rowdict
from vec import *
from math import sqrt

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    result = orthogonalize(L)
    for vector in result:
        vector_norm = sqrt(vector * vector)
        for key in vector.D:
            vector[key] = vector[key] / vector_norm
    return result

# test
#inlist = [[4,3,1,2],[8,9,-5,-5],[10,1,-1,5]]
#outlist = [
#    [0.73, 0.55, 0.18, 0.37],
#    [0.19, 0.40, -0.57, -0.69],
#    [0.53, -0.65, -0.51, 0.18]]
#
#vlist = [list2vec(x) for x in inlist]
#olist = [list2vec(x) for x in outlist]
#
#a = orthonormalize(vlist)
#print(a)
#print('should be very similar to')
#print(olist)



def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    A,B = aug_orthogonalize(L)
    # multipliers = Vec(L[0].D,{})
    D = set(range(len(L)))
    multipliers = Vec(D,{})
    # normalize
    for i in range(len(A)):
        norm = sqrt(A[i] * A[i])
        for key in A[i].D:
            A[i][key] = A[i][key] / norm
        multipliers[i] = norm
    # multiply with the latter matrix
    for vector in B:
        for i in vector.D:
            vector[i] = multipliers[i] * vector[i]
            
    return A,B


# test
#L = [list2vec(v) for v in [[4,3,1,2],[8,9,-5,-5],[10,1,-1,5]]]
#expectedQ = [list2vec(x) for x in [[0.73, 0.55, 0.18, 0.37], [0.19, 0.40, -0.57, -0.69], [0.53, -0.65, -0.51, 0.18]]]
#actualQ, actualR = aug_orthonormalize(L)
#print(str(L))
#print(str(coldict2mat(actualQ)*coldict2mat(actualR)))