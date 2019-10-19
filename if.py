# age = 19
# if age >= 18:  #if语句测试真假
#     print('you are old enough to vote!')
#     print('have you registered to vote yet?')

# age = 17
# if age >=18:  #if-else语句测试
#     print('you are old enough to vote!')
#     print('have you registered to vote yet?')
# else:
#     print('sorry,you are too young to vote.')
#     print('please register to ote as soon as you turn 18!')

# age = 12
# if age < 4: #if-elif-else测试
#     print('your admission cost is $0.')
# elif age < 18:
#     print('your admission cost is $5.')
# else:
#     print('your admission cost is $10.')

# age = 12
# if age < 4:  #if-elif-else测试，使代码更简洁
#     price=0
# elif age < 18:
#     price=5
# else:
#     price = 10
# print('your admission cost is $' + str(price)+'.')

# age = 12   #if-elif-else
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# else:
#     price = 5
# print('your admission cost is $' + str(price)+ '.')

# age = 12   #if-elif-elif
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >=65:
#     price = 5
# print('your admission cost is $' + str(price) + '.')

# requestd_toppings = ['mushrooms', 'extra cheese']  #if-if测试，不管第一个条件是否通过，都会执行下面几条
# if 'mushrooms' in requestd_toppings:
#     print('adding mushrooms')
# if 'pepperoni' in requestd_toppings:
#     print('adding pepperoni.')
# if 'extra cheese' in requestd_toppings:
#     print('adding extra cheese.')
# print('\nFinished making your pizza!')