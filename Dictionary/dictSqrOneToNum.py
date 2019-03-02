# Write a program to accept a number from user & return a dictionary of squares from 1 to that number.

def dictSqrOneToNum(num):
    sqrDict={}
    for i in range(1,num+1):
        sqrDict[i]=i*i
    return sqrDict
        
def main():
    num = eval(input('Enter the number: '))
    opDict = dictSqrOneToNum(num)
    print('Dictionary of squares from 1 to {0} is\n{1}'.format(num,opDict))

if __name__ == '__main__':
    main()
