def test():
    #获取字符串的值
        str="qazxswedc"
        # 输出第一个字符
        print(str[0])
        # 输出下标1-4（不包括4）
        print(str[1:4])
        # 输出下标从2开始到全部
        print(str[2:])
        # 从倒数第二个字符开始输出
        print(str[-2:])

    #字符串操作
        #  + 拼接两个字符串
        str1="hello"
        str2="world"
        print(str1+""+str2)
        # * 重复输出某个字符串
        str3 = "Hello ya!"
        print(str3 * 3)
        # in ;  not in  判断字符串是否包含 给定的字符
        str4 = "Hello world"
        if 'H' in str4:
            print(" 'H' is in")
        if 'M' not in str4:
            print(" 'M' is not in")

    #序列的通用操作
        #声明序列
            # 单个序列
            student=["xxx",20]
            seq=["abc","def","ghj"]
            # 字符串是以单个字符为元素的序列
            str="abcde"
            # 包含其他序列的序列
            somepeople = [["lisi", 21], ["wangwu", 22], ["zhaoliu", 23]]
            # 空列表 可以用[] 来表示， None 为python的内建值，表示空
            # 创建 占用10个元素空间的空列表
            seq = [None] * 10
        #索引
            # 通过下标访问
            people = ["xiongda", "xionger", "zhangsan"]
            print(people[0])
            print(people[-1])
            print(people[2])
        #分片
            # 分片 ： 使用索引访问一定范围内的元素，通过冒号 隔开两个索引
            # 第一个索引的元素包含在分片内，第二个不包含
            number = [1, 2, 3, 4, 5, 6, 7]
            print(number[2:5])
            print(number[-3:-1])
            # 如果第一个索引，比第二个索引晚出现在序列中，分片结果就是一个空序列
            print(number[3:1])
            print(number[-1:-3])
            # 分片 [a:b] ，  a b的值也可省略，[:b] 从0开始 到b
            # [a:]从a开始 到最后； [:] 都省略，表示 遍历所有，可以用于复制序列
            name = "LiuYuanJu"
            print(name[0:3])
            print(name[3:])
            print(name[:3])
            print(name[:])
            # 步长 ： 通常隐式设为 1 ，也可显示设置；
            number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            print(number1[0:10:2])
        #序列运算符
            # + 运算符 进行同类型的序列连接，但是并不改变原序列
            print([1,2,3] + [4,5,6] )
            print("hello" + "men")
            # * 生成一个新序列，将 原序列重复 n  次
            print("Ha" * 10 )
        #常用内建函数
            # len()  返回长度
            # max()  min() 最大最小值
            # in 检查是否  具有成员资格，即 是否包含
    #列表:除了序列的基本操作，列表还有许多改变列表的方法
        #基本操作
            # list() 可将某种类型的数据转换为 对应的序列， list是一种数据类型
            print(list("hello"))
            # 1. 改变列表;元素赋值
            x = [1, 2, 3]
            x[1] = 0
            print(x)
            # 2. 删除元素
            people = ["zhangsan", "lisi", "wangwu"]
            del people[2]
            print(name)
            print(people)
            # 3. 分片赋值
            py = list("python")
            print(py)
            py[1:3] = list("om")
            print(py)
            py[1:] = list("po")
            print(py)
        #列表方法
            # append  列表末尾加入新对象
            list1 = [1, 2, 3]
            list1.append(4)
            print(list1)
            # count 统计某个元素出现的次数
            list1.count(2)
            # extend 在末尾 一次性追加 另一个序列中的多个值
            list2 = [7, 8, 9]
            list1.extend(list2)
            print(list1)
            # index 返回与某个值匹配的第一个索引位置
            print(list1.index(3))
            # insert 向列表中插入对象
            list1.insert(1, "first")
            print(list1)
            # pop 移除列表最后一个元素， 并返回该元素的值
            list1.pop()
            # remove 移除某个值的 第一个  匹配项
            list1.remove("first")
            # reverse 将列表元素 倒序
            list1.reverse()
            # sort 在列表原位置 进行排序， 改变了原来的列表
            list1.sort()
            # sorted 返回一个列表排序后的 <span style="font-family: Arial, Helvetica, sans-serif;">副本列表</span>
            list2 = sorted(list1)
        #元组:元组不能修改，用（）括起来。用 逗号 隔开一些值，就自动创建的元组， 如果只有一个值，也必须加上逗号
            # 元组
            print(1,2,3 )
            # tuple 将一个序列转换为 元组
            print(tuple([1,2,3]))
        #字典
            #1.字典的格式：字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
            data = {"name": "liu", "age": 18}
            print(data)
            #2.访问字典的值
            person = {"name": "liu", "age": 12, "sex": "man"}
            print(person["name"])
            #3.基本的字典操作
             #len(d)   返回 项（键值对）的数量
             #d[key]  返回关联到 键 key 上的值
             #d[key] = v 将值关联到 键 key 上
             #del d[k] 删除 键为 k 的项
             #k in d 检查 d 中是否含有键为k 的项
            #4. 字典的内置方法
            # clear 清除字典中的所有项
            x = {"name": "liu", "age": 12, "sex": "man"}
            x.clear()
            print(x)
            # copy  浅复制，当在副本中替换值时，原副>>>#本不受影响，但添加删除（原地修改）时，原字典也会改变
            x = {"name": "liu", "hobby": ["music", "game", "running"]}
            y = x.copy()
            print(y)
            y["name"] = "zhangsan"
            y["hobby"].remove("game")
            print(y)
            print(x)
            # deepcopy  深复制
            from copy import deepcopy
            x = {"name": "liu", "hobby": ["music", "game", "running"]}
            dy = deepcopy(x)
            print(dy)
            dy["name"] = "zhangsan"
            dy["hobby"].append("reading")
            print(dy)
            print(x)
            # fromkeys
            # 使用给定的键 建立新字典
            dict.fromkeys(["name", "age"])
            # get 宽松的访问字典的方式 如果不存在，不会报错，而是 None
            print(data.get("name"))
            print(data.get("sex"))
            print(data.get("sex", "N/A")) # 自定义 “默认值”
            # update 利用一个字典项 更新另一个字典
            x = {"name": "liu", "age": 12}
            y = {"name": "zhangsan"}
            x.update(y)
            print(x)