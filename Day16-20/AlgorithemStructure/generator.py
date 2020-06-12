prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
scores = [[0] * len(courses) for _ in range(len(names))]
print(scores)

for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'type the {course} of {name} : '))
    print(scores)
