# slots magic

# 动态语言允许我们在程序运行时给对象绑定新的属性，或方法，当然也可以对已经绑定的新的属性或者方法
# 当然也可以对已经绑定的属性和方法进行解绑定。 但是如果我们需要限定自定义类型的对象只能绑定某些属性
# 可以通过在类中定义__slots__变量来进行限定。需要注意的是 __slots__的限定支队当前类的对象生效，
class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @age.setter
    def age(self, age):
        self._age = age

    @age.setter
    def gender(self, gender):
        self._gender = gender

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('mike', 12)
    person.play()
    person._gender = 'male'
   # print(person.gender)


if __name__ == '__main__':
    main()


# 在类中每次实例化一个对象都会生产一个字典来保存一个对象的所有的实例属性，这样非常的有用处，可以使我们任意的去设置新的属性。
#
# 每次实例化一个对象Python都会分配一个固定大小内存的字典来保存属性，如果对象很多的情况下会浪费内存空间。
#
# 可通过__slots__方法告诉python不要使用字典，而且只给一个固定集合的属性分配空间