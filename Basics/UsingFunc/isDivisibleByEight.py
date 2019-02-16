# Write a program to accept a no from user & check if it is divisible by 8 without using arithmatic operators.

def isDivisibleByEight(num):
    if(num&7==0):
        return True
    else:
        return False

def main():
    num = eval(input('Enter the number: '))
    result = isDivisibleByEight(num)
    if(result):
        print('%d is divisible by 8.'%num)
    else:
        print('%d is not divisible by 8.'%num)
    
if __name__ == '__main__':
    main()
