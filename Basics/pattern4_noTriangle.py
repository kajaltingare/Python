def pattern4(n):
    for i in range(1,n+1):
        num=i
        for _ in range(1,n-i+1):
            print(' ',end='')
        for j in range(1,2*i):
            print('%d'%num,end='')
            if(j<i):
                num=num-1
            else:
                num=num+1
        print()
def main():
    n=eval(input('Enter the no of rows to print: '))
    pattern4(n)
if __name__=='__main__':
    main()
