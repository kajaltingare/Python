#if your loop terminates then else is executed.
i=0
while i<10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1
else:
    print("Executed else of while.")
