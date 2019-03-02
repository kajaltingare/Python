# Write a recursive program to count no.. of 1 bits in it, without using arithmatic operator.

def countOne(num):
    if(num==0):
        return 0
    return 1+countOne(num&(num-1))

def main():
    num = eval(input('Enter the number: '))
    result = countOne(num)
    print('Count of 1 bit: %d'%result)

if __name__ == '__main__':
    main()
