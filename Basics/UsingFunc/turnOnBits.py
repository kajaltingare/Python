# Write a program to accept a no from user & no. of bits to turn on from given position.

def turnOnBits(no,pos,bits):
    x = (1<<bits) - 1
    x = x<<(pos-bits)
    result = no | x
    return result

def main():
    no,pos,bits = eval(input('Enter the no,position,no of bits to turn on: '))
    result = turnOnBits(no,pos,bits)
    print('Number after turning off bit: %d'%result)
    
if __name__ == '__main__':
    main()
