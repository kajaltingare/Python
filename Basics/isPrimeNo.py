def isPrime(num):
    if(num<2):
        return False
    elif(num==2):
        return True
    elif(num%2==0):
        return False
    else:
        i=0
        for i in range(3,int(num/2),i+2):
            if(num%i==0):
                return False
            else:
                return True
def main():
    num = eval(input('Enter the number to check is it prime or not: '))
    if(isPrime(num)):
        print('%d is prime number.'%num)
    else:
        print('%d is not prime number.'%num)
if __name__=='__main__':
    main()
