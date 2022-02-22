import getpass
correct_pin = int(1234)
attempts = 1
max_attempts = 3

# while loop
while attempts < 4:
    user_pin = int(getpass.getpass(prompt='Please enter your pin: '))
    # conditional if statement within while loop to match user pin to correct pin each time it is entered
    if user_pin != correct_pin and attempts < max_attempts:
        attempts += 1
        print('Incorrect pin, please try again')

# if user input matches pin usr can access account and loop will break early
    elif user_pin == correct_pin:
        print('PIN is correct you can now view your account')
        break
# if user enters wrong pin 3 times they will not be able to access their account. Loop will end early.
    else:
        print('You have entered the incorrect PIN 3 times. Your account is now locked')
        break
