
a = int(input("Enter Ist number"))
b = int(input("Enter Second Number"))

c = input("Enter Operator");

if(c=="+") :
    print("Sum of two number =" , a + b)
elif (c=="-") : 
    print("Subtraction of two number =" , a - b)
elif (c=="*") :
    print("Multiplication of two number = " , a * b)
elif (c == "/") : 
    print("Divison of two number = " , a / b)    
else :
    print("Unvalid Operator")