
def yanghui(max):
    list1 =[1]
    list2 =[]
    n=0
    while n<max:
        for i in range(n):
            if i==0:
                list2[i] = 1
            else:
                list2[i]=list1[i-1]+list1[i]
        list2.append(1)
        list1 = list2[:]
        yield list2
        n=n+1
    return 'done'

y = yanghui(10)
for a in y:
    for i in a:
        print(i,end=' ')
    print()

