#Write a program to accept three numbers from user & print max between them.
n1,n2,n3=eval(input("Enter the 3 no.s: "))
if(n1>n2 and n1>n3):
    print("%d is max"%n1)
elif(n2>n3):print("%d is max"%n2)
else: print("%d is max" %n3)
