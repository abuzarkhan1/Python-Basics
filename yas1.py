email = input('Enter your email\n')

if email == 'abuzargmail.com' and '@' in email:
    print('Correct email')
    password = input('Enter your password\n')
    
    if password == '1122233':
        print('Finally Correct password welcome')
    else:
        print('Incorrect password. Please re-enter your password.')
        password = input('Enter your password again\n')
        
        if password == '11222233':
            print('Finally Correct password welcome')
        else:
            print('Incorrect password. Too many attempts. Please try again later.')
else:
    print('Incorrect email. Please re-enter your email.')
