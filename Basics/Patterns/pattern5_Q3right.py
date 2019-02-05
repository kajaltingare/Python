def pattern5(n):
    for i in range(0,n):
        for _ in range(0,i):
            print(' ',end='')
        for j in range(0,n-i):
            print('*',end='')
        print()

def main():
    n = eval(input('Enter the no of rows want to print pattern: '))
    pattern5(n)

if __name__ == '__main__':
    main()
