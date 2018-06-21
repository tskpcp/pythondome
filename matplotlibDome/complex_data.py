import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
def complexData():
    list_year = [
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017
    ]


    list_gdp = [
        219438.50,
        270232.30,
        319515.50,
        349081.40,
        413030.30,
        489300.60,
        540367.40,
        595244.40,
        643974.00,
        689052.10,
        744127.20,
        827122.00
    ]

    list_gdp_growth = [
        12.70,
        14.20,
        9.70,
        9.40,
        10.60,
        9.50,
        7.90,
        7.80,
        7.30,
        6.90,
        6.70,
        6.90
    ]
    #1. 画GDP总量柱状图，增长率折线图
    #plt.figure(figsize=(8,6))
    # plt.bar(list_year,list_gdp)
    # plt.plot(list_year,list_gdp_growth,color='red')
    # plt.title('gdp amount / growth from 2006 to 2007')
    # plt.xlabel('year')
    # plt.ylabel('gdp amout / growth')
    # plt.show()

    # 2.画GDP总量柱状图，增长率折线图，使用双坐标系
    # fig=plt.figure(figsize=(8,6))
    #
    # ax1=fig.add_subplot(2,1,1)
    # ax1.bar(list_year,list_gdp,label='gdp amout')
    # ax1.legend(loc='upper left')
    # ax1.set_xlabel('year')
    # ax1.set_ylabel('gdb amount')
    #
    # ax2 = ax1.twinx()
    # ax2.plot(list_year,list_gdp_growth,color='red',label='gdb growth')
    # ax2.legend(loc='upper right')
    # ax2.set_ylabel('gdp growth')
    # ax2.set_ylim(0,20)
    # ax2.set_title('gdp amount/ growth from 2006 to 2007')
    # plt.show()

    #3.画GDP总量柱状图，增长率折线图，使用上下子图
    # 设置图片大小
    # fig = plt.figure(figsize=(8, 6))
    #
    # # 画柱状图
    # ax1 = fig.add_subplot(2, 1, 1)
    # ax1.bar(list_year, list_gdp, label='gdp amount')
    # ax1.legend(loc='upper left')
    # ax1.set_ylabel('gdp amount')
    # ax1.set_title('gdp amount from 2006 to 2017')
    #
    # # 画折现图
    # ax2 = fig.add_subplot(2, 1, 2)
    # ax2.plot(list_year, list_gdp_growth, color='red', label='gdp growth')
    # ax2.legend(loc='upper right')
    # ax2.set_ylabel('gdp growth')
    # ax2.set_ylim(0, 15)
    # ax2.set_title('gdp growth from 2006 to 2017')
    # ax2.grid(True)
    #
    # # 调整子图之间的间距
    # plt.tight_layout()
    #
    # # 显示画图结果
    # plt.show()


    #4.画GDP总量柱状图，增长率折线图，使用左右子图
    # # 设置图片大小
    # fig = plt.figure(figsize=(16, 6))
    #
    # # 画柱状图
    #add_subplot(行、列、索引值)
    # ax1 = fig.add_subplot(1, 2, 1)
    # ax1.bar(list_year, list_gdp, label='gdp amount')
    # ax1.legend(loc='upper left')
    # ax1.set_ylabel('gdp amount')
    # ax1.set_title('gdp amount from 2006 to 2017')
    #
    # ax2 = fig.add_subplot(1, 2, 2)
    # ax2.plot(list_year, list_gdp_growth, color='red', label='gdp growth')
    # ax2.legend(loc='upper right')
    # ax2.set_ylabel('gdp growth')
    # ax2.set_ylim(0, 15)
    # ax2.set_title('gdp growth from 2006 to 2017')
    # ax2.grid(True)
    #
    # # 调整子图之间的间距
    # plt.tight_layout()
    #
    # # 显示画图结果
    # plt.show()

    #5.坐标使用中文

    # 指定默认字体
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    # 解决保存图像是负号'-'显示为方块的问题
    mpl.rcParams['axes.unicode_minus'] = False

    # 设置图片大小
    fig = plt.figure(figsize=(8, 6))

    # 画柱状图
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.bar(list_year, list_gdp, label='gdp总量')
    ax1.legend(loc='upper left')
    ax1.set_xlabel('年份')
    ax1.set_ylabel('gdp总量')

    # 画折线图
    ax2 = ax1.twinx()
    ax2.plot(list_year, list_gdp_growth, color='red', label='gdp增长率')
    ax2.legend(loc='upper left')
    ax2.set_ylabel('gdp增长率')
    ax2.set_ylim(0, 20)

    # 标识标题及坐标轴信息
    plt.title('2006 至 2017 中国GDP 总量 / 增长率 示意图')

    plt.legend()

    # 显示画图结果
    plt.show()