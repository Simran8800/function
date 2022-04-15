def prime_no(num):
    num=int(input("enter the number"))
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
            break
        else:
            print(num,"is a prime number")
    else:
        print(num,'is not a prime no')
prime_no(406)