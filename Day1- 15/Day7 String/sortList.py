# sort list

def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    #默认就是按照字母顺序排列
    list2 = sorted(list1)

    # sorted 函数不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)

    list1.sort(reverse=True)
    print(list1)


if __name__ == '__main__':
    main()
