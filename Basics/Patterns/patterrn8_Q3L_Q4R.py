def pattern8(n):
    for i in range(1,n+1):
        for _ in range(0,n-i+1):
            print('*',end='')
        print()

def main():
    n = eval(input('Enter the no of rows want to print pattern: '))
    pattern8(n)

if __name__ == '__main__':
    main()
