
def fibo(c):
    if c<3 :
        return 1
    else:
        return fibo(c-1)+fibo(c-2)

a = fibo(133)
print(a)