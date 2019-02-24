# Write a program to accept a no & count number of zeros in it.(int=32bits)

def countOfZeros(num):
    cnt = 0
    while(num!=0):
        cnt+=1
        num = num&(num-1)
    return (32-cnt)
        

def main():
    num = eval(input('Enter number to count zeros in it\'s binary: '))
    print('Assumung int is of 32 bits.')
    result = countOfZeros(num)
    print('Number of zero\'s in %d = %d'%(num,result))

if __name__ == '__main__':
    main()
