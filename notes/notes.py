from datetime import datetime
import random 
import json 
import requests
import pytz
import pandas as pd
import requests
import pandas as pd
import matplotlib.pyplot as plt

def user_date(user) -> None: 
    user['name'] = input('What is your first name?\n')

    user['surname'] = input('\nWhat is you last name?\n')
    
    user['age'] = int(input('\nWhat is your age: '))
    
    user['birthday'] = input('\nWhat is you birthday date?(in dd/mm/yyyy format)\n')

    return None

def new_account(users) -> dict:
    user = {}
    user_date(user)
    date_format(user)
    print(' ')
    username_maker(users, user)
    account, user = check_for_duplicate(users, user)
    if account == True:
        print('Welcome '+user['name']+'.\n')
    elif account == False:
        print('Welcome new user')
        age_verif(user)
        date_format(user)
        right_pick(user)
        password_generator(user)
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
        print ("Your account is saved to users.json")
    
    return user

def check_for_duplicate(users, user) -> dict:
    account = False
    for i in users:
        if i['username'] == user['username']:
            print('You already have account.')
            user = i
            account = True
    print(account)
    users.append(user)
    print(user)
    return account, user
    
    
    
    # return None

def account_checker(users) -> dict:
    user = {}    
    user['username'] = input('Username:\n')
    user['password'] = input('Password:\n')
    for i in users:
        if i['username'] == user['username'] and i['password'] == user['password']:
            print('Logged in.')
            return i
    print('Incorrect username or password.')
    return None

def username_maker(users, user) -> dict:
    user['username'] = user['name'][:3]+user['surname'][:4]+user['birthday'][6:11]+user['birthday'][3:5]+user['birthday'][0:2]
    print('Your username is:',user['username'],'\n')
    return users

def right_pick(user) -> None:
    if user['name'] == 'Rolands':
        user['rights'] = 'Admin'

    elif user['name'] == 'Mira':
        user['rights'] = 'super-user'

    else:
        user['rights'] = 'User'

    print('Possiable user rights:\n'
        '1 - Admin\n'
        '2 - Super-user\n'
        '3 - User')
    print('Your user right:', user['rights'])
    return None

def date_format(user) -> None:    
    while True:
        if user['birthday'][2] and user['birthday'][5] != '/':
            print("Incorrect format, enter date in dd/mm/yyyy format: ")
            user['birthday'] = input()
            continue
        elif int(user['birthday'][6:11]) < 1924 or int(user['birthday'][6:11]) > 2020:
            print("Incorrect year, enter date in dd/mm/yyyy format: ")
            user['birthday'] = input()
            continue
        elif int(user['birthday'][3:5]) > 12:
            print("Incorrect month, enter date in dd/mm/yyyy format: ")
            user['birthday'] = input()
            continue
        elif int(user['birthday'][0:2]) > 31:
            print("Incorrect day, enter date in dd/mm/yyyy format: ")
            user['birthday'] = input()
            continue
        break
    return None

def age_verif(user) -> None:
    if user['age'] < 18:
        print('Greetings '+user['name']+', you are too young to operate this program')
        choice = input('Do you want to play a game?\n')
        if choice == 'yes':
            game()
            print('Thanks for visiting. Welcome back soon.')
            exit()
        else:
            print('Thanks for visiting. Welcome back soon.')
            exit()
    return None

def thingspeak() -> str:
    cpu_data = []

    url = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20&timezone=Europe/Helsinki"
    response = requests.get(url)
    data = response.json()
    
    for entry in data["feeds"]:
        movement_value = entry["field1"]
        temp_value = entry["field2"]
        time_value = entry["created_at"]
    
        cpu = {
            'movement': movement_value,
            'temperature_celsius': float(temp_value),
            'temperature_fahrenheit': float((float(temp_value) * 9 / 5) + 32),
            'time': time_value
        }

        cpu['time'] = convert_time(cpu)
        cpu_data.append(cpu)

    with open("cpu.json", "w") as file:
        json.dump(cpu_data, file, indent=4)
        print ("Data is requested and saved to cpu.json")

    return cpu_data

