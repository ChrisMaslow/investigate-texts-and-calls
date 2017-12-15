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
diff_num = []

#This function check is current number a differnt number.
def check_num(num):
    if num not in diff_num:
        diff_num.append(num)

for text in texts:
    check_num(text[0])
    check_num(text[1])

for call in calls:
    check_num(call[0])
    check_num(call[1])

print("There are {} different telephone numbers in the records.".format(len(diff_num)))
