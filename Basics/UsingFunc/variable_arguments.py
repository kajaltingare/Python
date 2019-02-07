# variable arguments - python supports it
def addVarArgs(*args):
    print(type(args))
    print(args)
    result = 0
    for i in args:
        result+=i
    return result

def main():
    res1 = addVarArgs(10,20)
    print('addVarArgs(10,20): %d'%res1)
    res2 = addVarArgs(10,20,100)
    print('addVarArgs(10,20,100): %d'%res2)

if __name__=='__main__':
    main()
