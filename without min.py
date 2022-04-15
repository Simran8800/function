def num(a):
    b=a[0]
    i=0
    while i<len(a):
        if a[i]<b:
            b=a[i]
        i=i+1
    print(b)
num([8, 6, 4, 8, 4, 50, 2, 7])
 