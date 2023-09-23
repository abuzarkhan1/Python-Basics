
import time
 
sir  = input("Enter Your Name Sir:- ").title()

hour = int(time.strftime("%H")) 
if hour <= 4 | hour < 12 : 
    print("Good Morning Sir")
elif hour <= 17 | hour < 21 :
    print("Good AfterNoon Sir")
else :
    print("Good Night Sir")  