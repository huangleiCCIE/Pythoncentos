# alien_0 = {'color' : 'green' , 'points' : 5}   #列表中嵌套字典
# alien_1 = {'color' : 'yellow' , 'points' : 10}
# alien_2 = {'color' : 'red' , 'points' : 15}
#
# aliens = [alien_0 , alien_1 , alien_2]
# for alien in aliens:
#     print(alien)
#
# aliens = []     #一个字典打印30次
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print('...')
# print('Total number of aliens: '+ str(len(aliens)))
#
# aliens = []  #一个字典打印30次，且前三个字典如果color值为green，则将color值改为yellow，speed值改为medium，points值改为10
# for alien_number in range (0,30):
#     new_alien = {'color': 'green', 'points':5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# for alien in aliens[0:5]:
#     print(alien)
# print('...')
#
# pizza = {   #字典里引用列表
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
#     }
# print('You ordered a ' + pizza['crust'] + '-crust pizza' + 'with the following toppings:')
# for topping in pizza['toppings']:
#     print("\t"+ topping)

# favorite_languages = {      #字典嵌套列表
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell']
# }
# for name, languages in favorite_languages.items():
#     print('\n' + name.title() + "'s favorite languages are:")
#     for language in languages:
#         print('\t' + language.title())

# users = {               #字典嵌套字典
#     'aeinstein' : {
#         'first' : 'albert',
#         'last' : 'einstein',
#         'location' : 'princeton'
#         },
#     'mcurie':{
#         'first' : 'marie',
#         'last' : 'curie',
#         'location' : 'paris',
#         }
#     }
# for username, user_info in users.items():
#     print('\nUsername: ' + username)
#     full_name = user_info['first'] + ' '+ user_info['last']
#     location = user_info['location']
#     print('\tFull name:'+full_name.title())
#     print('\tLocation: '+ location.title())