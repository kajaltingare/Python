# Write a program to accept a sentence from user which contains lowercase and uppercase data & return a dictionary containing total no. of lowercase and uppercase characters.

def cntLowerUpperCharIntoDict(ipString):
    opDict={}
    lowerCnt,upperCnt=0,0
    for i in range(0,len(ipString)):
        if(ipString[i].islower()):
            lowerCnt+=1
            opDict['lowercase'] = lowerCnt
        else:
            upperCnt+=1
            opDict['uppercase']=upperCnt
    return opDict
 

def main():
    ipString = eval(input('Enter the sentence to count char in it: '))
    opDict = cntLowerUpperCharIntoDict(ipString)
    print('Dictionary of count of lowercase & uppercase characters in {0}:{1}'.format(ipString,opDict))
    

if __name__ == '__main__':
    main()
