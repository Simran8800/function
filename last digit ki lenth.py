def k(var):
    words=var.split()
    if  len(words)==0:
        return 0
    return len(words[-1])
print(k('hello world '))


