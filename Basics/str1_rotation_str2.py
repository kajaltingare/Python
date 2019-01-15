# Write a program to accept two strings from user & check if second string is rotation of first.
#
print('If string2 is rotation of string1, it will return true else will return false.')
sINP1 = input('Enter the first string: ')
sINP2 = input('Enter the second string: ')
print(sINP2 in(sINP1+sINP1))
