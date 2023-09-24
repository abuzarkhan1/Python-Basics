n = int(input("Please Value of n: "))

if(n%2==1):
    print("weird")
elif n%2 == 0 and  2 <= n <= 5:
    print("Not Weird")    
elif n%2 ==0 and 6 <= n <= 20:
    print("Not Weird")    
elif n%2 ==0 and 20 > n:
    print("Not Werid")