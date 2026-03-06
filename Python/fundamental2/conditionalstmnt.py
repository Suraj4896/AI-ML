age = int(input('enter your age: '))

if age < 13:
    print('you are child')
elif age >= 13 and age < 18:
    print('you are teenager')
else:
    print("you are adult")



#nesting
username = input('enter username: ')
password = input('enter password: ')

if username == 'admin' and password == 'pass':
    print('success')
else:
    if username != 'admin':
        print('username is wrong')
    else:
        print('password is wrong')