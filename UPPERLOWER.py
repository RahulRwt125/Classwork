b=[]
c=[]
a=input("Enter a word : ")
for i in a:
    if(i.isupper()):
        b.append(i)
    elif (i.islower()):
        c.append(i)
print("\n\nNumber of uppercase letters: ",len(b))
print("\nNumber of lowercase letters: ",len(c)) 
o=input("\n\n\nPress any key to exit.")    