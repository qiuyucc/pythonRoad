# range of index apply to list in python
def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # for loop check all the fruits

    for fruit in fruits:
        print(fruit.title(), end='')

    print()

    # range of index
    fruits2 = fruits[1:4]
    print(fruits2)

    # fruites = fruits #just create a new variable refer to fruits, not copy
    # copy the list :
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)

    # reverse the list
    fruits5 = fruits[::-1]
    print(fruits5)


if __name__ == '__main__':
    main()
