# Write a program to accept a list from user & check if it is sorted or not.

def isListSorted(InpList):        
    for i in range(1,len(InpList)):
        if(InpList[i-1]<=InpList[i]):
            pass
        else:
            return False
    else:
        return True      

def main():
    InpList = eval(input('Enter the list[]: '))
    if(isListSorted(InpList)):
        print('Given list is sorted.')
    else:
        print('List is not sorted.')

if __name__ == '__main__':
    main()
