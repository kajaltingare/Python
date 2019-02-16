# Write a program to accept a no, no. of bits, position from user to toggle the no.

def toggleBits(no,pos,bits):
    x = (1<<bits)-1
    x = x<<(pos-bits)
    result = no^x
    return result
    
def main():
    no,pos,bits = eval(input('Enter the no,position,no of bits to turn on: '))
    result = toggleBits(no,pos,bits)
    print('Number after toggle: %d'%result)

if __name__ == '__main__':
    main()
