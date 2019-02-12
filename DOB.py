a=[]
n=int(input("How many entries are there?"))
for i in range (1,n+1):
    x=int(input("Enter entry %d = "%i))
    a.append(x)
b=[(2019-x) for x in a]   
for i in range (1,len(b)+1):
    print("The age of entrant %d"%i,"is",b[i-1])