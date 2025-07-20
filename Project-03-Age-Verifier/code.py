#Age Verifier (Covers: comparison, logical operators)
age = int(input('Enter your Age: '))

if age > 0 and age <= 18 :
    print('You are Minor.')
elif age >= 18 :
    print('You are Adult.')
elif age >= 60 :
    print('You are Senior Citizen.')
else :
    print('Invalid Age....!')
