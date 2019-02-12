a=[]
b=[]
n=int(input("How many numbers are there in list 1? : "))
for i in range (1,n+1):
    x=int(input("Enter number %d : "%i))
    a.append(x)
m=int(input("How many numbers are there in list 2? : "))
for j in range (1,m+1):
    y=int(input("Enter number %d : "%j))
    b.append(y)
c=a+b
d=[i for i in c if i%2==0]
print("\n\nEven numbers of these two lists = ",d)
o=input("\n\n\nPress any key to exit.")    