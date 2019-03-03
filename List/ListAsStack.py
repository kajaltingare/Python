# Write a program to implement stack operations on list.

def pushList(stack,data):
    if(isFull(stack)):
        print('List is full.(Limit=10)')
    else:
        stack.append(data)
        return stack

def popList(stack):
    if(isEmpty(stack)):
        print('List is empty.')
    else:
        stack.pop()
    return stack

def peepList(stack):
    if(isEmpty(stack)):
        print('List is empty.')
    else:
        print(stack[-1])

def isEmpty(stack):
    if(len(stack)==0):
        return True
    else:
        return False

def isFull(stack):
    if(len(stack)==10):
        return True
    else:
        return False

def displayStack(stack):
    print(stack)

def showMenu():
    print('***** Menu *****')
    print('1.Push\n2.Pop\n3.Peep\n4.Display\n5.Exit')


def main():
    stack = eval(input('Enter your list[]: '))
    print('Hardcoding length of stack = 10')
    choice=0
    while(choice!=5):
        showMenu()
        choice = eval(input('Enter your choice: '))
        if(choice==1):
            data = eval(input('Enter data that you want to push: '))
            stack = pushList(stack,data)
            print('After adding data: %s'%stack)
        elif(choice==2):
            stack = popList(stack)
            print('After pop operation: %s'%stack)
        elif(choice==3):
            peepList(stack)
        elif(choice==4):
            displayStack(stack)
        else:
            if(choice==5):
                break
            else:
                print('Please enter valid choice.')
        

if __name__ == '__main__':
    main()
