# getter and setter to access private attribute

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self.age

    # setter
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s is playing dota2' % self._name)
        else:
            print('%s is playing chess' % self._name)


def main():
    person = Person('jake', 12)
    person.play()
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()
