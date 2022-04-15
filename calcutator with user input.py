def calcutator():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    operation=input("enter the simble,+,-,*,/")
    if operation=="+":
        print("addation=",a+b)
    elif operation=="-":
        print("subtract=",a-b)
    elif operation=="*":
        print("multiply=",a*b)
    elif operation=="/":
        print("division=",a/b)
    else:
        print("invalid")
calcutator()
