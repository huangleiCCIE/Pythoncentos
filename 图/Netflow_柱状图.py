from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置中文
plt.rcParams['font.family'] = 'sans-serif'
colorlist = ['r', 'b', 'g', 'y']

def mat_zhu(size_list, name_list):

    #调节图形宽、高
    plt.figure(figsize = (6,6))

    #横向柱状图
    #plt.barh(name_list,size_list,height=0.5,color=colorlist)

    #竖向柱状图
    plt.bar(name_list, size_list, width=0.5, color=colorlist)

    #添加主题和注释
    plt.title('协议与带宽分布') #主题
    plt.xlabel('带宽(M/S)') #X轴注释
    plt.ylabel('协议') #Y轴注释

    #保存成图片
    plt.savefig('result1.png')

    #绘制图形
    plt.show()
def mat_zhu_mark(size_list, name_list, x_label, y_label, title):
    #调节图形大小、宽、高
    fig = plt.figure(figsize = (6,6))
    ax = fig.add_subplot(111)

    fig.autofmt_xdate() #当x轴太拥挤的时候可以让他自适应

    ax.bar(name_list, size_list, width=0.5)

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.title(title) #主题
    plt.xlabel(x_label)  #x轴注释
    plt.ylabel(y_label)  #y轴注释
    #保存图片
    plt.savefig('result.png')
    #绘制图形
    plt.show()

if __name__ == '__main__':
    counters = [30, 53, 12, 45]   #y轴数据
    protocols = ['http协议', 'ftp协议', 'rdp协议','qq协议']  #x轴数据
    mat_zhu(counters, protocols)