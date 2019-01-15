name=str(input('Enter the string: ')) #babble
print("You entered the string as {0}".format(name))
print("Now, first character is {0} and replaced next all occurences by * in given string as: ".format(name[0]))
#print(name.replace("b","*")) op: *a**le

firstChar = name[0:1]
#print(firstChar)  op:b

remained = name[1:]
#print(remained)  op:abble

print(firstChar+remained.replace("b","*")) #ba**le

'''
>>> s='babble'
>>> print(s[0]+s[1:].replace(s[0],'*'))
ba**le
>>> '''
