# Write a program to find string1 is right rotation of string2.

def isRightRotation(firstString, secondString):
    completeStr =  secondString*2
    if(firstString in completeStr):
        return True
    else:
        return False

def main():
    firstString = eval(input('Enter the first string: '))
    secondString = eval(input('Enter the second string: '))
    result = isRightRotation(firstString, secondString)
    if(result):
        print('%s is right rotation of %s'%(firstString,secondString))
    else:
        print('No right rotation found.')

if __name__ == '__main__':
    main()

