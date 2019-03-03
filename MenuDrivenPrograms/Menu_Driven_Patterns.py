# Write a menu driven program for all 14 patterns.

def Pattern1(n):
    for i in range(0,n):
        for _ in range(i+1):
            print('*',end='')
        print()

def Pattern2(n):
    for i in range(1,n+1):
        for _ in range(1,n-i+1):
            print(' ',end='')
        for _ in range(1,i+1):
            print('*',end='')
        print()

def Pattern3(n):
    for i in range(1,n+1):
        for _ in range(1,n-i+1):
            print(' ',end='')
        for _ in range(1,2*i):
            print('*',end='')
        print()

def Pattern4(n):
    for i in range(1,n+1):
        num=i
        for _ in range(1,n-i+1):
            print(' ',end='')
        for j in range(1,2*i):
            print('%d'%num,end='')
            if(j<i):
                num=num-1
            else:
                num=num+1
        print()

def Pattern5(n):
    for i in range(0,n):
        for _ in range(0,i):
            print(' ',end='')
        for j in range(0,n-i):
            print('*',end='')
        print()

def Pattern6(n):
    for i in range(1,n+1):
        for _ in range(0,n-i+1):
            print('*',end='')
        print()

def Pattern7(n):
    ch = 65
    for i in range(1,n+1):
        num=ch
        for _ in range(1,n-i+1):
            print(' ',end='')
        for j in range(1,2*i):
            print(chr(num),end='')
            if(j<i):
                num=num-1
            else:
                num=num+1
        print()
        ch+=1

def numStarPattern8(n):
    for i in range(1,n+1):
        for j in range(i,n):
            print(n-j,end=' ')
        for _ in range(1,i+1):
            print('*',end=' ')
        print()

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

def numPattern10Colwise(n):
    for i in range(1,2*n):
        print()
        if(i<=n):
            for j in range(1,i+1):
                print(j,end=' ')
            print('',end=' ')
        else:
            j=0
            for _ in range(i,2*n):
                j+=1
                print(j,end=' ')

def Pattern11Double(n):
    for i in range(1,n+1):
        print(i,end=' ')
        k=i
        for j in range(1,i+1):
            k=k*2
            print(k,end=' ')
        print()

def Pattern12Double(n):
    for i in range(1,n+1):
        for j in range(1,i+2):
            print(i*j,end=' ')
        print()

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

def inpVal():
    n = eval(input('Enter number of rows you want to print pattern: '))
    return n

def patternMenu():
    choice=0
    while(choice!=15):
        print('\n\n***** ALL PATTERN PROGRAMS *****')
        print('\t 1.Pattern1\n\t 2.Pattern2\n\t 3.Pattern3\n\t 4.Pattern4\n\t 5.Pattern5\n\t 6.Pattern6\n\t 7.Pattern7\n\t 8.Pattern8\n\t 9.Pattern9\n\t10.Pattern10\n\t11.Pattern11\n\t12.Pattern12\n\t13.Pattern13\n\t14.Pattern14\n\t15.Exit')
        print('********************************')
        choice = eval(input('Please enter your choice: '))
        print()
        
        if(choice==1):
            n=inpVal()
            Pattern1(n)
        elif(choice==2):
            n=inpVal()
            Pattern2(n)
        elif(choice==3):
            n=inpVal()
            Pattern3(n)
        elif(choice==4):
            n=inpVal()
            Pattern4(n)
        elif(choice==5):
            n=inpVal()
            Pattern5(n)
        elif(choice==6):
            n=inpVal()
            Pattern6(n)
        elif(choice==7):
            n=inpVal()
            Pattern7(n)
        elif(choice==8):
            n=inpVal()
            numStarPattern8(n)
        elif(choice==9):
            n=inpVal()
            Pattern9(n)
        elif(choice==10):
            n=inpVal()
            numPattern10Colwise(n)
        elif(choice==11):
            n=inpVal()
            Pattern11Double(n)
        elif(choice==12):
            n=inpVal()
            Pattern12Double(n)
        elif(choice==13):
            patternDiamond()
        elif(choice==14):
            Pattern_EmptyDiamondInSqr()
        else:
            if(choice==15):
                break
            else:
                print('\nPlease enter correct choice.')

def main():
    patternMenu()

if __name__ == '__main__':
    main()
