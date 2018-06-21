if __name__=='__main__':
    import random
    from finish import sort

    a=random.sample(range(100),10)
    #
    print("a=",a)
    #
    #print("归并排序=",sort.merge_sort(a))
    # print("冒泡排序=", sort.bubble_sort(a))
    print("直接插入排序=", sort.direct_insertion_sort(a))
    print("希尔排序=", sort.shell_sort(a))
    #print("二分发",sort.BinarySearch([a],3))
    print("快速排序", sort.quick_sort(a, 0, len(a) - 1))
   # import numpy_test
    # print(test.pySum())
    # print(test.npSum())
   # import mysql
   # print(mysql.mysqldome())

    # from mysqldbHelper import *
    #
    # helper=mySqlDBHelper('192.168.1.249',3306,'root','root','utf8')
    # helper.setDB("pythontest")
    # # 查询
    # sql = "select * from cms_admin_mst"
    # rows = helper.queryAll(sql)
    # for row in rows:
    #     print(row['LOGIN_ID'], row['USER_NAME'],row['POSITION'],row['MARK'])
   #添加
   #dataSource={"LOGIN_ID":"2","PASSWORD":"123456","USER_NAME":"我们"}
   #helper.insert("cms_admin_mst",dataSource)
   #print(helper.getLastInsertRowId())
    #修改
    #pData={"POSITION":"uPDATE","MARK":"3"}
    #whereData={"LOGIN_ID":"2"}
    #helper.update("cms_admin_mst",pData,whereData)

    # import getHtml
    # html=getHtml.gethtml("http://www.toutiao.com/a6421022940322513153/?iid=11431899230&app=news_article")
    # print(html)

    #import test
    #test.test()


    from developing import graph

    g= graph.Graph()
    g.add_nodes([i+1 for i in range(8)])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))
    print("nodes:", g.nodes())
    #广度优先搜索算法
    order = g.breadth_first_search(1)
    # 深度优先搜索算法
    order = g.depth_first_search(1)

    #python数据结构之图深度优先和广度优先实例详解
    #http: // www.jb51.net / article / 69145.htm
    #Python 广度优先 / 深度优先遍历二叉树
    #http: // www.jianshu.com / p / 7d665f3c01bc
   # 二、基本算法之DFS、BFS和A *
   # http: // blog.csdn.net / moodytong / article / details / 7651801
   # 随笔分类 - python
    #http: // www.cnblogs.com / yupeng / category / 521124. html

#【永无休止】Python数据分析（六）：通用函数，快速的元素级数组函数
#http://www.toutiao.com/a6399931270432588034/?iid=7739938160&app=news_article

# http://blog.csdn.net/qq_33528613/article/category/6902810/3
#http: //blog.csdn.net/work201003/article/category/6047021
#【达人科技】Python 3 集合基础和概念!
#https://www.baidu.com/s?ie=utf8&oe=utf8&wd=%E3%80%90%E8%BE%BE%E4%BA%BA%E7%A7%91%E6%8A%80%E3%80%91Python%203%20%E9%9B%86%E5%90%88%E5%9F%BA%E7%A1%80%E5%92%8C%E6%A6%82%E5%BF%B5%EF%BC%81&tn=98010089_dg&ch=3
#【博客园】Python自动化开发(三):循环次数控制、常用数据类型、字符串格式化、列
#https://www.baidu.com/s?ie=utf8&oe=utf8&wd=%E3%80%90%E5%8D%9A%E5%AE%A2%E5%9B%AD%E3%80%91Python%E8%87%AA%E5%8A%A8%E5%8C%96%E5%BC%80%E5%8F%91%EF%BC%88%E4%B8%89%EF%BC%89%EF%BC%9A%E5%BE%AA%E7%8E%AF%E6%AC%A1%E6%95%B0%E6%8E%A7%E5%88%B6%E3%80%81%E5%B8%B8%E7%94%A8%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%E3%80%81%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%A0%BC%E5%BC%8F%E5%8C%96%E3%80%81%E5%88%97%E8%A1%A8%E5%B8%B8%E7%94%A8%E6%93%8D%E4%BD%9C%E3%80%81%E5%88%97%E8%A1%A8%E7%9A%84%E5%90%8E%E7%BB%AD%E6%93%8D%E4%BD%9C&tn=98010089_dg&ch=3

#mysql数据库操作
#http://www.cnblogs.com/woider/p/5926744.html
#http://www.cnblogs.com/wt11/p/6141225.html


#读取excel
    #http://www.jb51.net/article/77626.htm
#导出excel

#利用Python学习RabbitMQ消息队列
#http://www.jb51.net/article/75647.htm
#Python实现多线程HTTP下载器示例
#http://www.jb51.net/article/105255.htm
#详谈python http长连接客户端
#http://www.jb51.net/article/115917.htm
#Python进程间通信用法实例
#http://www.jb51.net/article/67270.htm
#自己使用总结Python程序代码片段
#http://www.jb51.net/article/67118.htm