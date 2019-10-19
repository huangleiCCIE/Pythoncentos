# import matplotlib.pyplot as plt
# squares = [1,4,9,16,25]   # 只是标明了y轴
# plt.plot(squares,linewidth=2) #曲线图线条的粗细
# plt.title("Square Numbers",fontsize=24) #图上文字
# plt.xlabel("Value",fontsize=14) #图下文字
# plt.ylabel("Square of Value", fontsize=14) #图左文字
# plt.tick_params(axis='both', labelsize=14) #标签大小
# plt.show()

# import matplotlib.pyplot as plt
# # input_values = [1, 2, 3, 4, 5,] #标明了x轴
# # squares = [1, 4, 9, 16, 25] #标明了y轴
# # plt.plot(input_values, squares, linewidth=5) #曲线图
# # plt.show()

# import matplotlib.pyplot as plt
# plt.scatter(2,4,s=5)  #输出点的样式，调整点的x轴和y轴以及大小
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value',fontsize=14)
# plt.ylabel('Square of Value',fontsize=14)
# plt.show()

# import matplotlib.pyplot as plt
# x_values = [1, 2, 3, 4, 5]  #x轴
# y_values = [1, 4, 9, 16, 25] #y轴
# plt.scatter(x_values, y_values, s=20)
# plt.show()

# import matplotlib.pyplot as plt
# x_values = list(range(1,5))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values,y_values,s=20)
# plt.axis([0,5,0,25])
# plt.show()