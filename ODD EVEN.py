a=0
l=[]
n=int(input("How many numbers are there? : "))
for i in range (1,n+1):
    x=int(input("Enter number %d : "%i))
    l.append(x)
e=[]
o=[]
for a in l:
    if(a%2==0):
        e.append(a)
    else:
        o.append(a)
print("\n\nEven numbers= ",e)
print("\nOdd numbers= ",o)        

t=input("\n\n\nPress any key to continue")