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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""


# 不收集重复的电话号码
def collect_or_not(num):
    if num not in compare_list:
        compare_list.append(num)


# 收集被叫和收、发短信的电话号码
def collect_number():
    for call in calls:
        collect_or_not(call[1])

    for text in texts:
        collect_or_not(text[0])
        collect_or_not(text[1])


compare_list = []
telemkt_list = []
collect_number()

# 判断并收集疑似电话推销号码
for call in calls:
    if call[0] not in compare_list:
        if call[0] not in telemkt_list:
            telemkt_list.append(call[0])

telemkt_list = sorted(telemkt_list)
print("These numbers could be telemarketers: ")
for num in telemkt_list:
    print(num)
