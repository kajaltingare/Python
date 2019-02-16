#if your loop terminates bcoz of break then else is not executed.
while True:
    i=eval(input("Enter the no:(to break, enter 10) "))
    if(i==10):
        break
    print(i)
else:
        print("Executed else of while.")
