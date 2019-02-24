# Write a program to accept two numbers, number of bits & same bits position for them & swap corresponding bits of both numbers.

def swapBitsIn2Nos(x,y,pos,bits):
    mask = (1<<bits)-1
    mask = mask<<(pos-bits)
    x_part = x & mask
    y_part = y & mask
    x = x & ~mask
    y = y & ~mask
    x = x | y_part
    y = y| x_part
    return x,y
    

def main():
    n1,n2,pos,bits = eval(input('Enter the two numbers, same position for numbers and no. of bits: '))
    num1, num2 = swapBitsIn2Nos(n1,n2,pos,bits)
    print('After swapping: %d->%d and %d->%d'%(n1,num1,n2,num2))

if __name__ == '__main__':
    main()
