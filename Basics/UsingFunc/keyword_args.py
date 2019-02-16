#keyword argument - basic

def myAdd(a,b,c):
    return(a+b+c)
def main():
   # print(myAdd(1,c=1,1)) #for this it throws error as
   #positional arg follows keyword args.
   print("Additon: ",myAdd(1,c=1,b=1))
if __name__=='__main__':
    main()
