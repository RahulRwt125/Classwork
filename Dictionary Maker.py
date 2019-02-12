k=0
p=0
a=[]
b=[]
n=int(input("How many elements are there in list 1? : "))
for i in range (1,n+1):
    x=input("Enter element %d : "%i)
    a.append(x)
m=int(input("How many elements are there in list 2? : "))
for j in range (1,m+1):
    y=input("Enter element %d : "%j)
    b.append(y)
r=dict(zip(a,b))
print ("\nHere is the generated dictionary:",r)

t=input("\n\nPress any key to terminate:")