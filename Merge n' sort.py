k=0
p=0
a=[]
b=[]
d=[]
n=int(input("How many numbers are there in list 1? : "))
for i in range (1,n+1):
    x=int(input("Enter number %d : "%i))
    a.append(x)
m=int(input("How many numbers are there in list 2? : "))
for j in range (1,m+1):
    y=int(input("Enter number %d : "%j))
    b.append(y)
c=a+b
print("\n\nMerged List = ",c)   
for p in range (0,len(c)):
    for i in range (p,len(c)):
        if(c[p]>c[i]):
            k=c[p]
            c[p]=c[i]
            c[i]=k
    d.append(c[p])
print("\nSorted list = ",d)  

o=input("\n\n\nPress any key to exit.")         