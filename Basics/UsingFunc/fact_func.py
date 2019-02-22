# Write a program to find factorial of a number.

def factorial(fact):
    
    if(fact<0):
        print('Please enter positive number.')
    else:
        num = 1
        for x in range(2,fact+1):
            num=num*x
        return num
    
def main():
    fact = eval(input('Enter the number whose factorial want to find: '))
    result = factorial(fact)
    print('%d!=%d'%(fact,result))

if __name__ == '__main__':
    main()
