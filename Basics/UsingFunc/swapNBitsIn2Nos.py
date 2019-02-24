# Write a program to accept two numbers, number of bits & different bits position for them & swap corresponding bits of both numbers.

def swapNBitsIn2Nos(x,y,posx,posy,bits):
    mask = (1<<bits)-1
    x_mask = mask<<(posx-bits)
    
    y_mask = mask<<(posy-bits)
    
    x_part = x & x_mask
    y_part = y & y_mask
    x = x & ~x_mask
    y = y & ~y_mask
    x = x | (y_part<<(posx-posy))
    y = y| (x_part>>(posx-posy))
    return x,y
    

def main():
    x,y,posx,posy,bits = eval(input('Enter the two numbers, position of 1st number, position of 2nd number and no. of bits: '))
    num1, num2 = swapNBitsIn2Nos(x,y,posx,posy,bits)
    print('After swapping: %d->%d and %d->%d'%(x,num1,y,num2))

if __name__ == '__main__':
    main()
