import re

f = open("address-material.txt", 'rt', encoding="utf-8")
contents = f.readlines()
f.close()

p = re.compile(r'[\d\.-]+@qq.com')

email_list = []
for line in contents:
    matchedList = re.finditer(p, line)
    if matchedList:
        email_list.extend(matchedList)
f = open("email.txt", "wt")
for ite in email_list:
    email = ite.group()
    f.write(email + "\n")
f.close()


