def addWithDefArg(a,b,c=0,d=0,e=0):
    return (a+b+c+d+e)

def main():
    print(addWithDefArg(10,20))
    print(addWithDefArg(10,20,30))
    print(addWithDefArg(10,20,30,40))
    print(addWithDefArg(10,20,30,40,50))

if __name__ == '__main__':
    main()
