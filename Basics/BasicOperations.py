# Write a program to accept two numbers from user and perform basic mathematical operations on it.
num1=int(input('Enter the first number: \n'))
num2=int(input('Enter the second number: \n'))

#Addition
sum=num1+num2 
print("Addition: {0}+{1} = {2}".format(num1,num2,sum))

#Subtraction
print("Subtraction: {0}-{1} = {2}".format(num1,num2,num1-num2))

#Multiplication
print("Multiplication: {0}*{1} = {2}".format(num1,num2,int(num1*num2)))

#Division
print("Division: {0}/{1} = {2}".format(num1,num2,num1/num2))

#Exponential
print("Exponential: {0}^{1} = {2}".format(num1,num2,num1**num2))
print("Exponential by built-in function: ",pow(num1,num2))
