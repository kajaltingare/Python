#Write a program to accept a string from user & return first two,last two char.

inp_string = eval(input("Enter the string: "))
print("Returning first two and last char of given string as:")
print(inp_string[0:2]+inp_string[-2::])
