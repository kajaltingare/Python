# Write a program to accept a string from user & check if it is palindrome or not.

def isStrPalindrome(inp_str):
	if(inp_str[::]==inp_str[::-1]):
	    return True
	else:
	    return False
def main():
    inp_str = input('Enter the string to check palindrome for: ')
    if(isStrPalindrome(inp_str)):
        print("Palindrome found!")
    else:
        print("No palindrome.")
if __name__=='__main__':
    main()
