def factorial(a):
    q=1
    for i in range (1,a+1):
        q=q*i
    print("\nFactorial of",a,"is",q)


x=int(input("Enter the number: "))
factorial(x)

t=input("Press any key to continue.")