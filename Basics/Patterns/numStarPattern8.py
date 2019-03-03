# Write a program to print pattern of reducing no & incrementing stars.

def numStarPattern8(n):
    for i in range(1,n+1):
        for j in range(i,n):
            print(n-j,end=' ')
        for _ in range(1,i+1):
            print('*',end=' ')
        print()

def main():
    n = eval(input('Enter the number of rows: '))
    numStarPattern8(n)

if __name__ == '__main__':
    main()
