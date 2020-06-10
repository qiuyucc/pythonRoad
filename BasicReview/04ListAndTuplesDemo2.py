'''
计算指定年月日时这一年的第几天
'''


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """计算传入的日期是这一年的第几天
       :param year: 年
       :param month: 月
       :param date: 日
       """
    # 用嵌套的列表保存平年和闰年每个月的天数
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]

    # boolean Fasle =0, True =1
    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days[index]
    return total + date


print(which_day(1980, 11, 28))  # 333
print(which_day(1981, 12, 31))  # 365
print(which_day(2018, 1, 1))  # 1
print(which_day(2016, 3, 1))  # 61
