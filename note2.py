users = []
user = {}

while True:
    if input('Wanna continue?') == 'yes':
        user['name'] = input('Insert name: ')
        users.append(user.copy())  # Using copy() to avoid overwriting previous entries
    else:
        break

print(users)
