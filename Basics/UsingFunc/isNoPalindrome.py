# Write a program to accept a no from user & check if it is palindrome or not.

def isNoPalindrome(num):
	tempNo = num
	result = 0
	while(tempNo>0):
	    result = result*10 + (tempNo%10)
	    tempNo = tempNo//10
	if(num==result):
	    return True
	else:
	    return False
def main():
    num = eval(input('Enter the number: '))
    if(isNoPalindrome(num)):
        print("Palindrome found!")
    else:
        print("No palindrome.")
if __name__=='__main__':
    main()
