# Write a program to print UpperLeft side pattern of stars.

def pattern1(n):
    for i in range(0,n):
        for _ in range(i+1):
            print('*',end='')
        print()

def main():
    n = eval(input('Enter number of rows you want to print pattern: ')) 
    pattern1(n)
    
if __name__=='__main__':
    main()
