# anlien_0 = {'color': 'green', 'points':5}  #提取字典中的值
# print(anlien_0['color'])

# alien_0 = {'color': 'green', 'points':5} #字典中提取值并赋给新的变量
# new_points = alien_0['points']
# print('You just earned ' + str(new_points) + ' points!')

# alien_0 = {'color': 'green', 'points':5} #字典中插入新值
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {} #空字典中添加新值
# alien_0['color'] = 'green'
# alien_0['points']=5
# print(alien_0)

# alien_0 = {'color':'green'}  # 修改字典里的值
# print('The alien is ' + alien_0['color']+'.')
# alien_0['color'] = 'yellow'
# print('The alien is now ' + alien_0['color']+'.')

# alien_0 = {'x_position' : 0, 'y_position': 25, 'speed': 'medium'}  #修改字典里的值
# print('Original x-position: ' + str(alien_0['x_position']))
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print('New x-position: ' + str(alien_0['x_position']))

# alien_0 = {'color': 'green','points':5}  #使用del永久删除字典里的键与值
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# favorite_languages = {  #创建字典，提取值并以大写显示
#     'jen':'pytnon',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python',
#     }
# print("Sarah's favprite language is " +
#       favorite_languages['sarah'].title()+
#       '.')

# user_0 = {    #使用for循环，遍历字典里的键与值
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi'
#     }
# for key,value in user_0.items():
#     print('\nkey: ' + key)
#     print('value: ' + value)

# favorite_languages = {    #使用for循环，遍历字典里的键与值
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python'
#     }
# for name,language in favorite_languages.items():
#     print(name.title()+"'s favorite language is "+ language.title() + '.')


# favorite_languages = {   #使用if语句，确定一个字符是否包含在字典里
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python'
#     }
# if 'erin' not in favorite_languages.keys():
#     print('Erin,please take our poll!')

# favorite_languages = {    #遍历字典中的键，并排序
#     'jen': 'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python'
#     }
# for name in sorted(favorite_languages.keys()):
#     print(name.title()+', thank you for taking the poll.')

# favorite_languages = {    #遍历字典里的值
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ruby',
#     'phil' : 'python'
#     }
# print('The following languages have been mentioned:')
# for language in favorite_languages.values():
#     print(language.title())

# favorite_languages = {      #通过set，打印字典里不重复的值
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python'
#     }
# print('The following languages have been mentioned:')
# for language in set(favorite_languages.values()):
#     print(language.title())



