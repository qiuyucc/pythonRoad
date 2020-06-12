#在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典

stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

stocks2 = {key: value for key, value in stocks.items() if value>100}
print(stocks2)

