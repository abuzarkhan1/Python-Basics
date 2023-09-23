num1 = int(input("Enter Ist Number"))

num2 = int(input("Enter Second Number"))

opt = input("Enter Operator")

match opt:
    case "+":
        print("Addition of Two Number = " , num1 + num1)
    case "-":
        print("Subtraction of Two Number = " , num1 - num2)
    case "*":
        print("Multiplication of Two Number =", num1 * num2)
    case "/":
        print("Divison of Two Number = ", num1 / num2)   
    case _ :
        print("Invalid operator")             