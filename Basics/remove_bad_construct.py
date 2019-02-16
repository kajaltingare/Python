#Write a program to accept a sentence from user & replace the 'not bad' construct if found with 'good'
inp_stmt=input("Enter the statement: ")
#students are not that bad but still they study.
not_index=inp_stmt.find("not") #index of not=13
if not_index!=-1:
    bad_index=inp_stmt.find("bad")
    if(bad_index!=-1 and bad_index>not_index):
        result=inp_stmt[:not_index]
        result+='good'
        result+=inp_stmt[bad_index+3:]
        print(result)
else:
    print("\'not\' keyword is not found.")


