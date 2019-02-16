# Write a program to accept a string from user & perform verbing operation.
inp_stmt=input("Enter the statement: ")
if(len(inp_stmt)>=3):
    if(inp_stmt.endswith("ing")):
        print(inp_stmt[:-3]+'ly')
    else:print(inp_stmt+'ing')
else:
    print('Please enter verb atleast 3 or more number of characters in it.')
