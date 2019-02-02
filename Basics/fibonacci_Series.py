def fiboSeries(n):
    a,b=1,1
    print(a,end='')
    for i in range(1,n-1):
        c=a+b
        print(' %d'%c,end='')
        a=b
        b=c
def main():
    n=eval(input('Enter no of fibo to print: '))
    fiboSeries(n)

if __name__=='__main__':
    main()
