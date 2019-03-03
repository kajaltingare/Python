# Write a program to print UpperRight side patterrn of stars.

def Pattern2(n):
    for i in range(1,n+1):
        for _ in range(1,n-i+1):
            print(' ',end='')
        for _ in range(1,i+1):
            print('*',end='')
        print()
def main():
    n=eval(input('Enter the number of rows to print: '))
    Pattern2(n)
if __name__=='__main__':
    main()
