# Write a program to accept a no, no. of bits & position to turn off from given no. Print no after turning off bits in decimal.

def turnOffBits(no,bits,pos):
    x = (1<<bits) - 1
    x = x<<(pos-bits)
    result = no & ~x
    return result

def main():
    no,bits,pos = eval(input('Enter the no, no of bits to turn off, position: '))
    result = turnOffBits(no,bits,pos)
    print('Number after turning off bit: %d'%result)
    
if __name__ == '__main__':
    main()
