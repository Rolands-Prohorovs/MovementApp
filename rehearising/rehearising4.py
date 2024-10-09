#  functions

# def greeting(name):
#     return f'Hello', (name)

# message = greeting('Student')
# print(message)
# person = input('What is your name?')
# age = int(input('What is your age?'))

# def greeting_airport(person, age):
#     print(f'How do you do {person}')
#     if age >= 18:
#         print('Welcome on your flight')
#     else:
#         print('I am sorry, you are not allowed to fly on your own.')
#         print(f'You need to wait for {18 - age} years')

# greeting_airport(person, age)



# def prime_number(number):
#     Prime_Numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#     while True:
#         for i in Prime_Numbers:
#             if number == i:
#                 print(f'{number} is prime number.')
#                 break
#             else:
#                 continue
#         else:
#             print(f'{number} is regular number.')
#             break
#         choice = input('Do you want to try other number?')
#         if choice  != 'yes':
#             print(f'Goodbye!')
#             break
#         else:
#             number = int(input('Choice any number: '))
#             prime_number(number)
#             continue
# number = int(input('Input any number: '))
# prime_number(number)

# def prime_number(number):
#     is_prime = True
#     for i in range(2 , number):
#         if number % 1 == 0:
#             is_prime = False
#     if is_prime:
#         print(f'{number} is a ')


# def capital_letter(first_name, last_name):
#     if first_name.isupper() == True:
#         name = True
#     else:
#         name = False
#     if last_name.isupper() == True:
#         surname = True
#     else:
#         surname = False

#     if name == True:
#         print('Your name starts with capital letter.')
#     elif surname == True:
#         print('Your surname starts with capital letter.')
#     elif name and surname == True:
#         print('Your name and surname starts with capital letter.')
#     else:
#         print('Your name and surname do not start with capital letters.')

# first_name = input('Write your first name: ')
# last_name = input('Write your  last name: ')
# capital_letter(first_name, last_name)

