def wordsForNumber(i):
    if(i==1):
        print('One')
    elif(i==2):
        print('Two')
    elif(i==3):
        print('Three')
    elif(i==4):
        print('Four')
    elif(i==5):
        print('Five')
    elif(i==6):
        print('Six')
    elif(i==7):
        print('Seven')
    elif(i==8):
        print('Eight')
    elif(i==9):
        print('Nine')
    else:
        print('Zero')
        
def noInWords(num):
    i=0
    revN = revNo(num)
    while(revN!=0):
        i = i*10+ (revN%10)
        wordsForNumber(revN%10)
        revN = int(revN//10)
    return i
def revNo(num):
    revN=0
    while(num!=0):
        revN = revN*10+ (num%10)
        num = int(num//10)
    return revN

def main():
    num = eval(input('Enter the number you want to print it in words: '))
    returnVal = noInWords(num)
    returnVal = str(returnVal)
    num = str(num)
    if(len(num)== len(returnVal)):
        print()
    else:
        for _ in range(0,len(returnVal)+1):
            print('Zero')
    
if __name__=='__main__':
    main()
