# current_number = 1    #使用while循环，打印1到5
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = '\nTell me something, and I will repeat it back to you:'
# prompt += "\nEnter 'quit' to end the program."
# message = ''
# while message != 'quit':     #使用while + if 的循环，客户输入quit才会退出，并且输入quit不打印
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = '\nTell me something, and Iwill repeat it back to you:'
# # prompt +="\nEnter 'quit' to end the program."
# #
# # active = True       #设置一个标志为true，使代码可以进入while，当用户输入quit，则active就为假，就会终止循环
# # while active:
# #     message = input(prompt)
# #     if message == 'quit':
# #         active = False
# #     else:
# #         print(message)

# prompt = '\nPlease enter the name of a city you have visited:'
# prompt += "\n(Enter 'quit' when you are finished.)"
#
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break     #使用break强制退出循环
#     else:
#         print("I'd love to go to " + city.title() + "!")

# current_number = 0
# while current_number < 10:
#     current_number +=1
#     if current_number % 2 == 0:
#         continue                   #continue的作用是，如果余数等于0，则不会执行下面的代码
#     print(current_number)

# unconfirmed_users = ['alice', 'brian','candace']  #通过while,使列表里的值放到其它变量
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print('Verifying user:' + current_user.title())
#     confirmed_users.append(current_user)
# print('\nThe following users have been confirmed:')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat'] #通过while删除列表中不想要的值
# # print(pets)
# # while 'cat' in pets:
# #     pets.remove('cat')
# # print(pets)

# responses = {}   #通过while打印将用户输入的值,组成字典
# polling_active = True
# while polling_active:
#     name = input('\nWhat is your name?')
#     response = input('Which mountain would you like to climb someday?')
#     responses[name] = response
#     repeat = input('Would you like to let another person respond?(yes/no)')
#     if repeat == 'no':
#         polling_active = False
# print('\n--- Poll Results ---')
# for name,response in responses.items():
#     print(name + ' would like to climb ' + response + '.')

