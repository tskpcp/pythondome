import matplotlib.pyplot as plt
def listDdp():
    list_year=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
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
  #画柱状图
    plt.bar(list_year,list_gdp)
    plt.title('gdp amount from 2006 to 2017')
    plt.xlabel('year')
    plt.ylabel('gdp amount')

    plt.savefig('1.jpg',dpi=100)
    plt.show()
