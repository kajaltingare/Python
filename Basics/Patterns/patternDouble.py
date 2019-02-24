# Write a program to print pattern which is double of previous number in a row manner.

def patternDouble(n):
    for i in range(1,n+1):
        print(i,end=' ')
        k=i
        for j in range(1,i+1):
            k=k*2
            print(k,end=' ')
        print()

def main():
    n = eval(input('Enter the number: '))
    patternDouble(n)

if __name__ =='__main__' :
    main()