def convert_time(cpu) -> None:
    date = cpu['time'][0: 10]
    clock = cpu['time'][11: 19]
    date = list(date)
    date[4] = '/'
    date[7] = '/'
    cpu['time'] = ''.join(date)
    cpu['time'] = cpu['time'] +  ' ' + clock
    return cpu['time']
       
def movement_detection(cpu) -> None:
    if cpu['movement'] == '1':
        print('Movement detected.\n')
    else:
        print('Movement was not detected.\n')
    return None

def temperature_of_CPU(cpu) -> None:
    print('Temperature of CPU is', cpu['temperature_celsius'],'°C')
    print('The given temperature ',cpu['temperature_celsius'],'°C is ',cpu['temperature_fahrenheit'],' °F\n')

    cpu['choice_of_temp'] = input('Would you like to see temperature in Celsius or Fahrenheit: ')
    if cpu['choice_of_temp'] == 'Celsius':
        if cpu['temperature_celsius'] < 70:
            print('The temperature of the CPU is ',cpu['temperature_celsius'],'°C, it is OK.')
        elif cpu['temperature_celsius'] >= 70:
            print('The temperature of the CPU is ',cpu['temperature_celsius'],'°C, it is TOO HOT!')
        else:
            print('The temperature of the CPU is ',cpu['temperature_celsius'],'°C, it is ON FIRE!!!') 
    else:
            if cpu['temperature_celsius'] < 70:
                print('The temperature of the CPU is ',cpu['temperature_fahrenheit'],'°F, it is OK.')
            elif cpu['temperature_celsius'] >= 70:
                print('The temperature of the CPU is ',cpu['temperature_fahrenheit'],'°F, it is TOO HOT')
            else:
                print('The temperature of the CPU is ',cpu['temperature_fahrenheit'],'°F, it is ON FIRE')

    return None 

def password_generator(user) -> None:
    print("\nLet's create password for your account!\n")

    while True:
        Capital = int(input('Enter number of capital letters: '))
        Small = int(input('Enter number of small letters: '))
        Number = int(input('Enter number of numbers: '))
        Special_char = int(input('Enter number of special characters: '))

        Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        Capitals = []
        while Capital > 0:
            Capitals += random.choice(Alphabet)
            Capital -= 1

        Small_Alphabet = 'abcdefghijklmnopqrstuvwxyz'
        LowerCase = []
        while Small > 0:
            LowerCase += random.choice(Small_Alphabet)
            Small -= 1

        AllNumbers = '123456789'
        Numbers = []
        while Number > 0:
            Numbers += random.choice(AllNumbers)
            Number -= 1

        AllSpecial_Characters = '!@#$%^&*()_+=-~`;:,<.>?|'
        Special_Characters = []
        while Special_char > 0:
            Special_Characters += random.choice(AllSpecial_Characters)
            Special_char -= 1

        user['password']  = Capitals+LowerCase+Numbers+Special_Characters
        random.shuffle(user['password'] )
        user['password']  = ''.join(user['password'] )
        print('Your password is "'+user['password']+'"\n')

        if input('Are you happy with your password?\n') != 'no':
            break
        else:
            continue

    return None 

def game() -> None:
    print('\nLet\'s play a number guessing game!')
    print('Rules of the game:\n'
          'I will choose number between 1 and 100 and you will have 8 tries to guess the number.\n'
          'I will give you hints while you try.')

    program = 0
    user = 0

    while True:
        i = 0
        number = random.randint(1 , 100)
        while i < 8:
            guess = input('Your guess: ')
            i += 1
            if guess == 'quit':
                break
            guess = int(guess)
            if guess == number:
                print('Good job, you got it from the',i,'try\n')
                user += 1
                break
            elif i == 8:
                print ('You lost, loser.\n')
                program  += 1
            elif guess > number:
                print('Try lower.\n')
                continue
            elif guess < number:
                print('Try higher.\n')
                continue
        print('Score\n'
            'Program:',program,'\n'
            'User:', user,'\n')
            
            
        if input('Do you wanna play another round?\n') != 'yes':
            print('hahaha, scared of losing?')
            break
        else:
            continue
    return None

