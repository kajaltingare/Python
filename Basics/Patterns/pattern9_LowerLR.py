# Write a program to print cord of lights like pattern of stars or LowerLeftRight both side pattern of stars.

def Pattern9(n):
    for i in range(1,n+1):
        for _ in range(n-i+1):
            print('*',end=' ')
        for _ in range(2,2*i-1):
            print(' ',end=' ')
        if(i==1):
            for _ in range(1,n):
                print('*',end=' ')
        else:
            for _ in range(n-i+1):
                print('*',end=' ')
        print()

def main():
    n = eval(input('Enter number of rows you want to print pattern: ')) 
    Pattern9(n)
    
if __name__=='__main__':
    main()

