# Python中的集合肯定不能够支持索引运算。另外，集合的互异性决定了集合中不能有重复元素，这一点也是集合区别于列表的关键，说得更直白一些就是，Python中的集合类型具有去重特性。
# 当然，Python中的集合一定是支持in和not in成员运算的，这样就可以确定一个元素是否属于集合，也就是上面所说的集合的确定性。集合的成员运算在性能上要优于列表的成员运算
set1 = {1, 2, 3, 3, 2, 3, 2}
print(set1)
print(len(set1))
# No repeat number in the set

# 创造集合的构造器与哇
set2 = set('hello')
print(set2)

set2 = set('hello')
print(set2)
# 将列表转换成集合(可以去掉列表中的重复元素)
set3 = set([1, 2, 3, 3, 2, 1])
print(set3)

# 创建set的生成方法， 将【】 换成{}
set4 = {num for num in range(1, 20) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 集合元素的便利
for elem in set4:
    print(elem)

# 集合的运算

# in not in
set1 = {11, 12, 13, 14, 15}
print(10 in set1)
print(14 in set2)
print(16 not in set2)
set2 = {'Python', 'Java', 'Go', 'Swift'}
print('Ruby' in set2)  # False
print('Java' in set2)  # True

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
# 方法一: 使用 & 运算符
print(set1 & set2)  # {2, 4, 6}
# 方法二: 使用intersection方法
print(set1.intersection(set2))  # {2, 4, 6}

# 并集
# 方法一: 使用 | 运算符
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 方法二: 使用union方法
print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
# 方法一: 使用 - 运算符
print(set1 - set2)  # {1, 3, 5, 7}
# 方法二: 使用difference方法
print(set1.difference(set2))  # {1, 3, 5, 7}

# 对称差
# 方法一: 使用 ^ 运算符
print(set1 ^ set2)  # {1, 3, 5, 7, 8, 10}
# 方法二: 使用symmetric_difference方法
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}
# 方法三: 对称差相当于两个集合的并集减去交集
print((set1 | set2) - (set1 & set2))  # {1, 3, 5, 7, 8, 10}

set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = set2

print(set1 < set2, set1 <= set2)
print(set2 < set3, set2 <= set3)
print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set2 > set1)

# 创建一个空集合
set1 = set()
# 通过add方法添加元素
set1.add(33)
set1.add(55)
set1.update({1, 10, 100, 1000})
print(set1)  # {33, 1, 100, 55, 1000, 10}
set1.discard(100)
set1.discard(99)
print(set1)
# 通过remove方法删除指定元素，建议先
if 10 in set1:
    set1.remove(10)
print(set1)
# remove specific elements
if 10 in set1:
    set1.remove(10)
print(set1)

# pop method to delete a element and return it
print(set1.pop())
set1.clear()
print(set1)

# judge two collections have same elements
set1 = {'Java', 'Python', 'Go', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Objective-C', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # True
print(set1.isdisjoint(set3))  # False

# 不可变合集
set1 = frozenset({1, 3, 5, 7})
set2 = frozenset(range(1, 6))
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set1 < set2)
