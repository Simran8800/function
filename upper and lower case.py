def str(a):
    lower=0
    upper=0
    for character in a:
        if character.islower():
            lower=lower+1
        elif character.isupper():
            upper=upper+1
    print("lower =",lower)
    print("upper =",upper)
str("The quick Brow Fox")
