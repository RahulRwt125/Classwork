x=[]
s=('a','e','i','o','u')
a=input("Enter a string : ")
a=a.lower()
for i in a:
    if i in s:
        x.append(i)
print("\n\nNumber of Vowels:",len(x))
t=input("\n\n\nPress any key to terminate the program:")
