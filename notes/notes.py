from datetime import datetime
import random 
import json

def user_date(users, user): 
    user['name'] = input('What is your first name?\n')

    if user['name'] == 'Rolands':
        user['rights'] = 'Admin'

    elif user['name'] == 'Mira':
        user['rights'] = 'super-user'

    else:
        user['rights'] = 'User'
        
    user['surname'] = input('\nWhat is you last name?\n')
    
    user['birthday'] = input('\nWhat is you birthday date?(in dd/mm/yyyy format)\n')
    
    while True:
            try:
                birthday = datetime.strptime(user['birthday'], '%d/%m/%Y')
                break
            except ValueError:
                print("Incorrect format, enter date in dd/mm/yyyy format: ")
                user['birthday'] = input()
                continue

    user['age'] = int(input('\nWhat is your age: '))

    
    if user['age'] < 18:
        print('Greetings '+user['name']+', you are too young to operate this program')
        print('Thanks for visiting. Welcome back soon.')
        exit()


    print('\nWelcome '+user['name']+'.\n')

    user['username'] = user['name'][:3]+user['surname'][:4]+user['birthday'][6:11]+user['birthday'][3:5]+user['birthday'][0:2]
    print(user['username'])
    
    for i in users:
            if "username" in i and i["username"] == user["username"]:
                print('You already have account.')
                if input('Do you wanna make another or continue with this?(continue/another)\n') != 'continue':
                    return user_date(users, user)
                else:
                    print('Continue with existing account.')
                    return
    
    print('Your username is:',user['username'],'\n')
    users.append(user)
    return
    # check_account(users, user)

    
# def check_account(users, user):
    

def movement_detection():
    print('\nWas movement detected?')
    movement = random.choice([True, False])
    if movement == True:
        print('Movement detected\n')
    elif movement == False:
        print('Movement not detected\n')



def temperature_of_CPU():
    cpu = {}
    print('What is the temperature of the CPU?')
    cpu['celsius_temp'] = random.randint(1,100)

    print('Temperature of CPU is', cpu['celsius_temp'],'°C')
    cpu['fahrenheit_temp'] = (cpu['celsius_temp'] * 9/5) + 32
    print('The given temperature ',cpu['celsius_temp'],'°C is ',cpu['fahrenheit_temp'],' °F\n')

    cpu['choice_of_temp'] = input('Would you like to see temperature in Celsius or Fahrenheit: ')
    if cpu['choice_of_temp'] == 'Celsius':
        if cpu['celsius_temp'] < 70:
            print('The temperature of the CPU is ',cpu['celsius_temp'],'°C, it is OK.')
        elif cpu['celsius_temp'] >= 70:
            print('The temperature of the CPU is ',cpu['celsius_temp'],'°C, it is TOO HOT!')
        else:
            print('The temperature of the CPU is ',cpu['celsius_temp'],'°C, it is ON FIRE!!!') 
    else:
            if cpu['celsius_temp'] < 70:
                print('The temperature of the CPU is ',cpu['fahrenheit_temp'],'°F, it is OK.')
            elif cpu['celsius_temp'] >= 70:
                print('The temperature of the CPU is ',cpu['fahrenheit_temp'],'°F, it is TOO HOT')
            else:
                cpu['celsius_temp']('The temperature of the CPU is ',cpu['fahrenheit_temp'],'°F, it is ON FIRE') 



def password_generator(user):
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


def game():
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

def main():
    users  = []
    user = {}
    print('Hello user, welcome to the Motion Detector! Let’s start.\n')

    print("First let's create an acount for you.")

    
    with open("users.json", "r") as file:
        users = json.load(file)

    user_date(users, user)

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)
        print ("Updated data written to users.json")

    print('\nPossiable user rights:\n'
        '1 - Admin\n'
        '2 - Super-user\n'
        '3 - User')
    print('Your user right:', user['rights'])

    password_generator(user)
    movement_detection()
    temperature_of_CPU()

    if input('Do you wanna try to win me in the number guessing game?\n') != 'yes':
        print('Scared of losing?')
    else:
        game()

    print('Program ending.')

main()




