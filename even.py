def evenodd(*a):
    
    i=0
    while i<len(a):
        if a[i]%2==0:
            print("even")
        else:
            print("odd")
        i=i+1
evenodd(2,3,4,65,76,90)  
