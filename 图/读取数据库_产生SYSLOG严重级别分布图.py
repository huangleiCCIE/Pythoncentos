import  sqlite3
from dateutil import parser
from matplotlib import pyplot as plt
from 图.syslog_wdb import severity_level_dict

def syslog_show(name_list, count_list, show_name):
    plt.rcParams['font.sans-serif'] = ['SimHei']  #设置中文
    #调节图形大小，宽，高
    plt.figure(figsize=(6,6))

    #使用count_list的比例来绘制饼图
    #使用level_list作为注释
    patches, l_text, p_text = plt.pie(count_list,
                                      labels=name_list,
                                      labeldistance=1.1,
                                      autopct='%3.1f%%',
                                      shadow=False,
                                      startangle=90,
                                      pctdistance=0.6)
    # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance，百分比的text离圆心的距离
    # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
    for t in l_text:
        t.set_size = 30
    for t in p_text:
        t.set_size = 20
    #设置x,y轴刻度一致
    plt.axis('equal')
    plt.title(show_name) #主题
    plt.legend()
    plt.show()

if __name__ == '__main__':
    #连接数据库
    conn = sqlite3.connect('syslog.sqlite')
    cursor = conn.cursor()

    #syslog严重级别分布图
    cursor.execute('select severity_level_name, COUNT(*) from syslogdb group by  severity_level_name')  #以安全级别分类并统计次数
    yourresult = cursor.fetchall()

    #提取严重级别和次数
    severity_level_name_list = []
    severity_level_count_list = []
    for severity_level_name_count in yourresult:
        severity_level_name_list.append(severity_level_name_count[0]) #严重级别提取出来
        severity_level_count_list.append(severity_level_name_count[1])  #次数取出来
    syslog_show(severity_level_name_list, severity_level_count_list, 'SYSLOG严重级别分布图')

#-----------------------------------------------------------------------------------------------------------------------------------------------
    #日志源分布图
    cursor.execute('select log_source, COUNT(*) from syslogdb group by  log_source')  # 以安全级别分类并统计次数
    yourresult = cursor.fetchall()

    log_source_name_list = []
    log_source_count_list = []
    for log_source_name_count in yourresult:
        log_source_name_list.append(log_source_name_count[0])  # 严重级别提取出来
        log_source_count_list.append(log_source_name_count[1])  # 次数取出来
    syslog_show(log_source_name_list, log_source_count_list, '日志源分布图')
    conn.close()