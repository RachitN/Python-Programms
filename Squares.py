def func(w,h,s):
    if w<=0:
        return s
    n=int(h/w)
    s=s+n
    h=h-w*n
    mi=min(w,h)
    ma=max(w,h)
    return func(mi,ma,s)
t=int(input())
while t>0:
    w=int(input())
    h=int(input())
    s=0
    mi=min(w,h)
    ma=max(w,h)
    print (func(mi,ma,s))
    t=t-1
