# Write a program to print fibonacci series with given upper limit, starting from 1.

def fiboSeries(upperLmt):
    a,b=1,1
    print(a,b,end='')
    #for i in range(1,upperLmt):
    while((a+b)<=upperLmt):
        c=a+b
        print(' %d'%c,end='')
        a=b
        b=c
def main():
    upperLmt = eval(input('Enter upper limit of fibo to print: '))
    fiboSeries(upperLmt)

if __name__=='__main__':
    main()
