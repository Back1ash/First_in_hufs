def chicken100():
    print("百鸡问题:")

    fa_chick, ma_chick, chick = list(range(101)), list(range(101)), list(range(101))
    for i in fa_chick:
        for j in ma_chick:
            for x in chick:
                if 5*i + 2*j + x/3 == 100 and i+j+x == 100:
                    print(f"公鸡 : {i}, 母鸡 : {j}, 鸡 : {x}")
    

chicken100()
