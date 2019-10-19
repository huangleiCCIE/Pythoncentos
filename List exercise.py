#3-1 #3-2
# names=['xiao ming', 'xiao zhang', 'xiao wu']
# message='Hello'
# print(names[0].title() + ' ' + message)
# print(names[1].title() + ' ' + message)
# print(names[2].title() + ' '+ message)

#3-3
# commute = ['bike', 'bus', 'car' ]
# print('I would like to own a ' + commute[0])
# print('I would like to own a ' + commute[-1])
# print('I would like to own a ' + commute[-2])

#3-4
# name_list = ['xiaoming', 'xiaowang', 'xiaozhang']
# print(name_list)
# name_list.remove('xiaoming')
# print(name_list)
# name_list.insert(0,'xiaohuang')
# print(name_list)
# name_list.insert(0,'xiaoliu')
# name_list.insert(2,'xiaoxu')
# name_list.append('xiaoguo')
# print(name_list)
# xiaoguo=name_list.pop()
# print(xiaoguo+' 抱歉')
# xiaozhang=name_list.pop()
# print(xiaozhang+' 抱歉')
# xiaowang=name_list.pop()
# print(xiaowang+' 抱歉')
# xiaoxu=name_list.pop()
# print(xiaoxu+' 抱歉')
# print(len(name_list))

#3-8
# place_name = ['beijing', 'shanghai', 'hangzhou', 'shenzhen', 'chengdu']
# print(sorted(place_name))
# print(place_name)
# print(sorted(place_name,reverse=True))
# print(place_name)
# place_name.reverse()
# print(place_name)
# place_name.reverse()
# print(place_name)
# place_name.sort()
# print(place_name)
# place_name.sort(reverse=True)
# print(place_name)

#4-1
# pizza = ['guodong', 'niupai', 'shala']
# for new_pizza in pizza:
#     print(new_pizza)
#     print('I like pepperoni pizza')
# print('I really love pizza!')

#4-2
# animal = ['dog', 'cat', 'pig']
# for new_animal in animal:
#     print(new_animal)
#     print('A ' + new_animal.title() +  ' would make a great pet')
# print('Any of these animals would make a great pet')

#4-3
# for value in range(1,21):
#     print(value)

#4-4 4-5
# value_list = []
# for value in range(1,101):
#     value_list.append(value)
# print(value_list)
# print(min(value_list))
# print(max(value_list))
# print(sum(value_list))

#4-6
# value_list = list(range(1,20,2))
# for value in value_list:
#     print(value)

# # 4-7
# value_list = list(range(3,31,3))
# for value in value_list:
#     print(value)

#4-8
# list = []
# for value in range(1,11):
#     value = value **2
#     list.append(value)
# print(list)

# #4-9
# squares = [value ** 3 for value in range(1,10) ]
# print(squares)

#4-10
# squares = [value ** 3 for value in range(1,10)]
# print(squares)
# print('The first three items in the list are')
# print(squares[:3])
# print('Three items from the middle of the list are')
# print(squares[3:6])
# print('The last three items in the list are')
# print(squares[6:])

#4-11
# pizza = ['guodong', 'niupai', 'shala']
# friend_pizzas = pizza[:]
# pizza.append('shucai')
# friend_pizzas.append('shuiguo')
# for new_pizza in pizza:
#     print('My favorite pizzas are ' + new_pizza)
# for friend_pizzas in friend_pizzas:
#     print("My friend's favorite pizzas are " + friend_pizzas)

#4-13
# food = ('1', '2', '3', '4', '5')
# for new_food in food:
#     print(new_food)
# food = ('1', '4', '5', '7', '9')
# for new_food in food:
#     print(new_food)

# requested_toppings = ['mushrooms', 'onions', 'pineapple'] #检查特定值是否包含在列表中
# # print('mushrooms' in requested_toppings)
# # print('pepperoni' in requested_toppings)

# banned_users = ['andrew', 'carolina', 'david']  #检查特定值是否不包含在列表中
# user = 'marie'
# if user not in banned_users:
#     print(user.title()+', you can post a reponse if you wish.')

# 5-1
# car = 'subaru'
# print(car!='baba')
# car = 'sudu'
# print(car !='sudu')

#5-2
# car ='bwm'
# food ='BWM'
# print(car == food)

# a=1
# b=2
# print(a == b)
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >=b)
# print(a != b)

# a = 1
# b = 2
# print(a<1 or b>1)
# print(a<1 and b>1)

# a=[1,2,3,4]
# print(2 in a)
#
# a=[1,4,5,6]
# print(4 not in a)

# #5-3 5-4 5-5
# alien_color = ['green', 'yellow', 'red']
# if 'green' in alien_color:
#     print('Players get 5 points')
# elif 'yellow' in alien_color:
#     print('Players get 10 points')
# else:
#     print('Players get 15 points')

