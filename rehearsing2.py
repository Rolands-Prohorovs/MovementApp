# print('Welcome to the MovementApp!')
# Temperature = int((input('What is the temperature of your IoT CPU?')))
# if Temperature > 80:         
#     print('Too hot!')
# else:
#     print('Cool!')

# Number = int(input('Write a number:'))
# Reminder = Number % 2
# if Reminder == 0:
#     print('Even')
# else:
#     print('Odd')

# Name1 = input('Write your name: ')
# Name2 = input('Write name of your friend: ')
# NameLen1 = len(Name1)
# NameLen2 = len(Name2)
# if NameLen1 > NameLen2:
#     print('Name',Name1,'longer then', Name2)
# elif NameLen1 < NameLen2:
#     print('Name',Name1,'shorter then', Name2)
# else:
#     print('Names are equal')

# x = 4
# print(x < 5 and x < 10)
# print(x < 5 or x < 4)
# print(not(x < 5 and x < 10))

# Town = 'Lahti'
# Street = 'Mukkulantaku'
# Building = 19

# if (Town == 'Lahti' and Street == 'Mukkulantaku' and Building == 19):
#     print('You are at LAB!')
# elif (Town == 'Lahti' and (Street != 'Mukkulantaku' or Building <= 19)):
#     print('You are in the correct town, but you are not there yet')
# elif (Town == 'Lahti' and (Street != 'Mukkulantaku' or Building >= 19)):
#     print('You are in the correct town, but you went too far')
# elif not(Town == 'Lahti' and Street == 'Mukkulantaku' and Building == 19):
#     print('You are completely lost...')

#                                   3 WORDS IN  ALPHABETICAL ORDER 
# Word1 = input('Write first word: ')
# Word2 = input('Write second word: ')
# Word3 = input('Write third word: ')

# Words = [Word1 , Word2, Word3]

# Alph = sorted(Words)

# print(Alph)

#                                RANDOM NUMBER IN ORDER
# import random 
# print(random.random())
# RandomInteger = random.randint(1,10)
# print(RandomInteger)

# a = random.randint(1,1000)
# b = random.randint(1,1000)
# c = random.randint(1,1000)

# Numbers = [a , b , c]
# Numbers = sorted(Numbers)
# print(Numbers)


#                             RANDOM LETTER 
# import string
# Name = input('Write your name:')
# Letter = random.choice(string.ascii_letters)
# if Letter in Name:
#     print('The letter ',Letter,'was found in your name',Name,'.')
# else:
#     print('The letter ',Letter,'was not found in your name',Name,'.')



#                                SIMPLE MENU
# print('Select from the list:\n 1. Login\n 2. Go to settings\n 3. Logout')
# Choice = input('Chooce your option: ')
# if Choice == 'Login':
#     print('Program started')
# elif Choice == 'Go to settings':
#     print('Settings')
# elif Choice == 'Logout':
#     print('Logged out')
# else:
#     print('User input not recognized.')


#                                      ROCK PAPER SCISSORS
# import random 
# RandomInteger = random.randint(1,3)
# if RandomInteger == 1:
#     ProgramChoice = 'rock'
# elif RandomInteger == 2:
#     ProgramChoice = 'scissors'
# elif RandomInteger == 3:
#     ProgramChoice = 'paper'
# print("Let's play a game!")
# print('Choose rock, paper or scissors:')
# UserChoice = input('')
# if ProgramChoice == UserChoice:
#     print('Draw')
# elif ProgramChoice == 'rock' and UserChoice == 'scissors':
#     print('Rock beats scissors, you lost, Loser!')
# elif ProgramChoice == 'rock' and UserChoice == 'paper':
#     print('Paper beats rock, you won, lucky you!')

# elif ProgramChoice == 'scissors' and UserChoice == 'rock':
#     print('Rock beats Scissors, you won, lucky you!')
# elif ProgramChoice == 'scissors' and UserChoice == 'paper':
#     print('Scissors beats Paper, you lost, Loser!')

# elif ProgramChoice == 'paper' and UserChoice == 'rock':
#     print('Paper beats Rock, you lost, Loser!')
# elif ProgramChoice == 'paper' and UserChoice == 'scissors':
#     print('Scissors beats Paper, you won, lucky you!')
# else:
#     print('Watch you grammar fool:(')
#                           Date format check
import random

Movement = random.choice([True, False])

print(Movement)
