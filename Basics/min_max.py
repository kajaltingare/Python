# Write a program to accept two numbers from user & subtract min from max,print result.
num1,num2=eval(input("Enter the no.s: "))
if(num1>num2):
        print("%d-%d=%d"%(num1,num2,num1-num2))
else:print("%d-%d=%d"%(num2,num1,num2-num1))

