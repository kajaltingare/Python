# Write a program to accept number from user & print table from 2 to number.
num = eval(input('Enter the number: '))
if(num>=2):
    for j in range(2,num+1):
        for i in range(1,11):      
            print(j*i,end=' ')
        print()
else:
    print('Please enter number>=2')
