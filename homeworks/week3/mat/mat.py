from vec import Vec
from GF2 import one

def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]
    # in case it is a sparse matrix
    if k not in M.f.keys():
        return 0
    else:
        return M.f[k]

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k] = val

def add(A, B):
    "Returns the sum of A and B"
    # define a new matrix as the result
    C = Mat(A.D, {})
    assert A.D == B.D
    for i in A.D[0]:
        for j in A.D[1]:
            C[(i,j)] = A[(i,j)] +B[(i,j)]
    return C

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M" 
    result = Mat(M.D, {})
    if alpha == 0:
        return result
    elif  alpha == 1:
        return M
    else:
        for key in M.f.keys():
            result[key] = M[key] * alpha
        return result

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    for i in A.D[0]:
        for j in A.D[1]:
            if A[(i,j)] != B[(i,j)]:
                return False
    return True

def transpose(M):
    "Returns the transpose of M"
    # first transpose the D
    result = Mat((M.D[1],M.D[0]), {})
    #second transpose the value
    for key in M.f.keys():
        result[(key[1],key[0])] = M[key]
    return result

def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D
    result_vec = Vec(M.D[1],{})
    for j in M.D[1]:
        result_vec[j] = 0
        for i in M.D[0]:
            result_vec[j] += M[(i,j)] * v[i]
    return result_vec
            

def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D
    result_vec = Vec(M.D[0],{})
    for j in M.D[0]:
        result_vec[j] = 0
        for i in M.D[1]:
            result_vec[j] += M[(j,i)] * v[i]
    return result_vec


def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]
    result_matrix = Mat((A.D[0],B.D[1]), {})
    # calculate the value
    for i in result_matrix.D[0]:
        for j in result_matrix.D[1]:
            result_matrix[(i,j)] = 0
            for k in A.D[1]:
                result_matrix[(i,j)] += A[(i,k)] * B[(k,j)]
    return result_matrix             
            
        
    

################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"


print("For  getitem(M, k)")
M = Mat(({1,3,5}, {'a'}), {(1,'a'):4, (5,'a'): 2})
print(M[3,'a'])
# 0
M = Mat((set(range(1000)), {'e',' '}), {(500, ' '): one, (255, 'e'): 0})
print(M[500, ' '])
#one
print(M[500, 'e'])
#0
print(M[255, 'e'])
#0
print(M==Mat((set(range(1000)), {'e',' '}), {(500, ' '): one, (255, 'e'): 0}))
#True


print("For setitem(M,k,val)")
M = Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):7})
M['b', 5] = 9
M['c', 5] = 13
print(M == Mat(({'a','b','c'}, {5}), {('a', 5):3, ('b', 5):9, ('c',5):13}))
#True
#Make sure your operations work with bizarre and unordered keys.
N = Mat(({((),), 7}, {True, False}), {})
N[(7, False)] = 1
N[(((),), True)] = 2
print(N == Mat(({((),), 7}, {True, False}), {(7,False):1, (((),), True):2}))
#True


print("For add(A, B)")
A1 = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3})
A2 = Mat(({3, 6}, {'x','y'}), {(3,'y'):4})
B = Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (3,'y'):4, (6,'y'):3})
print(A1 + A2 == B)
#True
print(A2 + A1 == B)
#True
print(A1 == Mat(({3, 6}, {'x','y'}), {(3,'x'):-2, (6,'y'):3}))
#True
zero = Mat(({3,6}, {'x','y'}), {})
print(B + zero == B)
#True
C1 = Mat(({1,3}, {2,4}), {(1,2):2, (3,4):3})
C2 = Mat(({1,3}, {2,4}), {(1,4):1, (1,2):4})
D = Mat(({1,3}, {2,4}), {(1,2):6, (1,4):1, (3,4):3})
print(C1 + C2 == D)
#True

print("For scalar_mul(M, x)")
M = Mat(({1,3,5}, {2,4}), {(1,2):4, (5,4):2, (3,4):3})
print(0*M == Mat(({1, 3, 5}, {2, 4}), {}))
#True
print(1*M == M)
#True
print(0.25*M == Mat(({1,3,5}, {2,4}), {(1,2):1.0, (5,4):0.5, (3,4):0.75}))
#True
M = Mat(({1,2,3},{4,5,6}), {(1,4):one, (3,5):one, (2,5): 0})
print(one * M == Mat(({1,2,3},{4,5,6}), {(1,4):one, (3,5):one, (2,5): 0}))
#True
print(0 * M == Mat(({1,2,3},{4,5,6}), {}))
#True

print("For transpose(M)")
M = Mat(({0,1}, {0,1}), {(0,1):3, (1,0):2, (1,1):4})
print(M.transpose() == Mat(({0,1}, {0,1}), {(0,1):2, (1,0):3, (1,1):4}))
#True
M = Mat(({'x','y','z'}, {2,4}), {('x',4):3, ('x',2):2, ('y',4):4, ('z',4):5})
Mt = Mat(({2,4}, {'x','y','z'}), {(4,'x'):3, (2,'x'):2, (4,'y'):4, (4,'z'):5})
print(M.transpose() == Mt)
#True

print("For vector_matrix_mul(v, M)")
v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
M1 = Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 2, (2, 1):-1, (3, 1): 1, (3, 3): 7})
print(v1*M1 == Vec({1, 2, 3},{1: -8, 2: 2, 3: 0}))
#True
print(v1 == Vec({1, 2, 3}, {1: 1, 2: 8}))
#True
print(M1 == Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 2, (2, 1):-1, (3, 1): 1, (3, 3): 7}))
#True
v2 = Vec({'a','b'}, {})
M2 = Mat(({'a','b'}, {0, 2, 4, 6, 7}), {})
print(v2*M2 == Vec({0, 2, 4, 6, 7},{}))
#True

print("For matrix_vector_mul(M, v)")
N1 = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
print(N1*u1 == Vec({1, 3, 5, 7},{1: 3, 3: 9, 5: -2, 7: 3}))
#True
print(N1 == Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1}))
#True
print(u1 == Vec({'a', 'b'}, {'a': 1, 'b': 2}))
#True
N2 = Mat(({('a', 'b'), ('c', 'd')}, {1, 2, 3, 5, 8}), {})
u2 = Vec({1, 2, 3, 5, 8}, {})
print(N2*u2 == Vec({('a', 'b'), ('c', 'd')},{}))
#True

print("For matrix_matrix_mul(A, B)")
A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
print(A*B == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31}))
#True
C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2}) 
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
print(C*D == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5}))
#True
M = Mat(({0, 1}, {'a', 'c', 'b'}), {})
N = Mat(({'a', 'c', 'b'}, {(1, 1), (2, 2)}), {})
print(M*N == Mat(({0,1}, {(1,1), (2,2)}), {}))
#True
