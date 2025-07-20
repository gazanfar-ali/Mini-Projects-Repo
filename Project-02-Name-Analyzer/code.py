#Name Analyzer (Covers: strings, string methods, len)
a = input("Enter your Name: ")
print("Length of your Name is:", len(a))

if a[0].lower() in ['a', 'e', 'i', 'o', 'u']:
    print('Your name starts with Vowel.')
else :
    print('Your name does not start with Vowel.')

print('Name is lower case: ',a.lower())

print('1st letter of your name:', a[0])

print("Your name reversed is:", a[::-1])
