#Write a program to print pattern rowwise like a table upto rownum.

def Pattern12Double(n):
    for i in range(1,n+1):
        for j in range(1,i+2):
            print(i*j,end=' ')
        print()

def main():
    n = eval(input('Enter the number: '))
    Pattern12Double(n)

if __name__ =='__main__' :
    main()
