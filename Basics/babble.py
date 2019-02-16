# Write a program to accept a string from user, replace all occurances of 1st character with * in remaining string.
name = str(input('Enter the string: ')) #babble
print("You entered the string as {0}".format(name))
print("Now, first character is {0} and replaced next all occurences by * in given string as: ".format(name[0]))
print(name[0:1]+name[1:].replace('b','*'))
