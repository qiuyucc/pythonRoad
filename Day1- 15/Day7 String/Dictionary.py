# Dictionary Like map in java
# key - value pair

def main():
    scores = {'brook': 98, 'james': 39, 'mike': 85}
    # get value from key
    print(scores['brook'])
    print(scores['james'])
    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    # update dictionary element
    scores['james'] = 65
    scores['mike'] = 72
    scores.update(hello=59, kobe=71)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    # get方法也是通过键获取对应的值但是可以设置默认值

    print(scores.get('武则天', 60))
    print(scores)
    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))
    print(scores)
    # 清空字典
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
