# Write a program to accept a number from user & find it's factorial.

fact = eval(input("Enter the no whose factorial want to find: "))
num=1
for x in range(fact,1,-1):
    num=num*x
print('%d!=%d'%(fact,num))


'''for x in range(2,fact+1):
    num=num*x
print(num)'''
    
