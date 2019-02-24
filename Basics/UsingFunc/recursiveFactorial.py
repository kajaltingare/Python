# Write a recursive program to find factorial of a number.

def recursiveFactorial(n):
    if(n==0 or n==1):
        return 1
    if (n==2):
        return 2
    else:
        return n*recursiveFactorial(n-1)
        

def main():
    num = eval(input('Enter the number to find factorial: '))
    result = recursiveFactorial(num)
    print('%d! = %d'%(num,result))

if __name__ == '__main__':
    main()
