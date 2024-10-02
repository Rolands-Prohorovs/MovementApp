import random 
def game():
    print('Let\'s play a number guessing game!')
    print('Rules of the game: I will choose number between 1 and 100 and you will have 8 tries to guess the number. I will give you hints while you try.')

    program = 0
    user = 0

    while True:
        i = 0
        number = random.randint(1 , 100)
        print(number)
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

game()