def num(a):
    for i in range (len(a)):
        for j in range (i+1,len(a)):
           if (a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
    print(a)
num([6, 8, 4, 3, 9, 56, 0, 34, 7, 15])
