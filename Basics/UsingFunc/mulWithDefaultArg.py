# Multiplication with default arguments.

def mulWithDefaultArg(a,b,c=1,d=1,e=1):
    return(a*b*c*d*e)

def main():
    print(mulWithDefaultArg(2,2))
    print(mulWithDefaultArg(2,2,2))
    print(mulWithDefaultArg(2,2,2,2))
    print(mulWithDefaultArg(2,2,2,2,2))

if __name__ == '__main__':
    main()
