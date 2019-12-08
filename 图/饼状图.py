from matplotlib import pyplot as plt
import matplotlib
plt.rcParams['font.sans-serif'] = ['SimHei']  #设置中文
plt.rcParams['font.family'] = 'sans-serif'

matplotlib.matplotlib_fname()
def mat_bing(size_list, name_list):
    #调节图形大小、宽、高
    plt.figure(figsize=(6,6))

    patches, label_text, percent_text = plt.pie(size_list,
                                        labels=name_list,
                                        labeldistance=1.1,
                                        autopct='%3.1f%%',
                                        shadow=False,
                                        startangle=90,
                                        pctdistance=0.6)
    #labeldistance:文本的位置离远点有多远，1,1指1.1倍半径的位置
    #autopct:圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    #shadow:饼是否有阴影
    #startangle:起始角度，0：表示从-开始逆时针转，为第一块，一般选择从90度开始比较好看
    #pctdistance：百分比的text离圆心的距离
    #patches、label_text、percent_text：p_text:饼图内部文本  l_text:饼图外部文本

    #改变文本的大小
    #方法是把每一个text遍历，调用set_size方法设置它的属性
    for l in label_text:
        l.set_size = 30
    for p in percent_text:
        p.set_size = 20

    #设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    counters = [30, 53, 12, 45]   #窜进每一块的大小
    protocols = ['http协议','ftp协议', 'rdp协议', 'qq协议']
    mat_bing(counters,protocols)
