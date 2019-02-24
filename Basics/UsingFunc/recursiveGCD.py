# Write a program to find GCD of two number recursively.

def recursiveGCD(n1,n2):
    if (n1==n2):
        return n1
    if(n1>n2):
        return recursiveGCD(n1-n2,n2)
    else:
        return recursiveGCD(n1,n2-n1)

def main():
    n1,n2 = eval(input('Enter the two numbers to find GCD: '))
    result = recursiveGCD(n1,n2)
    print('GCD of %d and %d is %d.'%(n1,n2,result))

if __name__ =='__main__':
    main()
