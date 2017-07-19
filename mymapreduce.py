from functools import reduce
def myprod(x,y):
    return x*y

list1=[1,2,3,4,5]
result = reduce(myprod,list1)
print(result)
