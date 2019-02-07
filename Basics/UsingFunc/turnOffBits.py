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
