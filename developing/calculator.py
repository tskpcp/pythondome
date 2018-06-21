# 计算器

import re

def check(s):
    flag=True
    if re.findall('[a-zA-Z]',s):
        print('表达式不规范')
        flag=False
    return flag
def format_string(string):
    string = string.replace('--', '+')
    string = string.replace('-+', '_')
    string = string.replace('++', '+')
    string = string.replace('+-', '-')
    string = string.replace('*+', '*')
    string = string.replace('/+', '/')
    string = string.replace('+*', '*')
    string = string.replace('+/', '/')
    return string

def mul_div(expression):
    # 定义正则表达式可以匹配到类似'x*y' / 'x/y'
    mul_div_regular = '\d+\.?\d*[*/]\d+\.?\d*'
    # 得到匹配到的第一个符合的表达式字符段
    ret = re.search(mul_div_regular, expression)
    # 这里判断是否找到乘除表达式了，如果匹配为空，直接返回这个表达式进行加减运算就可以了
    if not ret:
        return expression
    # 如果不为空就说明匹配到了，就开始运算
    else:
        # 获得这个字符串
        ret1 = ret.group()
        # 判断是否有/
        if len(ret1.split('/')) > 1:
            x, y = ret1.split('/')
            result = float(x) / float(y)
        # 判断是否有*
        if len(ret1.split('*')) > 1:
            x, y = ret1.split('*')
            result = float(x) * float(y)
        # 没有的话直接pass就行了，就会剩加减到下个函数运行
        else:
            pass
        # 得到的浮点型要强制转换字符串
        result1 = str(result)
        # 这里是用字符串结果替换刚找到的这个表达式块例如（x*y）
        re_expr = re.sub(mul_div_regular, result1, expression, count=1)
        # 上面是运算了一小块，这里是不断调用乘除运算并且每次调用都会格式化表达式，直到表达式没有乘除符号了就返回这个括号内表达式的结果了
        fina_expr = mul_div(format_string(re_expr))
        return fina_expr


def add_sub(expression):
    add_sub_regular = '\-?\d+\.?\d*[\+\-]\d+\.?\d*'
    ret = re.search(add_sub_regular, expression)
    if not ret:
        return expression
    else:
        ret1 = ret.group()
        if len(ret1.split('+')) > 1:
            x, y = ret1.split('+')
            result = float(x)+float(y)
        else:
            x, y = ret1.split('-')
            result = float(x) - float(y)
        result1 = str(result)
        re_expr = re.sub(add_sub_regular, result1, expression, count=1)
        fina_expr = add_sub(format_string(re_expr))
        return fina_expr

if __name__ == '__main__':
    source = input('请输入表达式(退出q):')
    # 检查是否有字母
    if check(source):
        # 去空格去一次就够了
        source = source.replace(' ', '')
        # 格式化 具体看上面format_string()函数
        source = format_string(source)
        print('表达式:', source)
        # 进入while循环，只要有括号，就一直在这个循环里运行
        while source.count('(') > 0:
            # 寻找第一个最内层括号以字符串的格式获取
            strs = re.search('\([^()]+\)', source).group()
            # 运行第一个括号内的乘除得到返回值
            replace_str = mul_div(strs)
            # 运行此括号内的加减并得到返回值
            replace_str = add_sub(replace_str)
            # 得到字符串是结果和括号，去掉括号并在整体表达式中用结果替换原先的内容 到这里相当于运算了一个括号里的表达式并用结果替代了原先的位置
            source = format_string(source.replace(strs, replace_str[1:-1]))
            # 然后上去继续判断是否还有括号，有括号就继续，直到剩下没有括号的表达式运行else
        else:
            #没有括号的表达式直接先乘除运算后加减运算
            replace_str = mul_div(source)

            replace_str = add_sub(replace_str)
            print(replace_str)
