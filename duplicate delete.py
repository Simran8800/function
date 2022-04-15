def duplicate(a):
    list2=[]
    for i in a:
        if i not in list2:
            list2.append (i)
    print(list2)
duplicate( [1,2,3,3,3,3,4,5])
    
