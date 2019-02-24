# Write a program to count no of 1's bits in a given number.

def countNoofOne(n):
    count = 0
    while(n!=0):
        count+=1
        n = n &(n-1)
    return count

def main():
    n = eval(input('Enter the number: '))
    result = countNoofOne(n)
    print('Count of 1 in a given number: %d'%result)

if __name__ =='__main__':
          main()
