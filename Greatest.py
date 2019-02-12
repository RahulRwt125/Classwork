a=0
l=[]
for i in range (1,11):
    x=int(input("Enter number %d : "%i))
    l.append(x)
for i in range (0,10):
    if(l[0]<l[i]):
        l[0]=l[i]
print("\nGreatest number=%d"%l[0])
o=input("Press any key to continue")        
        