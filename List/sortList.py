# Write a program to sort a list.

def sortList(InpList):
    for i in range(0,len(InpList)-1):
        for j in range(i+1,len(InpList)):
            if(InpList[i]>InpList[j]):
                temp = InpList[i]
                InpList[i]=InpList[j]
                InpList[j]=temp
    return InpList

def main():
    InpList = eval(input('Enter the list[]: '))
    opList = sortList(InpList)
    print('After sorting the list: ')
    print(opList)

if __name__ == '__main__':
    main()
