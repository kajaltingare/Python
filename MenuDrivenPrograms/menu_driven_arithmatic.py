# Write a menu driven arithmatic oprations based program.

def takeInputVal():
    a,b=eval(input("Enter the two numbers: "))
    return a,b

def myAdd(a,b):
    return (a+b)

def mySub(a,b):
    return (a-b)

def myMul(a,b):
    return (a*b)

def myDiv(a,b):
    return (a/b)

def myExp(a,b):
    return (a**b)

def myMenu():
    choice = 0
    while(choice!=6):
        print('\n****** MENU *****')
        print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponential\n6.Exit')
        choice = eval(input('Please enter your choice: '))
        if(choice==1):
            a,b = takeInputVal()
            print("Addition: %d+%d = %d"%(a,b,myAdd(a,b)))
        elif(choice==2):
            a,b = takeInputVal()
            print("Subtraction: %d-%d = %d"%(a,b,mySub(a,b)))
        elif(choice==3):
            a,b = takeInputVal()
            print("Multiplication: %d*%d = %d"%(a,b,myMul(a,b)))
        elif(choice==4):
            a,b = takeInputVal()
            print("Division: %d/%d = %d"%(a,b,myDiv(a,b)))
        elif(choice==5):
            a,b = takeInputVal()
            print("Exponential: %d ^ %d = %d"%(a,b,myExp(a,b)))
        else:
            if(choice==6):
                break
            else:
                print('\nPlease enter the correct choice.')

def main():
    myMenu()    
    
if __name__ == '__main__':
    main()

