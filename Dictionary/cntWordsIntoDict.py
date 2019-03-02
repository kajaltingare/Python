# Write a program to accept a paragraph from user & return a dictionary of count of words in it.

def cntWordsIntoDict(ipString):
    opDict={}
    for ch in ipString.split():
        if(opDict.get(ch)!=None):
            opDict[ch]+=1
        else:
            opDict[ch]=1
    return opDict
 

def main():
    ipString = eval(input('Enter the sentence to count char in it: '))
    opDict = cntWordsIntoDict(ipString)
    print('Count of words in a paragraph: {0}'.format(opDict))
    

if __name__ == '__main__':
    main()
