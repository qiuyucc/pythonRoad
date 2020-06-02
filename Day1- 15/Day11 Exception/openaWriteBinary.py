def main():
    try:
        with open('../images/luffy.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('../images/ball.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('write the document went wrong')
    except IOError as e:
        print('wrong when writing')
    print('end')


if __name__ == '__main__':
    main()
