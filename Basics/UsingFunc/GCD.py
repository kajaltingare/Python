# Write a program to accept two numbers from user & find GCD of them.

def GCD(n1,n2):
    while(n1!=n2):
        if(n1>n2):
            n1-=n2
        else:
            n2-=n1
    return n1

def main():
    n1,n2 = eval(input('Enter the two numbers: '))
    result = GCD(n1,n2)
    print('GCD of %d and %d is %d.'%(n1,n2,result))

if __name__ == '__main__':
    main()
