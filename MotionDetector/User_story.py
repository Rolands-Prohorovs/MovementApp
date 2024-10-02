from datetime import datetime
import sys
import random 

def exit_function():
     print('Thanks for visiting. Welcome back soon.')
     sys.exit()

print('Hello user, welcome to the Motion Detector! Let’s start.\n')

User = {}

FirstName = input('What is your first name?')
User['name'] = FirstName
if FirstName == 'quit':
     exit_function()

LastName = input('What is you last name?')
User['surname'] = LastName
if LastName == 'quit':
     exit_function()

Date = input('What is you birthday date?(in dd/mm/yyyy format)')
User['birthday'] = Date
if Date == 'quit':
     exit_function()

print('')
print("Hello", FirstName, LastName,", welcome to the Motion Detector! Let's start.")

print('Your username is:',FirstName[:3]+LastName[:4]+Date[6:11]+Date[3:5]+Date[0:2])
Username = FirstName[:3]+LastName[:4]+Date[6:11]+Date[3:5]+Date[0:2]
User['username'] = Username
print('')
# Movement = input('Has there been movement? Yes/No')

Movement = random.choice([True, False])
if Movement == True:
     print('Movement detected: Yes')
else:
     print('Movement detected: No')
if Movement == 'quit':
     exit_function()
print('')

# Celsius = input('What is temperature of CPU? in °C')

Celsius = random.randint(1,100)
print('Temperature of CPU is', Celsius)
Celsius = int(Celsius)
Fahrenheit = (Celsius  * 9/5) + 32
print('The given temperature ',Celsius,' is ',Fahrenheit,' F')
print('')

try:
    birthday = datetime.strptime(Date, '%d/%m/%Y')
except ValueError:
    print("Incorrect format, enter date in dd/mm/yyyy format:")
    Date = input()
if Date == 'quit':
     print('Thanks for visiting. Welcome back soon.')
     sys.exit()

print('')
if User['name'] == 'Rolands':
    print('Welcome '+User['name']+', you have admin rights.')
    User['rights'] = 'Admin'
elif User['name'] == 'Mira':
    print('Welcome '+User['name']+', you have super-user rights')
    User['rights'] = 'super-user'
else:
    print('Welcome '+User['name']+', you have viewer rights.')
    User['rights'] = 'User'

print('')

Age = int(input('What is your age: '))
User['age'] = Age
if Age == 'quit':
    exit_function()
if Age < 18:
    print('Greetings '+User['name']+', you are too young to operate this program')
    print('Thanks for visiting. Welcome back soon.')
    exit()

print('')
Temp = input('Would you like to see temperature in Celsius or Fahrenheit: ')
if Temp == 'quit':
     exit_function()
if Temp == 'Celsius':
    if Celsius < 70:
        print('The temperature of the CPU is ',Celsius,', it is OK.')
    elif Celsius >= 70:
        print('The temperature of the CPU is ',Celsius,', it is TOO HOT!')
    else:
        print('The temperature of the CPU is ',Celsius,', it is ON FIRE!!!') 
else:
        if Celsius < 70:
             print('The temperature of the CPU is ',Fahrenheit,', it is OK.')
        elif Celsius >= 70:
             print('The temperature of the CPU is ',Fahrenheit,', it is TOO HOT')
        else:
             print('The temperature of the CPU is ',Fahrenheit,', it is ON FIRE') 

print('')

if Movement == True:
     print('Movement detected')
elif Movement == False:
     print('Movement not detected')
else:
     print('You did not answer if there was movement ')

print('')

print("Let's create password for your account!")

print('')

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

    Password = Capitals+LowerCase+Numbers+Special_Characters
    random.shuffle(Password)
    Password = ''.join(Password)
    print(Password)

    if input('Are you happy with your password?') != 'no':
        break
    else:
        continue
    
print('')

print('Possiable user rights:\n'
      '1 - Admin\n'
      '2 - Super-user\n'
      '3 - User')
print('Your user right:', User['rights'])

