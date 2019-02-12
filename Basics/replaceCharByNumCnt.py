def replaceCharByNumCnt(inpString):
    result = ""
    i = 0
    while(i<len(inpString)):
        cnt = 1
        ch = inpString[i]
        while(i+1!= len(inpString) and ch==inpString[i+1]):
            cnt+=1
            i+=1
        else:
            i+=1
            result+=ch
            result+=str(cnt)
    returm result 

def main():
    inpString = eval(input('Enter the string: '))
    result = replaceCharByNumCnt(inpString)
    print(result)
  
  if __name__ == '__main__':
      main()
    
