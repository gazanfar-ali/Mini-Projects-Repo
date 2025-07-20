#Calculator using WHIlE & MATCH CASE
while  True :
    print('\n..............GK Calculatort...............')
    print('1.ADD 2.SUBTARCT 3.MULTIPLY 4.DIVIDE 5.EXIT')

    choice = int(input('\nEnter your choice: '))

    match choice :
        case 1 :
            n1 = float(input('\nEnter the 1st num: '))
            n2 = float(input('Enter the 2nd num: '))
            print("The sum is : ", n1+n2)
        case 2 :
            n1 = float(input('\nEnter the 1st num: '))
            n2 = float(input('Enter the 2nd num: '))
            print('The subtraction is: ', n1-n2)
        case 3 :
            n1 = float(input('\nEnter the 1st num: '))
            n2 = float(input('Enter the 2nd num: '))
            print('The multiplication is: ', n1*n2)
        case 4 :
            n1 = float(input('\nEnter the 1st num: '))
            n2 = float(input('Enter the 2nd num: '))

            if n2 == 0 :
                print('Cannot divide by 0.')
            else :
                print('The division is: ', n1/n2)
        case 5 :
            print("Exited from program.")
            break
        case _ :
            print('Invalid Input...!')
