# Write a program to check whether the given no is multiple of 512.

def isMultiple512(num):
    if(num&511==0):
        return True
    else:
        return False

def main():
    num = eval(input('Enter the number: '))
    result = isMultiple512(num)
    if(result):
        print('%d is multiple of 512.'%num)
    else:
        print('%d is not multiple of 512.'%num)
    
if __name__ == '__main__':
    main()
