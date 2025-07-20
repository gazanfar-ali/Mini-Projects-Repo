#Password Checker
p = '1826'
count = 0

while count < 3 :
    n = input('\nEnter the Password(0 to exit): ')

    if n == p :
        print('Access Granted')
        break
    elif n== '0':
        print('Program Exited.')
        break
    else :
        print('Access Denied, Try Again')
        count += 1
        if count < 3 :
            print(3 - count, 'attempts left.')
        else :
            print('Too many failed attempts. Access blocked.')
