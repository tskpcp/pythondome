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

