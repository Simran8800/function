list=['abc', 'xyz', 'aba', '1221']
i=0
count=0
while i<len(list):
    if len(list[i])>=2:
        if list[i][0]==list[i][(len(list[i])-1)]:
            count=count+1
        i=i+1
print(count)