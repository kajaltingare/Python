def cntConsonent(inpString):
    count = 0
    for i in inpString:
        if(i in "aeiouAEIOU"):
            continue
        else:
            count+=1        
    return count

def main():
    inpString = eval(input('Enter the string: '))
    count = cntConsonent(inpString)
    print('Count of consonents in {0} is {1}'.format(inpString,count))

if __name__ == '__main__':
    main()
