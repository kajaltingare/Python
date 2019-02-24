# Write a program to print Diamond pattern.

def patternDiamond():
    n=5
    for rows in range(1,n-1):
        for _ in range(1,n-1-rows):
            print(' ',end='')
        for _ in range(0,2*rows-1):
            print('*',end='')
        print()
    else:
        rows=n-1
        while(rows!=n+1):
            for _ in range(1,rows-2):
                print(' ',end='')
            for star in range(0,2*rows-n):
                if(rows==n):
                    print('*')
                    break
                print('*',end='')
            print()
            rows+=1       
                

def main():
    patternDiamond()

if __name__ == '__main__':
    main()
