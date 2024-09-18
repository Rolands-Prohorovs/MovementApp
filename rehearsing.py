#Tis is my first program 
#print("He said: \"Hello word!\" \n and kept on coding") 
#quote in the print command(everything that goes after \ is regular text)
#\n text will start in the new line

#print('Hello' + 'user!')

#input('What is your name?')

# print('Welcome ' + input('What is your name?') + '!')

# print('Hello'[0])

# print('Hello'[0:2])

# print('123' + '456')

# FirstName = input('What is your firstname:')
# LastName = input('What is your lastname:') 
# print('Hello ' + FirstName + ' ' + LastName + '!')#
#print('Hello', FirstName, LastName,'!')#in Phyton I do not need + I can use coma(,)

import math


Sentence = 'Finding a substring'

# print(Sentence)

# print(Sentence[0])

# print(Sentence[0:2])

# print(Sentence[1:4])

# print(Sentence[0:9])

# print(Sentence[3:14])

# print(Sentence[0:19])

# print(Sentence[0:222])

print(Sentence[-2])
print(Sentence[:9])
print(Sentence[0:9])
print(Sentence[-9:-1])
print(Sentence[2:9:3])
print(Sentence[::3])
print(Sentence[::-1])

#Integer(whole number)
# print(123 + 456)#output:579
# print(123_456_789)#output: 123456789

# #Float
# print(3.14)

# #Boolean
# print(True)
# print(False)

# Calclen = len('Calculate the number of characters')#calculates lenght of sentence, with space and start counting with 1
# print(Calclen)
# print(type(Calclen))

# Num1 = float(10)#change vereable from integer ro float
# print(type(Num1))

# Num2 = int('20')
# Num3 = 30 + Num2 
# print(Num3)

# print(5 * 3 - 4 / 2 + 2)

# print(5 * 3 - 4 / (2 + 2))


# print(8 / 3)#output: 2.666666(float)

# print(int(8 / 3))#output: 2(integer)

# print(round(8 / 3))#output: 3

# print(round(8 / 3, 2))#output: 2,67


#print(7 / 2)#output:3.5(float)

#print(7%2)#output: 1(just a remeinder)


#Using % formating 

# Name = 'Rolands'
# Age = 19
# Height = 195.5

# FormattedString = 'My name is %s, I am %d years old and I am %f cm tall.' %(Name, Age, Height)
# print(FormattedString)

# %s for string 
# %d for integer
# %f for float


#Using format() method

# Name = 'Rolands'
# Age = 19

# FormattedString = 'My name is {0} and I am {1} years old.' .format(Name, Age)
# print(FormattedString)

#{} = placehold for variable


# Name = 'Rolands'
# Age = 19
# Number = 8/3

# FormattedString = 'My name is {0} and I am {1} years old. The number is {2:.2f}'.format(Name, Age, Number)
# print(FormattedString)

# EasyCalc = 0
# EasyCalc = EasyCalc + 1 # 0 + 1
# EasyCalc += 1 # 0 + 1
# EasyCalc -= 1 # 0 - 1
# EasyCalc *= 1 # 0 * 1
# EasyCalc /= 1 # 0 / 1

# print(f'This is the result of easy calculation: {EasyCalc}. Good job!')


# Height = input("What is height of cylinder")
# Height = int(Height)
# Radius = input("What ir radius of cylinder")
# Radius = int(Radius)
# Pi = math.pi

# EasyCalc = 1
# EasyCalc *= Pi
# EasyCalc *= Radius ** 2
# EasyCalc *= Height

# print(f'The volume of your cylinder is:{round(EasyCalc, 3)}')
