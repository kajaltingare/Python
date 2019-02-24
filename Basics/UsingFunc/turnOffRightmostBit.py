# Write a program to accept a number & turn off rightmost 1 bit.

def turnOffRightmostBit(n):
   ''' x =1
    while((n&x)==0):
        x=x<<1
    else:
        return (n&~x) '''
   return (n&(n-1))

def main():
    n = eval(input('Enter the number: '))
    result = turnOffRightmostBit(n)
    print('Number after turning off rightmost bit: %d'%result)

if __name__ =='__main__':
    main()
