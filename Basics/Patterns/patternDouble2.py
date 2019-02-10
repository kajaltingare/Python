def patternDouble2(n):
    for i in range(1,n+1):
        for j in range(1,i+2):
            print(i*j,end=' ')
        print()

def main():
    n = eval(input('Enter the number: '))
    patternDouble2(n)

if __name__ =='__main__' :
    main()
