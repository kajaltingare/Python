# Write a program to accept a sentence from user & return dictionary containing count of each character in it.

def cntCharInDict(ipString):
    opDict={}
    for ch in ipString:
        if(opDict.get(ch)!=None):
            opDict[ch]+=1
        else:
            opDict[ch]=1
    return opDict
 

def main():
    ipString = eval(input('Enter the sentence to count char in it: '))
    opDict = cntCharInDict(ipString)
    print('Count of characters in a sentence: {0}'.format(opDict))
    

if __name__ == '__main__':
    main()
