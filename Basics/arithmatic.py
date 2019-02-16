# Arithmatic operations with free fall code using function

def myAdd(a,b):
    return (a+b)
def mySub(a,b):
    return (a-b)
def myMul(a,b):
    return (a*b)
def myDiv(a,b):
    return (a/b)
print("Free fall at begin!")
def main():
    a,b=eval(input("Enter the no.s: "))
    print("Addition: ",myAdd(a,b))
    print("Subtraction: ",mySub(a,b))
    print("Multiplication: ",myMul(a,b))
    print("Division: ",myDiv(a,b))
if __name__=='__main__':
    main()
print("Free fall at end!")
    
    
