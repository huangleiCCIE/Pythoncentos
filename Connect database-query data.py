import sqlite3

information = """
请输入查询选项：
输入 1 : 查询整个数据库
输入 2 ： 基于姓名查询
输入 3 ： 基于年龄查询
输入 4 ： 基于作业数查询
输入 0 ： 退出
"""

def result_str(sql):
    conn = sqlite3.connect('qytanghomework.sqlite')  #连接qytanghomework数据库
    cursor = conn.cursor()
    all_info = cursor.execute(sql)  #执行搜索
    all_description = [des[0] for des in all_info.description]   #搜索列标题传给all_description
    seach_result = cursor.fetchall() #将结果传给seach_result
    if not seach_result:  #如果搜索结果没找到
        conn.close()   #关闭数据库
        return '学员信息未找到'  #返回 '学员信息未找到' 字符串

    return_str = ''
    for x in seach_result:    #遍历结果
        for y in zip(all_description,x):#将标题和结果压缩到一起
            return_str += f'{y[0]:>3}:{y[1]:<3}'  #格式化打印一下
        return_str += '\n' #换行
    conn.close()  #关闭数据库连接
    return return_str   #返回组合到一起的字符串

while True:
    print(information) #打印信息
    user_input = input('请选择：') #让用户输入
    if user_input == '0':  #输入是0，退出程序
        break

    elif user_input == '1':  #用户输入1，打印整个表
        print(result_str('select * from qytang_homework_info'))

    elif user_input == '2':  #用户输入2，根据姓名查询
        user_sn = input('请输入学员姓名：') #用户输入学员姓名
        if not user_sn:  #如果没有该学员，继续循环
            continue
        print(result_str('select * from qytang_homework_info where 姓名 = "{0}"'.format(user_sn)))  #查询表中关于用户输入的该学员信息

    elif user_input == '3':
        user_gae = input('搜索大于输入年龄的学员，请输入学员年龄：')
        if not user_gae:
            continue
        print(result_str('select * from qytang_homework_info where 年龄 > "{0}"'.format(user_gae)))


    elif user_input == '4':
        user_homework = input('搜索大于输入作业数的学员，请输入作业数量：')
        if not user_homework:
            continue
        print(result_str('select * from qytang_homework_info where 作业数 > "{0}"'.format(user_homework)))

    else:
        print('输入错误，请重试')