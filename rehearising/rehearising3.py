# Children = 3
# Hometown = 'Lahti'

# TownInFinland = ['Lahti' , 'Helsinki', 'Lapperanta'] #could be only strings

# RandomInfo = ['Lahti' , 47 , True , 'Roland']#could be and boolean, float, int and string

# print(TownInFinland[0])
# print(TownInFinland[1])

# TownInFinland[2] = 'Turku'#changes 2 element to 'Turku'
# print(TownInFinland)

# TownInFinland.append('Rovanieni')#addes city 'Rovanieni' to the end of string
# print(TownInFinland)

# NumOfTown = len(TownInFinland)#counts length of the list
# print(TownInFinland[NumOfTown - 1])#prints last element of the list

# Municipalities = ['Asikkala' , 'Hollola' , 'Karvia' , 'Kempele']
# Towns = ['Lahti' , 'Helsinki' , 'Lapperanta' , 'Oulu' , 'Tampere']
# MunicipalitiesAndTowns = [Municipalities , Towns]

# print(MunicipalitiesAndTowns[1][-2])

# Towns = ['Lahti' , 'Helsinki' , 'Turku' , 'Vaasa' , 'Mikkeli' , 'Lapperanta' , 'Oulu' , 'Tampere']
# print(Towns[2:5])
# print(Towns[2:])
# print(Towns[:5])
# print(Towns[2:5:2])
# print(Towns[::-2])

# Towns.sort()
# print(Towns)

# # Dictionaries( it have {Key: Value})

# Teacher = {
# 'name': 'Mira',
# 'age': 47,
# 'city': 'Lahti'
# }
# Student = {
#     'name': 'Rolands',
#     'age': 19,
#     'city': 'Lahti'
# }

# print(Teacher['name'])
# print(Student['age'])

# Teacher['email'] = 'mira.vorne.@lab.fi'
# print(Teacher['email'])

# print(Teacher)
#How to sreate empty dictionary

# empty = {}

# empty['street'] = 'Mukkulantaku'

# print(empty)
#whipe exiting dictionary 
# empty = {}
# print(empty)

#Loops 

# for key in Teacher:
#     print(key)
#     print(Teacher[key])



                 #List in dictionary 
# Student = [
#     {'name': 'Mikko', 'age': 25, 'city': 'Tampere'},
#     {'name': 'Maija', 'age': 30, 'city': 'Espoo'},
#     {'name': 'Ville', 'age': 35, 'city': 'Helsinki'}
# ]
# print(Student)
# print(Student[0])


     #Dictionary in list
# Cities = {
#     'Finland': ['Tampere','Espoo','Helsinki'],
#     'Sweden': ['Stockholm','Goteborg','Malmo']
# }
# print(Cities['Finland'][0])



             #Dictionary in list in list
# Order = {
#     'starter': {1: 'Salad',2:'Soup'},
#     'main':{1:['Burger','Fries'],2:['Steak']},
#     'desert': {1:['Ice cream'],2:[]}
# }
# print(Order['main'][2][0])

# Courses = {
#     'Pyhton basic':{
#         'content':[
#             'conditions','loop','function','data types'
#             ],
#             'credit':4
#     },
#     'Databases':{
#         'content':[
#             'Setup','CRUD','Relations','Joins'
#         ],
#         'credit':5
#     }
# }

# for course, detail in Courses.items():
#     print('Content of', course)
#     for content in detail['content']:
#         print(content)

#First task
# import random 

# Towns = ['Lahti' , 'Helsinki' , 'Lapperanta' , 'Oulu' , 'Tampere']
# Town = random.choice(Towns)
# print(Town)
# if Town == 'Lahti':
#     print('The town of',Town, 'our hometown!')
# elif Town == 'Helsinki':
#     print('The town of',Town, 'our capital city!')
# elif Town == 'Oulu' or 'Lapperanta' or 'Tempere':
#     print('The town of',Town)

    #Second Task 

# #prints numbers from 1 to 9 in сторбик
# for i in range(1,10):
#     print(i)        


# #prints numbers from 1 to 9 in one line 
# for i in range(1,10):
#     print(i, end=' ')


# #prints 1, 4 , 7, every 3 numbers
# for i in range(1, 10, 3):
#     print(i)

# Total = 0
# for i in range(1, 101, end=' '):
#     Total += i
#     print(Total)

# Number = int(input('Insert number: '))
# Total = 0
# for i in range(1, Number):
#     if i % 2 == 0:
#         Total += i
        
# print(Total)

#Skipping the action
# for i in range(9):
#     if i == 3:
#         continue
#     print(i)

#While Loops

# while 1 < 10:
#     print('Do not try me XD')


# i = 0 
# while i < 10:
#     print(f'The iteration number is: i')

# ContinueLoop = True 
# while ContinueLoop == True:
#     if input('Do you want to continue?') != 'yes':
#         ContinueLoop = False

while True:
    if input('Do you want to continue another loop?') != 'yes':
        break
    else:
        continue