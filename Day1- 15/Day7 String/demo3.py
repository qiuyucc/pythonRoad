# def for get file's postfix


def get_postfix(filename):
    """

    :param filename:
    :return: filename's postfix
    """

    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos + 1
        return filename[index:]
    else:
        return ' '


if __name__ == '__main__':
    filename = input('Type your file name: ')
    print(get_postfix(filename))
