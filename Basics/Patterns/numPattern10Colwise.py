# Write a program to print flag like pattern of numbers or UpperLeft and LowerLeft pattern of numbers. 

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


def main():
    n=eval(input('Enter number: '))
    if(n<2):
        print('Please enter number>1 to see pattern.')
    else:
        numPattern10Colwise(n)

if __name__ == '__main__':
    main()
