# version code 1049
# Please fill out this stencil and submit using the provided submission script.

from orthogonalization import orthogonalize
import orthonormalization
from mat import Mat
from vec import Vec
from vecutil import list2vec
from matutil import listlist2mat
from math import sqrt
from orthogonalization import project_orthogonal 
from matutil import mat2rowdict
from triangular import triangular_solve
from orthonormalization import aug_orthonormalize
from QR import factor

## Problem 1
def basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - a list of linearly independent Vecs with equal span to vlist
    '''
    basic_result =  orthogonalize(vlist)
    final_result = []
    # remove the 0 vector
    for v in basic_result:
        if v * v > 10e-20:
            final_result.append(v)
    return final_result

# test
#vlist =[list2vec(x) for x in [[2, 4, 3, 5, 0], [4, -2, -5, 4, 0], [-8, 14, 21, -2, 0], [-1, -4,-4, 0, 0], [-2, -18, -19, -6, 0], [5, -3, 1, -5, 2]]]
#print(basis(vlist))

## Problem 2
def subset_basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - linearly independent subset of vlist with the same span as vlist
    '''
    basic_result =  orthogonalize(vlist)
    final_result = []
    # add in the corresponding non-zero vector
    for i in range(len(vlist)):
        if basic_result[i] * basic_result[i] > 10e-20:
            final_result.append(vlist[i])
    return final_result       



## Problem 3
def orthogonal_vec2rep(Q, b):
    '''
    Input:
        - Q: an orthogonal Mat
        - b: Vec whose domain equals the column-label set of Q.
    Output:
        - The coordinate representation of b in terms of the rows of Q.
    Example:
        >>> Q = Mat(({0, 1}, {0, 1}), {(0, 1): 0, (1, 0): 0, (0, 0): 2, (1, 1): 2})
        >>> b = Vec({0, 1},{0: 4, 1: 2})
        >>> orthogonal_vec2rep(Q, b) == Vec({0, 1},{0: 8, 1: 4})
        True
    '''
    return Q * b

# test
#Q = Mat(({0, 1}, {0, 1}), {(0, 1): 0, (1, 0): 0, (0, 0): 2, (1, 1): 2})
#b = Vec({0, 1},{0: 4, 1: 2})
#print(orthogonal_vec2rep(Q, b) == Vec({0, 1},{0: 8, 1: 4}))



## Problem 4
def orthogonal_change_of_basis(A, B, a):
    '''
    Input:
        - A: an orthogonal Mat
        - B: an orthogonal Mat whose column labels are the row labels of A
        - a: the coordinate representation in terms of rows of A of some vector v 
    Output:
        - the Vec b such that b is the coordinate representation of v in terms of columns of B
    Example:
        >>> A = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (2, 0): 0, (1, 0): 0, (2, 2): 1, (0, 2): 0, (2, 1): 0, (1, 1): 1})
        >>> B = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 2, (2, 0): 0, (1, 0): 0, (2, 2): 2, (0, 2): 0, (2, 1): 0, (1, 1): 2})
        >>> a = Vec({0, 1, 2},{0: 4, 1: 1, 2: 3})
        >>> orthogonal_change_of_basis(A, B, a) == Vec({0, 1, 2},{0: 8, 1: 2, 2: 6})
        True
    '''
    # still a little confusing
    return (a*A) * B


# test
#A = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (2, 0): 0, (1, 0): 0, (2, 2): 1, (0, 2): 0, (2, 1): 0, (1, 1): 1})
#B = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 2, (2, 0): 0, (1, 0): 0, (2, 2): 2, (0, 2): 0, (2, 1): 0, (1, 1): 2})
#a = Vec({0, 1, 2},{0: 4, 1: 1, 2: 3})
#print(orthogonal_change_of_basis(A, B, a) == Vec({0, 1, 2},{0: 8, 1: 2, 2: 6}))


## Problem 5
def orthonormal_projection_orthogonal(W, b):
    '''
    Input:
        - W: Mat whose rows are orthonormal
        - b: Vec whose labels are equal to W's column labels
    Output:
        - The projection of b orthogonal to W's row space.
    Example: 
        >>> W = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (1, 0): 0, (0, 2): 0, (1, 1): 1})
        >>> b = Vec({0, 1, 2},{0: 3, 1: 1, 2: 4})
        >>> orthonormal_projection_orthogonal(W, b) == Vec({0, 1, 2},{0: 0, 1: 0, 2: 4})
        True
    '''
    # still not know the 7 characters solution
    return  project_orthogonal(b, list(mat2rowdict(W).values()))


# test
#W = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (1, 0): 0, (0, 2): 0, (1, 1): 1})
#b = Vec({0, 1, 2},{0: 3, 1: 1, 2: 4})
#print(orthonormal_projection_orthogonal(W, b) == Vec({0, 1, 2},{0: 0, 1: 0, 2: 4}))
#g2 = 1 / sqrt(2)
#g3 = 1 / sqrt(3)
#W = listlist2mat([[g2,g2,0],[g3,-g3,g3]])
#b = list2vec([10,20,30])
#d = orthonormal_projection_orthogonal(W, b)
#print(d)


## Problem 6
# Write your solution for this problem in orthonormalization.py.



## Problem 7
# Write your solution for this problem in orthonormalization.py.



## Problem 8
# Please give each solution as a Vec

least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]]) 
least_squares_b1 = list2vec([10, 8, 6])

x_hat_1 =  list2vec([1.08,0.984])


least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])

x_hat_2 =  list2vec([2.5,2.66])



## Problem 9
def QR_solve(A, b):
    '''
    Input:
        - A: a Mat
        - b: a Vec
    Output:
        - vector x that minimizes norm(b - A*x)
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR.factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result * result < 1E-10
        True
    '''
    Q,R = factor(A)
    return triangular_solve(mat2rowdict(R),list(A.D[1]), Q.transpose()*b)

# test
#domain = ({'a','b','c'},{'A','B'})
#A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
#Q, R = factor(A)
#b = Vec(domain[0], {'a': 1, 'b': -1})
#x = QR_solve(A, b)
#result = A.transpose()*(b-A*x)
#print(result * result < 1E-10)