def information_table(cpu_data) -> None:
    df = pd.DataFrame(cpu_data)
    print(df)
    return None
    
def information_chart(cpu_data) -> None:
    df = pd.DataFrame(cpu_data)
    plt.figure(figsize=(10, 5))
    plt.plot(df['movement'], label='Movement')
    plt.plot(df['temperature_celsius'], label='Temperature')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title('Temperature and Movement Over Time')
    plt.legend()
    plt.show()
    return None

def information_bar_chart(cpu_data) -> None:
    
    df = pd.DataFrame(cpu_data)
    plt.figure(figsize=(10, 5))
    colors = []
    for temp in df['temperature_celsius']:
        if temp < 47:
            colors.append('blue')
        else:
            colors.append('red')
    plt.bar(df.index, df['temperature_celsius'], width=0.4, label='Temperature', color=colors)
    plt.xlabel('Time')
    plt.ylabel('Temperature (Celsius)')
    plt.title('Temperature Over Time (Sorted in Descending Order)')
    plt.legend()
    plt.show()

    plt.scatter(df.index, df['movement'], color='grey')
    plt.xlabel('Time')
    plt.ylabel('Movement')
    plt.title('Movement')
    plt.legend()
    plt.show()
    # df = pd.DataFrame(cpu_data)
    # df = df.sort_values(by='temperature_celsius', ascending=False).reset_index(drop=True)    
    # # Set up the figure with two subplots, sharing the x-axis
    # fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    
    # colors = []
    # for temp in df['temperature_celsius']:
    #     if temp < 47:
    #         colors.append('blue')
    #     else:
    #         colors.append('red')

    # ax1.bar(df.index, df['temperature_celsius'], color=colors)
    # ax1.set_title('Temperature Over Time (Descending)')
    # ax1.set_ylabel('Temperature')
    
    # # Second subplot for Movement (with dots)
    # ax2.scatter(df.index, df['movement'], color='green')
    # ax2.set_title('Movement Over Time')
    # ax2.set_xlabel('Time')
    # ax2.set_ylabel('Movement')
    
    # # Adjust layout to avoid overlap
    # plt.tight_layout()
    
    # # Show the chart
    # plt.show()

def account_information(user) -> None:
    print('\n***Account details***')
    print('Name:', user['name'])
    print('Surname:', user['surname'])
    print('Birthday:',user['birthday'])
    print('Age:', user['age'])
    print('Username:', user['username'])
    print('Password:', user['password'])
    return None

def main() -> None:
    users  = []

    with open("users.json", "r") as file:
        users = json.load(file)

    print('Hello user, welcome to the Motion Detector! Let’s start.\n')

    print("1. Sign in")
    print("2. Log in")
    
    if input("Your choice: ") != '1':
        user = new_account(users)
    else:
        user = account_checker(users)
        print('Welcome '+user['name']+'.\n')

    print(user)
    while True:
        print("\nMenu")
        print("1. Make a request for data of the CPU.")
        print("2. Information about CPU.")
        print("3. Number guessing game.")
        print('4. Acount information.')
        print("5. Exit")

        choice = input('Your choice: ')
        if choice == '1':
            cpu_data = thingspeak()
        elif choice == '2':
            while True:
                print('\nMenu:')
                print('1. Show information in the table.')
                print('2. Show information in the chart.')
                print('3. Show onformation in the bar chart.')
                print('4. Exit.')
                choice2 = input('Your choice: ')
                if choice2 == '1':
                    information_table(cpu_data)
                    
                elif choice2 == '2':
                    information_chart(cpu_data)
                    
                elif choice2 == '3':
                    information_bar_chart(cpu_data)
                    
                elif choice2 == '4':
                    break
                
                else:
                    print('Please enters 1, 2 or 3.')
                    continue

        elif choice == '3':
            game()
        elif choice == '4':
            account_information(user)
        elif choice == '5':
            print('Program ending...')
            break
        else:
            print('Please enters 1, 2, 3 or 4.')
            continue
    return None

main()
