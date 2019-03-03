# Write a program to print LowerRight side pattern of stars.

def Pattern5(n):
    for i in range(0,n):
        for _ in range(0,i):
            print(' ',end='')
        for j in range(0,n-i):
            print('*',end='')
        print()

def main():
    n = eval(input('Enter the no of rows want to print pattern: '))
    Pattern5(n)

if __name__ == '__main__':
    main()
