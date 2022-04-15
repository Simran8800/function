def num(a):
    i=0
    while i<len(a):
        if a[i]%2==0:
           return a[i]
        else:
           return 'odd'
        i=i+1
print(num([2,3,4,5,6]))

