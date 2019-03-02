# Write a program to remove all occurances of a given data from the list.

def removeDupCharList(InpList,char):
    while(char in InpList):
        InpList.remove(char)
    return InpList

def main():
    InpList = eval(input('Enter list[]: '))
    char = eval(input('Enter data you want to remove: '))
    result = removeDupCharList(InpList,char)
    print('After removing multiple instances of %s: '%char)
    print(result)

if __name__ =='__main__':
    main()
