# Write a program to accept three numbers from user & find minimum of them.
n1,n2,n3=eval(input("Enter the 3 no.s: "))
if(n1<n2 and n1<n3):print("{0} is minimum".format(n1))
elif(n2<n1 and n2<n3):print('%d is minimum.'%n2)
else:print('%d is minimum.'%n3)
