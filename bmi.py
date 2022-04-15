def age(a,b):
    
    c=b*b
    if a/c<=18.5:
        print("Underweight")
    elif a/c<=25:
        print("normal")
    elif a/c<=30:
        print("overweight")
    elif a/c<=35.0:
        print("older")
a=int(input("enter the waith"))
b=float(input("enter the hight"))
age(a,b)