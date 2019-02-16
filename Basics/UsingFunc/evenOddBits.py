# Write a program to check whether the given no is even or odd without using arithmatic operators.

def IsOdd(num):
    if((num&1)==0):
        return False
    else:
        return True
    
def main():
    num = eval(input('Enter the number: '))
    if(num<=0):
        print('Please enter positive number.')
    else:
        if(IsOdd(num)):
            print('%d is odd number'%num)
        else:
            print('%d is even number'%num)

if __name__ == '__main__':
    main()
