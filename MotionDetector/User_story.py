from datetime import datetime
import random 
import json 
import requests
import pytz

def user_date(user) -> None: 
    
    user['name'] = input('What is your first name?\n')

    user['surname'] = input('\nWhat is you last name?\n')
    
    user['birthday'] = input('\nWhat is you birthday date?(in dd/mm/yyyy format)\n')

    user['age'] = int(input('\nWhat is your age: '))

    return None

def new_account(users) -> dict:
    user = {}
    user_date(user)
    username_maker(users, user)
    check_for_duplicate(users, user)
    if user == None:
        account_checker(users)
    else:
        print('Welcome '+user['name']+'.\n')
        age_verif(user)
        date_format(user)
        
        right_pick(user)
        password_generator(user)
        return user

def check_for_duplicate(users, user) -> dict:
    for i in users:
        if i['username'] == user['username']:
            print('You already have account.')
            user = i
            return user
    return None

def account_checker(users) -> dict:
    user = {}
    user['username'] = input('Username:\n')
    user['password'] = input('Password:\n')
    for i in users:
        if i['username'] == user['username'] and i['password'] == user['password']:
            print('Logged in.')
            user = i
            return user
        else:
            continue
    print('Incorrect.')
    print('\nLets make you new one!\n')
    user = {}
    new_account(user)
           
def username_maker(users, user) -> dict:
    user['username'] = user['name'][:3]+user['surname'][:4]+user['birthday'][6:11]+user['birthday'][3:5]+user['birthday'][0:2]
    print('Your username is:',user['username'],'\n')
    users.append(user)
    return users

def right_pick(user) -> None:
    if user['name'] == 'Rolands':
        user['rights'] = 'Admin'

    elif user['name'] == 'Mira':
        user['rights'] = 'super-user'

    else:
        user['rights'] = 'User'

    print('\nPossiable user rights:\n'
        '1 - Admin\n'
        '2 - Super-user\n'
        '3 - User')
    print('Your user right:', user['rights'])
    return None

def date_format(user) -> None:
    while True:
            try:
                birthday = datetime.strptime(user['birthday'], '%d/%m/%Y')
                break
            except ValueError:
                print("Incorrect format, enter date in dd/mm/yyyy format: ")
                user['birthday'] = input()
                continue
    return None

def age_verif(user) -> None:
    if user['age'] < 18:
        print('Greetings '+user['name']+', you are too young to operate this program')
        print('Thanks for visiting. Welcome back soon.')
        exit()
    return None

def thingspeak() -> str:
    cpu = {}
    url = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=5&timezone=Europe/Helsinki"
    response = requests.get(url)
    data = response.json()

    for entry in data["feeds"]:
        movement_value = entry["field1"]
        temp_value = entry["field2"]
        time_value = entry["created_at"]

    cpu['movement'] = movement_value
    cpu['temperature_celsius'] = float(temp_value)
    cpu['temperature_fahrenheit'] = float((float(temp_value) * 9 / 5) + 32) 
    cpu['time'] = time_value
    return cpu

def convert_to_finnish_time(cpu) -> None:
    utc_time_str = cpu['time']
    finnish_tz = pytz.timezone('Europe/Helsinki')
    
    utc_time = datetime.strptime(utc_time_str, "%Y-%m-%dT%H:%M:%SZ")
   
    utc_time = utc_time.replace(tzinfo=pytz.utc)
   
    finnish_time = utc_time.astimezone(finnish_tz)
    
    cpu['time'] = finnish_time.strftime("%d.%m.%Y, %H:%M")
    print('At',cpu['time'])
    return None
       
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

def main() -> None:
    
    users  = []

    with open("users.json", "r") as file:
        users = json.load(file)

    print('Hello user, welcome to the Motion Detector! Let’s start.\n')

    if input("Do you have an account?\n") != 'yes':
        print('\nThen lets make you one!\n')
        user = new_account(users)
    else:
        user = account_checker(users)
        print('Welcome '+user['name']+'.\n')


    cpu = thingspeak()
    # convert_to_finnish_time(cpu)
    movement_detection(cpu)
    temperature_of_CPU(cpu)

    with open("cpu.json", "w") as file:
        json.dump(cpu, file, indent=4)
        print ("Updated data written to cpu.json")

    if input('Do you wanna try to win me in the number guessing game?\n') != 'yes':
        print('Scared of losing?')
    else:
        game()

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)
        print ("Updated data written to users.json")

    print('Program ending.')
    return None

main()


