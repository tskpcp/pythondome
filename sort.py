# 归并排序：利用递归，把一个数组无限二分，知道分到只剩两个值，然后进行排序形成新的数组。接着跟上一层的数组进行排序，直到对整个数组排序完成。
def merge(a,b):
    c=[]
    h=j=0
    while j<len(a) and h<len(b):
        if a[j]<b[h]:
            c.append(a[j])
            j+=1
        else:
            c.append(b[h])
            h+=1
    if j==len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c

def merge_sort(lists):
    if len(lists)<=1:
        return lists
    middle=int(len(lists)/2)
    left=merge_sort(lists[:middle])
    right=merge_sort(lists[middle:])
    return merge(left,right)

#希尔排序
#首先对n/2个间距分别进行比较两两比较。把较大的数放在后面。接着把间距再缩小一半进行排序。直到间距等于0.
def shell_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = int(len(lists) / 2)
    while middle>0:
        for j in range(middle):
            for i in range(0,int(len(lists)/middle-1)-1):
                if lists[i+j]>lists[i+j+1]:
                    lists[i+j],lists[i+j+1]=lists[i+j+1],lists[i+j]
        middle=int(middle/2)
    return lists
#冒泡排序
def bubble_sort(lists):
 if len(lists)<1:
     return lists
 for i in range(len(lists)-1,-1,-1):
        for j in range(i):
            if lists[j]<lists[j+1]:
                lists[j],lists[j+1]=lists[j+1],lists[j]
 return lists
#直接插入排序
def direct_insertion_sort(lists):
    if len(lists) < 1:
        return lists
    for i in range(1,len(lists)):
        key=lists[i]
        for j in range(i-1,-1,-1):
            if lists[j]>key:
                lists[j+1],lists[j]=lists[j],lists[j+1]
            else:
                    break
    return lists
#快速排序

#（1）确定该期间的中间位置K
#（2）将查找的值T与array[k]比较。若相等，查找成功返回此位置；否则确定新的查找区域，继续二分查找。区域确定如下：
#a.array[k]>T 由数组的有序性可知array[k,k+1,……,high]>T;故新的区间为array[low,……，K-1]
#b.array[k]<T 类似上面查找区间为array[k+1,……，high]。每一次查找与中间值比较，可以确定是否查找成功，不成功当前查找区间缩小一半。递归找，即可。
#3.时间复杂度:O(log2n);
#注意：二分查找的前提必须待查找的序列有序。

def BinarySearch(array,t):
    low = 0
    height = len(array)-1
    while low < height:
        mid = (low+height)/2
        if array[mid] < t:
            low = mid + 1

        elif array[mid] > t:
            height = mid - 1

        else:
            return array[mid]

    return -1

#快速排序
#．先从数列中取出一个数作为基准数。

#．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。

#．再对左右区间重复第二步，直到各区间只有一个数。
def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low
def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)

#选择排序
#对于一组关键字{K1,K2,…,Kn}， 首先从K1,K2,…,Kn中选择最小值，假如它是 Kz，则将Kz与 K1对换；

#然后从K2，K3，… ，Kn中选择最小值 Kz，再将Kz与K2对换。

#如此进行选择和调换n-2趟，第(n-1)趟，从Kn-1、Kn中选择最小值 Kz将Kz与Kn-1对换，最后剩下的就是该序列中的最大值，一个由小到大的有序序列就这样形成。
#时间复杂度  O(n*n)
def selection_sort(list2):
    for i in range(0, len (list2)):
        min = i
        for j in range(i + 1, len(list2)):
            if list2[j] < list2[min]:
                min = j
        list2[i], list2[min] = list2[min], list2[i]  # swap