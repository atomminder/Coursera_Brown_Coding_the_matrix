from image_mat_util import *

from mat import Mat
from matutil import *
from vec import Vec

from solver import solve

## Task 1
def move2board(v): 
    '''
    Input:
        - v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
    Output:
        - A {'y1','y2','y3'}-vector z, the coordinate representation
          in whiteboard coordinates of the point p such that the line through the 
          origin and q intersects the whiteboard plane at p.
    '''
    result_vec = Vec({'y1','y2','y3'}, {})
    result_vec['y1'] = v['y1'] / v['y3'];
    result_vec['y2'] = v['y2'] / v['y3'];
    result_vec['y3'] = 1;
    return result_vec

## Task 2
def make_equations(x1, x2, w1, w2): 
    '''
    Input:
        - x1 & x2: photo coordinates of a point on the board
        - y1 & y2: whiteboard coordinates of a point on the board
    Output:
        - List [u,v] where u*h = 0 and v*h = 0
    '''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    u = Vec(domain, {})
    u[('y3','x1')] = w1 * x1      
    u[('y3','x2')] = w1 * x2
    u[('y3','x3')] = w1
    u[('y1','x1')] = -x1
    u[('y1','x2')] = -x2
    u[('y1','x3')] = -1
    v = Vec(domain, {})
    v[('y3','x1')] = w2 * x1      
    v[('y3','x2')] = w2 * x2
    v[('y3','x3')] = w2
    v[('y2','x1')] = -x1
    v[('y2','x2')] = -x2
    v[('y2','x3')] = -1
    return [u, v]

## Task 3
# calculate
u1,v1 = make_equations(329,597,0,1)
u2,v2 = make_equations(358,36,0,0)
u3,v3 = make_equations(592,157,1,0)
u4,v4 = make_equations(580,483,1,1)
domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
last_vec = Vec(domain, {})
last_vec[('y1','x1')] = 1
vector_list = [u1,v1,u2,v2,u3,v3,u4,v4,last_vec]
L = rowdict2mat(vector_list)
#print(L)
b = Vec({0,1,2,3,4,5,6,7,8},{8:1})
#print(b)
h = solve(L,b)
#residual = b - L*h
#if residual * residual < 10e-14:
#    print(True)
#else:
#    print(False)
#print(h)
#H = Mat(({'y1', 'y3', 'y2'}, {'x2', 'x3', 'x1'}),{})
#H[('y1','x1')] = 1
#H[('y1','x2')] = 0.0517
#H[('y1','x3')] = -360
#H[('y2','x1')] = -0.382
#H[('y2','x2')] = 0.738
#H[('y2','x3')] = 110
#H[('y3','x1')] = -0.722
#H[('y3','x2')] = -0.0117
#H[('y3','x3')] = 669

#H = Mat(({'y1', 'y3', 'y2'}, {'x2', 'x3', 'x1'}),
#        {('y1','x1'):1,('y1','x2'):0.0517,('y1','x3'):-360,
#         ('y2','x1'):-0.382,('y2','x2'):0.738,('y2','x3'):110,
#         ('y3','x1'):-0.722,('y3','x2'):-0.0117,('y3','x3'):669})

H = Mat(({'y1', 'y3', 'y2'}, {'x2', 'x3', 'x1'}),
        h.f)

## Task 4
def mat_move2board(Y):
    '''
    Input:
        - Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector 
          giving the whiteboard coordinates of a point q.
    Output:
        - Mat instance, each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane 
          of the line through the origin and q).
    '''
    for i in Y.D[1]:
        Y['y1',i] = Y['y1',i] / Y['y3',i]
        Y['y2',i] = Y['y2',i] / Y['y3',i]
        Y['y3',i] = 1      
    return Y

# test
#(X_pts, colors) = file2mat('board.png', ('x1','x2','x3'))
#Y_pts = H * X_pts
#print(Y_pts.D[0])
# print(leY_pts.D[1])
#Y_in = Mat(({'y1', 'y2', 'y3'}, {0,1,2,3}),
#{('y1',0):2, ('y2',0):4, ('y3',0):8,
#('y1',1):10, ('y2',1):5, ('y3',1):5,
#('y1',2):4, ('y2',2):25, ('y3',2):2,
#('y1',3):5, ('y2',3):10, ('y3',3):4})
#print(Y_in)
#print(mat_move2board(Y_in))
#print(Y)