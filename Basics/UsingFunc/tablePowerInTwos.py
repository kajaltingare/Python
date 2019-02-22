# Write a program to accept any 2's power & print it's table in binary.

def tablePowerInTwos(num):
    for temp in range(1,11):
        if(temp==1):
            one = '0001'
            printBinary(one,num)
        elif(temp==2):
            two = '0010'
            printBinary(two,num)
        elif(temp==3):
            three = '0011'
            printBinary(three,num)
        elif(temp==4):
            four = '0100'
            printBinary(four,num)
        elif(temp==5):
            five = '0101'
            printBinary(five,num)
        elif(temp==6):
            six = '0110'
            printBinary(six,num)
        elif(temp==7):
            seven = '0111'
            printBinary(seven,num)
        elif(temp==8):
            eight = '1000'
            printBinary(eight,num)
        elif(temp==9):
            nine = '1001'
            printBinary(nine,num)
        elif(temp==10):
            ten = '1010'
            printBinary(ten,num)

def printBinary(bits,num):
    temp = num
    loopCnt = 0
    while(temp!=1):
        temp = temp/2
        loopCnt+=1
    for _ in range(0,loopCnt):
        bits = bits + '0'
    print(bits)

def countNoofOne(n):
    count = 0
    while(n!=0):
        count+=1
        n = n &(n-1)
    return count

def main():
    num = eval(input('Enter any number in 2\'s power to print it\'s table: '))
    if(num==1):
        print('Please enter valid number.')
    elif (countNoofOne(num)==1):
            print('Table in binary for number %d'%num)
            tablePowerInTwos(num)
    else:
        print('Please enter valid number.')

if __name__ == '__main__':
    main()
