# bicycles = ['trek', 'cannondale', 'rediline', 'specialized']  #列表
# #              0         1             2             3
# #             -4        -3            -2            -1
# print(bicycles[0].title())
# print(bicycles[-1].title())

# bicycles = ['trek', 'cannondale', 'rediline', 'specialized']    #字符串+列表+引用
# message = 'my first bicycle was a ' + bicycles[0].title() + '.'
# # print(message)

# motorcycles=['honda', 'yamaha', 'suzuki']    #修改列表中的值
# motorcycles[0]='ducati'
# print(motorcycles)

# motorcyles = ['honda', 'yamaha', 'suzuki'] #列表中添加新值
# motorcyles.append('ducati')
# print(motorcyles)

# motorcycles = []   #空列表中添加值
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki'] #在列表固定位置中添加新值
# motorcycles.insert(0, 'ducati')
# motorcycles.insert(1, 'moto')
# print(motorcycles)

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:  #循环打印列表，当打印bmw时，所有字母大写，其它则首字母大写
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# motorcycles= ['honda', 'yamaha', 'suzuki'] #删除列表中的特定元素，删除后，该元素不能继续使用
# del motorcycles[1]
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']  #将列表中最后一位弹出，并且赋值给新的变量
# popped_motorcycle = motorcycles.pop()   #想弹出具体参数，需要在.pop()添加位置信息
# print(popped_motorcycle)

# motorcysles = ['hona', 'yamaha', 'suzuki', 'ducati'] #可以使用remove删除具体参数，删除之后可以继续使用
# too_expensive = 'ducati'
# motorcysles.remove(too_expensive)
# print(motorcysles)
# print('\nA ' + too_expensive)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()    #永久性按照字母正序排序
# print(cars)
# cars.sort(reverse=True)   #永久性按照字母倒序排序
# print(cars)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(sorted(cars))   #临时性的按照字母排序，如果想倒序排序，则可以print(sorted(cars,reverse=True))
# print(cars)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.reverse()    #永久性倒着排序，如果想恢复，可以在执行一遍该命令
# print(cars)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars))  #确定列表的长度

# magicians = ['alice', 'david', 'carolina']  #使用for循环，循环打印列表中每一个元素
# for magician in magicians:
#     print(magician.title() + ',that was a great trick')
#     print("I can't wait to see your next trick,"+ magician.title() + ".\n")
# print('Thank you,everyone.That was a great magic show!')

# for value in range(1,7): #打印1到6的数字
#     print(value)

# squares = []    #以列表的形式打印1到10数字的平方
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)

# digits = [1,2,3,4,5,6,7,8,9,0]
# # print(min(digits))  #找出列表中最小值
# # print(max(digits))  #找出列表中最大值
# # print(sum(digits))  #列表的总和

# squares = []
# for value in range(1,11):  #得出1到10中的平方，以列表方式显示
#     square = value ** 2
#     squares.append(square)
# print(squares)

# squares = [value ** 2 for value in range(1,11)]  #通过列表解析以列表的形式打印1到10数字的平方
# print(squares)

# even_numbers = list(range(2,11,2))  #通过步长打印数字列表   2开始，超过11的数结束，每次增加2
# # print(even_numbers)

# players = ['charles', 'martina', 'michael', 'florence', 'eli'] #列表切片
# #              0          1          2           3        4
# print(players[1:4]) #范围是1-3，不包括最后4

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[:4]) #如果没有指定一个索引，自动从列表开头开始

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# # #             0           1          2           3        4
# #               -5          -4        -3          -2       -1
# # print(players[2:])  #在第二个开始，一直到最后
# print(players[-3:])   #倒数后三名

# players = ['charles', 'martina', 'michael', 'flrence', 'eli']
# for player in players[:3]:     #遍历切片
#     print(player.title())

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]    #将列表复制到一个新的列表，如果使用friend_foods = my_foods,只是两个变量同时引用一个列表
# my_foods.append('cannoli')
# friend_foods.append('kele')
# print(my_foods)
# print(friend_foods)