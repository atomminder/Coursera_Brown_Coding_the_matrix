from vec import Vec
from mat import Mat
from bitutil import *
from GF2 import one
from matutil import *

## Task 1 part 1
""" Create an instance of Mat representing the generator matrix G. You can use
the procedure listlist2mat in the matutil module (be sure to import first).
Since we are working over GF (2), you should use the value one from the
GF2 module to represent 1"""
G = listlist2mat([[one,0,one,one],[one,one,0,one],[0,0,0,one],[one,one,one,0],[0,0,one,0],[0,one,0,0],[one,0,0,0]])

## Task 1 part 2
# Please write your answer as a list. Use one from GF2 and 0 as the elements.
encoding_1001 = [0,0,one,one,0,0,one]


## Task 2
# Express your answer as an instance of the Mat class.
R = listlist2mat([[0,0,0,0,0,0,one],[0,0,0,0,0,one,0],[0,0,0,0,one,0,0],[0,0,one,0,0,0,0]])

## Task 3
# Create an instance of Mat representing the check matrix H.
H = listlist2mat([[0,0,0,one,one,one,one],[0,one,one,0,0,one,one],[one,0,one,0,one,0,one]])

## Task 4 part 1
def find_error(e):
    """
    Input: an error syndrome as an instance of Vec
    Output: the corresponding error vector e
    Examples:
        >>> find_error(Vec({0,1,2}, {0:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
        >>> find_error(Vec({0,1,2}, {2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{0: one})
        >>> find_error(Vec({0,1,2}, {1:one, 2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{2: one})    
    """
    result = -1
    if e[0] == one:
        result += 4
    if e[1] == one:
        result += 2
    if e[2] == one:
        result += 1
    if result == -1:
        return Vec({0, 1, 2, 3, 4, 5, 6},{})  
    else:
        return Vec({0, 1, 2, 3, 4, 5, 6},{result:one})  

#print(find_error(Vec({0,1,2}, {1:one, 2:one})))

## Task 4 part 2
# Use the Vec class for your answers.
non_codeword = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:one})
error_vector = Vec({0,1,2,3,4,5,6}, {6:one})
code_word = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:0})
original = Vec({0,1,2,3}, {1:one,3:one})
#print(R * code_word)

## Task 5
def find_error_matrix(S):
    """
    Input: a matrix S whose columns are error syndromes
    Output: a matrix whose cth column is the error corresponding to the cth column of S.
    Example:
        >>> S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
        >>> find_error_matrix(S)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0, (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0, (5, 2): 0, (0, 2): 0})
    """
    result_mat = Mat(({0, 1, 2, 3, 4, 5, 6}, S.D[1]),{})
    error_syndromes = mat2coldict(S)
    for i in error_syndromes.keys():
        result_vec = find_error(error_syndromes[i])
        for j in result_vec.f.keys():
            result_mat[(j,i)] = result_vec.f[j]
    return result_mat   
    #print([i+j for j in find_error(mat2coldict(S)[i]).f.keys()] for i in mat2coldict(S).keys())
    #return  Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}),  { (j,i):find_error(mat2coldict(S)[i]).f[j] for j in find_error(mat2coldict(S)[i]).f.keys() for i in mat2coldict(S).keys()})   
    #return  Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}),  { (j,i):1 for j in range(7) for i in mat2coldict(S).keys()})   

        
S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
#print(find_error_matrix(S))

## Task 6
s = "I'm trying to free your mind, Neo. But I can only show you the door. You’re the one that has to walk through it."
P = bits2mat(str2bits(s))
#print(P)
print(len(s))
## Task 7
C = G * P
print(C)
# learned from forum: https://class.coursera.org/matrix-001/forum/thread?thread_id=2392&utm_classid=970260&utm_nottype=class.forum.comment&utm_notid=-1&utm_linknum=4#comment-8046
# I think it is the len of the list returned from str2bits of C and the encoded C, 
# in other word it is the len of string * 8.
bits_before = 896
bits_after = 1568

#E = noise(P, 0.02)

## Ungraded Task
CTILDE = None

## Task 8
def correct(A):
    """
    Input: a matrix A each column of which differs from a codeword in at most one bit
    Output: a matrix whose columns are the corresponding valid codewords.
    Example:
        >>> A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
        >>> correct(A)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
    """
    return (A + find_error_matrix(H * A))

A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
#print(A)
#print(correct(A))