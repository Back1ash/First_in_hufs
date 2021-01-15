import random

def rand_1char():
    words = [
        "人", "风", "花", "一", "不", "春", "无", "云", "天", "来", "月", "山", "香", "时", "年", "有", "玉", "是", "何", "如"
    ]

    num = random.randint(0,19)
    print(words[num])

rand_1char()
