total_sum = 0

while True:
    user_input = input("Enter a number (or 'x' to exit): ")
    
    if user_input == 'x':
        break
    
    if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
        num = float(user_input)
        total_sum += num
    else:
        print("Invalid input. Please enter a valid number or 'x' to exit.")

print("Sum of all entered numbers:", total_sum)
