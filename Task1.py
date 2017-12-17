"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""


# 不收集重复的电话号码
def append_or_not(num):
    if num not in diff_num:
        diff_num.append(num)

diff_num = []
for text in texts:
    append_or_not(text[0])
    append_or_not(text[1])

for call in calls:
    append_or_not(call[0])
    append_or_not(call[1])

message = "There are {} different telephone numbers in the records."
print(message.format(len(diff_num)))
