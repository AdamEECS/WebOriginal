# 2016/8/28
#
# ========
# 作业 (待更新)
#
# 注意, 登录论坛后才有评论功能
# ========
#

'''
9.1
我们现在使用的数据存储文件格式如下
[
    {
        "note": "吃瓜",
        "username": "gua",
        "id": 1,
        "password": "123"
    },
    {
        "note": "note",
        "username": "gua1",
        "id": 2,
        "password": "123"
    }
]
它是一个包含了
dict
的
list
我们要查找
id
为
n
的元素, 需要从头到尾遍历这个
list
并且比较
id
最坏的情况是
id
为
n
的这个元素根本不存在, 你需要遍历整个
list
才能得到你想要的结果
请给出一个方案, 能够非常快速地根据
id
查找到我们想要的元素
提示: 根据需求改变存储文件的结构
[
    {
        1: {
            "note": "吃瓜",
            "username": "gua",
            "id": 1,
            "password": "123"
        },
        3: {
            "note": "note",
            "username": "gua1",
            "id": 3,
            "password": "123"
        },
    }
]

9.2
通过
9.1
我们已经能够迅速找到
id
为
n
的元素了
现在的需求是我们有时候并不满足于通过
id
查找元素
比如验证用户登录的时候需要通过
username
查找元素, username
是不重复的
请给出一个方案, 让我们能够迅速通过
username
查找元素
做不出就思考一下, 等上课的内容
提示: 根据需求改变存储文件的结构

# 我们做一个下面这样格式的索引字典
{
    'gua': 1,
    'gua1': 2,
}
'''
