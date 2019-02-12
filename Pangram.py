x=[]
s=[chr(j) for j in range (97,123)]
s=set(s)
a=input("Enter a string : ")
a=a.lower()
a=set(a)
for i in a:
    if i in s:
        x.append(i)
if (len(x)==26):
    print("\n\nThe string is a Pangram.")
else:
    print("\n\nThe string is not a Pangram.")  
t=input("\n\n\nPress any key to terminate the program.")    