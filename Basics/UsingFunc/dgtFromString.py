# Write a program to accept a string from user & print extracted digits from given string.
def dgtFromString(inpString):
    result=''
    for i in range(0,len(inpString)):
        if((inpString[i]).isdigit()):
            result = result + inpString[i]
        else:
            continue
    return result
    
def main():
    inpString = input('Enter the string: ')
    opString = dgtFromString(inpString)
    print('String after extracting digits from given string: {0}'.format(opString))
    
if __name__ == '__main__':
    main()
            
        
    
