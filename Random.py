import random

rand = random.randint(1,40)

while(True):
    inputt = int(input("Enter Number: "))
    if(inputt < rand):
        print("Wrong Guess, Try Greater Number")
    elif(inputt > rand):
        print("Wrong Guess, Try Smaller Number")
    else:
        print("Congratualtion You have Guess The Right Answer")        
        break