# Write a program to print pattern of square with empty diamond in it.

def Pattern_EmptyDiamondInSqr():
    n=7
    for rows in range(1,n-2):
        if(rows==1 or rows==n):
            for _ in range(1,n+1):
                print('*',end='')
        else:
            for _ in range(rows,n-2):
                print('*',end='')
            for _ in range(1,2*rows-2):
                print(' ',end='')
            for _ in range(rows,n-2):
                print('*',end='')
        print()
    else:
        rows=n-2
        while(rows!=n):
            for _ in range(1,rows-2):
                print('*',end='')
            for _ in range(0,n-rows+1):
                if(rows==n-1):
                    print(' ',end='')
                    break
                print(' ',end='')
            for _ in range(1,rows-2):
                print('*',end='')    
            print()
            rows+=1
        else:
            for _ in range(1,n+1):
                print('*',end='')


def main():
    Pattern_EmptyDiamondInSqr()

if __name__ == '__main__':
    main()
