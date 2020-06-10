xinhua = {
    '麓': '山脚下', '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名', '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号',
    'home': '中同仁路8号', 'tel': '13122334455', 'econtact': '13800998877'
}
print(person)

## dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='王大锤', age=55, weight=60, home='中同仁路8号')
print(person)  # {'name': '王大锤', 'age': 55, 'weight': 60, 'home': '中同仁路8号'}

# 可以通过Python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)

# 用字典生成法
item3 = {x: x ** 3 for x in range(1, 6)}
print(item3)

print(len(person))
for key in person:
    print(key)

# 字典的运算
# 对于字典类型来说，成员运算和索引运算肯定是最为重要的，前者可以判定指定的键在不在字典中，后者可以通过键获取对应的值或者向字典中加入新的键值对。
# 值得注意的是，字典的索引不同于列表的索引，列表中的元素因为有属于自己有序号，所以列表的索引是一个整数；字典中因为保存的是键值对，
# 所以字典的索引是键值对中的键，通过索引操作可以修改原来的值或者向字典中存入新的键值对。
# 需要特别提醒大家注意的是，字典中的键必须是不可变类型，例如整数（int）、浮点数（float）、字符串（str）、元组（tuple）等类型的值；

print('name' in person, 'tel' in person)
# change the age in dic to 25
if 'age' in person:
    person['age'] = 25
# 通过索引操作想person字典中存入新的键值对
person['tel'] = '13122334455'
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去赢取你的闺蜜'
print('name' in person, 'tel' in person)
# check key in person
print(len(person))

for key in person:
    print(f'{key}: {person[key]}')

# 字典的方法
# 字典中的值又是一个字典(嵌套的字典)
students = {
    1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
    1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
}

# 使用get方法通过键获取对应的值，如果取不到不会引发KeyError异常而是返回None或设定的默认值
print(students.get(1002))
print(students.get(1005))  # None
print(students.get(1005, {'name': 'no-name'}))

# 获取字典中所有的键
print(students.keys())      # dict_keys([1001, 1002, 1003])
# 获取字典中所有的值
print(students.values())    # dict_values([{...}, {...}, {...}])
# 获取字典中所有的键值对
print(students.items())     # dict_items([(1001, {...}), (1002, {....}), (1003, {...})])
# 对字典中所有的键值对进行循环遍历
for key, value in students.items():
    print(key, '--->', value)

# 使用pop方法通过键删除对应的键值对并返回该值
stu1 = students.pop(1002)
print(stu1)             # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print(len(students))    # 2
# stu2 = students.pop(1005)    # KeyError: 1005
stu2 = students.pop(1005, {})
print(stu2)             # {}

# 使用popitem方法删除字典中最后一组键值对并返回对应的二元组
# 如果字典中没有元素，调用该方法将引发KeyError异常
key, value = students.popitem()
print(key, value)    # 1003 {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}

# setdefault可以更新字典中的键对应的值或向字典中存入新的键值对
# setdefault方法的第一个参数是键，第二个参数是键对应的值
# 如果这个键在字典中存在，更新这个键之后会返回原来与这个键对应的值
# 如果这个键在字典中不存在，方法将返回第二个参数的值，默认为None
result = students.setdefault(1005, {'name': '方启鹤', 'sex': True})
print(result)        # {'name': '方启鹤', 'sex': True}
print(students)      # {1001: {...}, 1005: {...}}

#del key word
del person['age']
print(person)