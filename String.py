import itertools
testcase=int(input())
word=""
while testcase>0:
    n=int(input())
    x=itertools.product('abc',repeat=n)
    g=[i for i in x if i.count('b')<=1 and i.count('c')<=2]
    print(len(g))
    testcase=testcase-1
    
