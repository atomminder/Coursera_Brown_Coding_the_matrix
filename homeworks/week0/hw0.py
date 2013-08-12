# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [ x for x in L if x % num != 0]

L = [1,2,4,5,7]
num = 2
print(myFilter(L,num))


## Problem 2
def myLists(L):
    newList = []
    for l in L:
        newList.append([x for x in range(1,l+1)])
    return newList

print(myLists(L))



## Problem 3
def myFunctionComposition(f, g): 
    composition = {}
    for key in f.keys():
        composition[key] = g[f[key]]
    return composition

f = {0:'a', 1:'b'}
g = {'a':'apple', 'b':'banana'}
print(myFunctionComposition(f, g))

## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j 
complex_addition_b = 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = .001 + 9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    total = 0
    for num in L:
        total += num
    return total



## Problem 7
def myProduct(L):
    product = 1
    for num in L:
        product *= num
    return product



## Problem 8
def myMin(L):
    result = L[0]
    for index in range(1,len(L)):
        if L[index] < result:
            result = L[index]
    return result

print(myMin([1,2,3,4,5]))

## Problem 9
def myConcat(L):
    newString = ''
    for string in L:
        newString += string
    return newString



## Problem 10
def myUnion(L):
    result = set()
    for s in L:
        result |= s
    return result

