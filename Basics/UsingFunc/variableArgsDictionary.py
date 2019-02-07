def variableArgsDictionary(a,b,*args,**kwargs):
    print(a,b)
    print(type(args),type(kwargs))
    for x in args:
        print(x)
    for x in kwargs:
        print(x,kwargs[x])

def main():
    variableArgsDictionary(10,20,1,3,5,7,name="Jeetendra",hobby="Teaching")

if __name__ == '__main__':
    main()
