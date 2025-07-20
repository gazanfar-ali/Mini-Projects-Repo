# Stored credentials
u = 'user1'
p = 1234

# Maximum allowed attempts
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    print('\n.....LOGIN PAGE.....')

    un = input('\nEnter username: ')
    pp = int(input('Enter password: '))

    # Check if credentials are correct
    if un == u and pp == p:
        print('Welcome, user1!')
        break
    else:
        # Increment the attempt counter
        attempts += 1
        print(f'Invalid username or password. {max_attempts - attempts} attempts left.')

# If the user has exceeded the max attempts
if attempts == max_attempts:
    print("Too many failed attempts. Try again later.")

