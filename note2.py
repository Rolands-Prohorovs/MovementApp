users = []
while True:
    if input('Wanna continue? (yes/no) ') == 'yes':
        user = {}  
        user['name'] = input('Insert name: ')
        
        for i in users:
            if i['username'] == user['username']:
                print("Name already exists. Please enter a different name.")
        else:
            users.append(user)  
    else:
        break

print(users)
