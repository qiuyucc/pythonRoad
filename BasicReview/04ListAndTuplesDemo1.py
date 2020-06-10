# 成绩表和平均分


"""
录入5个学生3门课程的考试成绩
计算每个学生的平均分和每门课的平均分

Version: 0.1
Author: QIUYU
"""

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 用生成式创建嵌套的列表保存5个学生3门课程的成绩
scores = [[0] * len(courses) for _ in range(len(names))]
print(scores)
# 录入数据
for i, name in enumerate(names):
    print(f'请输入{name}的成绩 ===>')
    for j, course in enumerate(courses):
        scores[i][j] = float(input(f'{course}: '))
print()
print(scores)
print('-' * 5, '学生平均成绩', '-' * 5)
# 计算每个人的平均成绩
for index, name in enumerate(names):
    avg_score = sum(scores[index]) / len(courses)
    print(f'{name}的平均成绩为: {avg_score:.1f}分')
print()
print('-' * 5, '课程平均成绩', '-' * 5)
# 计算每门课的平均成绩
for index, course in enumerate(courses):
    # 用生成式从scores中取出指定的列创建新列表
    curr_course_scores = [score[index] for score in scores]

    avg_score = sum(curr_course_scores) / len(names)
    print(f'{course}的平均成绩为：{avg_score:.1f}分')

# 使用了enumerate函数，这个函数非常有用。我们之前讲过循环遍历列表的两种方法，
# 一种是通过索引循环遍历，一种是直接遍历列表元素。通过enumerate处理后的列表在循环遍历时会取到一个二元组，解包之后第一个值是索引，第二个值是元素
items = ['Python', 'Java', 'Go', 'Swift']
for index in range(len(items)):
    print(f'{index}:{items[index]}')
for index, item in enumerate(items):
    print(f'{index}:{item}')
   