from mat import Mat
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    result_mat = Mat((labels,labels), {})
    for label in labels:
        result_mat.f[(label,label)] = 1
    return result_mat

# test
# A = identity({'r','g','b'})
# print(A)

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    result_mat = identity()
    result_mat[('x','u')] = x
    result_mat[('y','u')] = y
    return result_mat

# test
# print(translation(2,3))

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    result_mat = identity()
    result_mat[('x','x')] = a
    result_mat[('y','y')] = b
    return result_mat


## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    result_mat = identity()
    result_mat[('x','x')] = math.cos(angle)
    result_mat[('y','y')] = math.cos(angle)
    result_mat[('x','y')] = -math.sin(angle)
    result_mat[('y','x')] = math.sin(angle)
    return result_mat

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y) * rotation(angle) * translation(-x,-y)    
# test
# print(rotate_about(1,1,30))

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    result_mat = identity()
    result_mat[('x','x')] = -1
    return result_mat

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    result_mat = identity()
    result_mat[('y','y')] = -1
    return result_mat
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    result_mat = identity(labels = {'r','g','b'})
    result_mat[('r','r')] = scale_r
    result_mat[('g','g')] = scale_g
    result_mat[('b','b')] = scale_b
    return result_mat

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    result_mat = identity(labels = {'r','g','b'})
    result_mat[('r','r')] = 77/256
    result_mat[('r','g')] = 151/256
    result_mat[('r','b')] = 28/256
    result_mat[('g','r')] = 77/256
    result_mat[('g','g')] = 151/256
    result_mat[('g','b')] = 28/256
    result_mat[('b','r')] = 77/256
    result_mat[('b','g')] = 151/256
    result_mat[('b','b')] = 28/256    
    return  result_mat

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


