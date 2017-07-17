if __name__=='__main__':
    import random
    import sort
    b=range(10)
    a=random.sample(b,10)
    print("a=",a)
    print("归并排序=",sort.merge_sort(a))
    print("冒泡排序=", sort.bubble_sort(a))
    print("直接插入排序=", sort.direct_insertion_sort(a))
    print("希尔排序=", sort.shell_sort(a))


