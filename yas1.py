email = input('Enter your email\n')

if email == 'abuzarkhangmail.com' and '@' in email:
    print('Correct email')
    password = input('Enter your password\n')
    
    if password == ' Khan  12':
        print('Finally Correct password welcome')
    else:
        print('Incorrect password. Please re-enter your password.')
        password = input('Enter your password again\n')
        
        if password == 'kna':
            print('Finally Correct password welcome')
        else:
            print('Incorrect password. Too many attempts. Please try again later.')
else:
    print('Incorrect email. Please re-enter your email.')
