import re

f = open("address-material.txt", 'rt', encoding="utf-8")
contents = f.readlines()
f.close()
email_list = []
for line in contents:
    matchedList = re.findall(r'[\d\.-]+@qq.com', line)
    if matchedList:
        email_list.extend(matchedList)
f = open("email.txt", "wt")
for email in email_list:
    f.write(email+"\n")
f.close()


