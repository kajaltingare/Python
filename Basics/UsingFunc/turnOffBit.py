def turnOffBit(no,pos):
    x = 1
    x = x<<(pos-1)
    x = ~x
    result = no & x
    return result

def main():
    no,pos = eval(input('Enter the no, position: '))
    result = turnOffBit(no,pos)
    print('Number after turning off bit: %d'%result)
    
if __name__ == '__main__':
    main()
