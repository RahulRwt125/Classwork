x=[]
s=input("Enter a string please : ")
s=s.lower()
for a in s.split():
    if a.startswith('a'):
        x.append(a)
print(x)        