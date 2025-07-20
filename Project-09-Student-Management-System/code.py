#Student Management System
s = list()

print('Student Management System')

while True:
    print('\n1. Add a Student')
    print('2. Update a Student name')
    print('3. Remove a Student')
    print('4. Search for a Student')
    print('5. Show all Students')
    print('6. Exit the Program\n')

    choice = int(input('Enter your choice: '))

    match choice:
        case 1:
            n = input('Enter the name to Add: ')
            s.append(n)
            print(n, 'added to the list.')

        case 2:
            if len(s) == 0:
                print('No students in the list to update.')
            else:
                try:
                    i = int(input('Enter the index you want to Update: '))
                    if 0 <= i < len(s):
                        n = input("Enter the new name: ")
                        s[i] = n
                        print(n, 'updated at index', i)
                    else:
                        print('Invalid index. Try again.')
                except:
                    print('Please enter a valid number.')

        case 3:
            if len(s) == 0:
                print('No students in the list to remove.')
            else:
                n = input('Enter the name to Remove: ')
                if n in s:
                    s.remove(n)
                    print(n, 'removed from the list.')
                else:
                    print(n, 'not found in the list.')

        case 4:
            n = input('Enter the name to Search: ')
            if n in s:
                print(n, 'is in the list.')
            else:
                print(n, 'is not in the list.')

        case 5:
            if len(s) == 0:
                print('No students found.')
            else:
                print('\nList of Students:')
                for i in range(len(s)):
                    print(i, '->', s[i])

        case 6:
            print("Exited from Program.")
            break

        case _:
            print('Invalid Choice...! Try Again.')
