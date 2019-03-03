# Write a program to print a pattern which contains triangle of stars.

def pattern3(n):
    for i in range(1,n+1):
        for _ in range(1,n-i+1):
            print(' ',end='')
        for _ in range(1,2*i):
            print('*',end='')
        print()
        
def main():
    n=eval(input('Enter the no of rows to print pattern: '))
    pattern3(n)
    
if __name__ == '__main__':
    main()
        