#5-6
# age = 88
# if age < 2:
#     print('baby')
# elif age < 4:
#     print('toddler')
# elif age < 13:
#     print('children')
# elif age < 20:
#     print('Teenagers')
# elif age < 65:
#     print('Adult')
# else:
#     print('Aged')

#5-7
# favorite_fruits = ['apple', 'banana', 'xigua']
# if 'apple' in favorite_fruits:
#     print('I Like apple')
# if 'yingtao' in favorite_fruits:
#     print('I Like yingtao')
# if 'banana' in favorite_fruits:
#     print('I Like banana')
# if 'xigua' in favorite_fruits:
#     print('I Like xigua')
# if 'caomei' in favorite_fruits:
#     print('I Like caomei')

# #5-8 5-9
# users = ['admin', 'hl', 'xz', 'xw', 'xl']
# if users:
#     for user in users:
#         if user == 'admin':
#             print('Hello admin,would you like to see a status report?')
#         else:
#             print('Hello Eric,thank you for logging in again')
# else:
#     print('We need to find some users!')

#5-10
# current_users = ['admin', 'hl', 'xz', 'xw', 'xl']
# # new_users = ['Admin', 'HL', 'df', 'fg', 'sw']
# # for new_user in new_users:
# #     if new_user.lower() in current_users:
# #         print('输入别的用户名')
# #     else:
# #         print('用户名未被使用')

#5-11
# numbers = [1,2,3,4,5,6,7,8,9]
# for number in numbers:
#     if number == 1:
#         print(str(number)+'st')
#     elif number == 2:
#         print(str(number)+'nd')
#     elif number == 3:
#         print(str(number)+ 'rd')
#     else:
#         print(str(number)+ 'th')

# dic = {'first_name': 'H',
#        'last_name': 'L',
#        'city' : 'chifeng'
#        }
# print(dic)

# dic = {}
# dic['hl']=5
# dic['zx']=6
# dic['bx']=7
# print(dic)

# dic ={'a':1,
# #       'b':2,
# #       'c':3,
# #       'd':4,
# #       'e':5
# #       }
# # print('a '+str(dic['a'])+'\n'+
# #       'b '+str(dic['b'])+'\n'+
# #       'c '+str(dic['c'])+'\n'+
# #       'd '+str(dic['d'])+'\n'+
# #       'e '+str(dic['e'])+'\n'
# #        )

# hls = {
#     'CH':'1',
#     'RB':'2',
#     'MG':'3'
#     }
# for key in hls.values():
#     print(key)
#     print('The Nile runs through Egypt')

# hls = {
#     'CH':'1',
#     'RB':'2',
#     'MG':'3'
#     }
# for key,value in hls.items():
#     print(key,value)
#     print('The Nile runs through Egypt')

# hls = {
#     'CH':'1',
#     'RB':'2',
#     'MG':'3'
#     }
# for key in hls.keys():
#     print(key)
#     print('The Nile runs through Egypt')

# Dics = {
#    'HL':'15',
#    'XM':'16',
#    'XW':'17'
#     }
# list = ['HL','XM']
# for Dic in Dics.keys():
#     if Dic in list:
#         print('Thack you '+ Dic)
#     else:
#         print('请尽快参加 '+ Dic)

# People1 = {
#     'first_name': 'xiaoming',
#     'age' : '22',
#     'city' : 'neimeng'
#     }
# People2= {
#     'first_name': 'xiaozhang',
#     'age' : '22',
#     'city' : 'neimeng'
#     }
# People3 = {
#     'first_name': 'xiaolei',
#     'age' : '22',
#     'city' : 'neimeng'
#     }
# Peoples = [People1,People2,People3]
# for People in Peoples:
#     print(People)

# cat = {
#     'type' : 'cat',
#     'zhuren' : 'xiaoming'
#     }
# dog = {
#     'type' : 'dog',
#     'zhuren' : 'xiaozhang'
#     }
# pets =[cat,dog]
# for pet in pets:
#     print(pet)

# favorite_places = {
#     'xiaoming' : {
#         'type' : 'dog'
#         },
#     'xiaozhang' : {
#         'type' : 'cate'
#         }
#     }
# for name,any in favorite_places.items():
#     print('Name:' + name)
#     type = any['type']
#     print('dongwu:' + type.title())

# number = {
#     '小明':{
#         'shuzi':5
#         },
#     '小张':{
#         'shuzi':6
#         }
#     }
# for name,numbers in number.items():
#     print('Name:'+ name)
#     print('Number:' + str(numbers['shuzi']))

# cities = {
#     'neimeng' : {
#         'conutry':'chifeng',
#         'renshu':5
#         },
#     'beijing' :{
#         'conutry':'haidian',
#         'renshu':6
#         }
#     }
# for name,city in cities.items():
#     print('省级名字:' +name)
#     print('状况：'+city['conutry'] +' ' +str(city['renshu']))
