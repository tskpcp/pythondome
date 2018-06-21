import matplotlib.pyplot as plt
def gdp2017Equal():
    gdp_2017={
        'primary industry':65468,
        'secondary industry':334623,
        'tertiart industry':427032
    }
    labels=gdp_2017.keys()
    values=gdp_2017.values()

    plt.figure(figsize=(6,6))
    plt.pie(values,labels=labels,autopct='%.1f%%',startangle=90)
    plt.axis('equal')
    plt.legend()
    plt.show()