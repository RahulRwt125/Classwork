a=0
l=[]
for i in range (1,11):
    x=int(input("Enter number %d : "%i))
    l.append(x)
for i in range (0,10):
    if(l[0]<l[i]):
        a=l[0]
        l[0]=l[i]
        l[i]=a
print("\nGreatest number=%d"%l[0])
for i in range(1,10):
    if(l[1]<l[i]):
        l[1]=l[i]
print("\nSecond largest number=%d"%l[1])        
o=input("Press any key to continue")        
        