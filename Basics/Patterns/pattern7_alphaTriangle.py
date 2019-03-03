# Write a program to print a pattern which contains triangle of alphabets.

def pattern7(n):
    ch = 65
    for i in range(1,n+1):
        num=ch
        for _ in range(1,n-i+1):
            print(' ',end='')
        for j in range(1,2*i):
            print(chr(num),end='')
            if(j<i):
                num=num-1
            else:
                num=num+1
        print()
        ch+=1
        
def main():
    n=eval(input('Enter the no of rows to print pattern: '))
    pattern7(n)
    
if __name__=='__main__':
    main()
        
