# Write a recursive program to find length of a string.

def recursiveStringLength(inpString):
    i = 0
    if(i==len(inpString)):
        return 0
    else:
        return 1+recursiveStringLength(inpString[i+1:])

def main():
    inpString = eval(input('Enter the string: '))
    result = recursiveStringLength(inpString)
    print('length of given string \'{0}\' = {1}'.format(inpString,result))


if __name__ == '__main__':
    main()
