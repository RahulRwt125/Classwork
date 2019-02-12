m,r=0,1
while m==0:    
    s=int(input("""Python 3 contains various operators. They are classified based on the function they provide. Which types of operators would you like to view?
    \n Press 1 for arithemetic operators.\n Press 2 for comparison operators."""))
    if (s==1):
        while r==1:
            o1=int(input("""Arithemetic operators are used to carry out basic mathematical problems. 
Which Arithemetic operator would you like to see the functionality of?\n 
    Press 1 for addition.\n    Press 2 for subtraction.\n    Press 3 for multiplication.   
    Press 4 for division.\n    Press 5 for modulus.\n    Press 6 for exponentiation. \n     Your Coice:"""))
            print("We must first get 2 numbers to operate on")
            x,y=int(input("Enter first number:")),int(input("Enter second number:"))
            if(o1==1):
                    z=x+y
                    print("    %d+%d = %d"%(x,y,z))
            elif(o1==2):
                    z=x-y
                    print("    %d-%d = %d"%(x,y,z))
            elif(o1==3):
                    z=x*y
                    print("    %d*%d = %d"%(x,y,z))    
            elif(o1==4):
                    z=x/y
                    print("    %d/%d = %.2f"%(x,y,z))
            elif(o1==5):
                    z=x%y
                    print("    %d%%d = %d"%(x,y,z))
            elif(o1==6):    
                    z=x**y
                    print("    %d raised to %d = %d"%(x,y,z))
            else: 
                    print("The choice of operation is probably incorrect, please choose from 1,2,3,4,5 or 6")
            r=int(input("Press 1 to repeat this module, press any other number to proceed:"))
        m=int(input("Press 0 for main menu, press any other number to exit:"))        
    elif(s==2):
        while r==1:
            x,y=int(input("""Comparison operators , as the name suggests, compare two or more values.
            For instance, we shall take 2 numbers. 
    Enter first number:""")),int(input("    Enter second number:"))
            if x>y:
                print("\n    Since %d is greater than %d, this line of text, executed using the 'Greater than'(>) or 'Greater than or equal to'(>=) operator is displayed"%(x,y))
            elif x<y:
                print("\n    Since %d is lesser than %d, this line of text, executed using the 'Lesser than'(<) or the 'Lesser than or equal to'(<=) operator is displayed"%(x,y))
            elif x==y:
                print("\n    Since %d is equal to %d, this line of text, executed using the 'equal to'(==) operator is displayed."%(x,y))
            print("""\n\n\nThe full lineup of comparison operators is:-
                      1. Equal to (==)
                      2. Not equal to (!=)
                      3. Strictly greater than (>)
                      4. Strictly less than (<)
                      5. Greater than or equal to (>=)
                      6. Less than or equal to (<=)""")
            r=int(input("Press 1 to repeat this module, press any other number to proceed"))
        m=int(input("Press 0 for main menu, press any other number to exit"))  
                