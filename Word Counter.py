i={}
y=[]
s=input("Enter a string please: ")
s=s.lower()
y=s.split()
for a in y:
    i[a]=i.get(a,0)+1
print(i)        

t=input("Press any key to continue.")