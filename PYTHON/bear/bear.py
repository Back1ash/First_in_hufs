import random
import time

monster =  '''
:::d(d(o<:::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::d88888P::::::::::::::::::::::::::::::::::::::::::::::::>o)b)b:::
::988888b::?:::::::::::::::::::::::::::::::::::::::::::::988888b::
::o888888bd8):::::::::::::::::::::::::::::::::::::::::6::d88888P::
:::98888888P:::::::::::::::::A:::::::~~~~~::::4::::::(8bd888888o::
::::988888):::::::::::::::::`8bo...d8888888b::i8::::::98888888P:::
:::::988888.::::::::::::::::::"88p888{-0=_\_0.8P::::::::(88888P:::
::::::'88888b::::::::::::::::::`},%:{\  (\./)8":::::::::'8888i::::
:::::::9888888b:::::::::::::::,;%%%:::./V^^^V\::::::::::888888;.::
::::::::988888P `::..,,;;;;,-######'_..\A   A/:::::::::(8888888;::
::::::::(88888'..``'    8888oooooo.:::\`9^^^P`,~--._::::9888P;;)::
::::::::::988P `` .      oo.8888888888:`(((:o.ooo8888Oo; ; '  ':::
:::::::::::`-..   `        `o`88888888b`:)):888b88888P""'     ;:::
:::::::::::::::"`--_`.       b`888888888;(.,"888b888"  ..  ;-'::::
:::::::::::::::::::::~"-....   b`8888888     .`8888. . ,,;''::::::
:::::::::::::::::::::::::`   . `    OOO       .`OO' ,,;'':::::::::
:::::::::::::::::::::::::::`.      "``      ''    ,'::::::::::::::
'''
print('\nBear attack ver.1')
time.sleep(1)
print('\n스산한 바람에 안개비 부슬부슬 내리는 늦은 가을밤!!!\n')
time.sleep(1)
print('\n과제 준비로 늦은 밤, 88계단 앞을 지나던 당신과 친구,\n')
time.sleep(0.5)
print('부스럭~ 부스럭~\n')
time.sleep(0.5)
print('어둡고 커다란 물체가 갑자기 . . .\n')
time.sleep(1)
print(monster)
time.sleep(1)
print('\n\n으악! 커다란 송곳니! 굵직한 앞발에 날카로운 발톱! 곰인가?\n\n')
time.sleep(0.5)
print('여긴 어디? 나는 누구?')
time.sleep(0.5)
print('아니지, 얘는 누구?')
time.sleep(0.5)
for i in range(3):
    print('.', end = '')
    time.sleep (0.5)
print('\n를 생각해 볼 겨를도 없이 덮쳐오는 거대한 그림자!')


userselect = ''
while userselect !='1' and userselect != '2':
    print('도망갈까요? (1), or 싸울까요? (2)\n')
    userselect = input()

    if userselect =='1':
        print('야 튀어 ~', end = '')
        runawaysituation = random.randint(0,1)
        if runawaysituation == 1:
            time.sleep(0.5)
            print('라는 말보다 빨리 달려나간 당신!!!', end ='')
            time.sleep(1.5)
            print('을 쫓아오는 곰!!!')
            for i in range(3):
                print('.')
                time.sleep(0.5)
            print('당신은 무사히 도망친 것 같습니다! 휴~~~\n')
            time.sleep(1)
            print('친구는???\n')
            time.sleep(0.5)
            print('')
            print('뒤를 돌아보니 엥~, 곰이 친구에게 재롱 부리고 있네요.')
        else:
            time.sleep(0.5)
            print('라는 말보다 빨리 달려나갔다고 생각했는데...')
            time.sleep(1)
            print('친구는 이미 저 멀리 앞서 뛰어가고 있네요')
            time.sleep(0.5)
            print('육상부 출신이었던 거야??! oO;')
            time.sleep(0.5)
            print('으악!!! 등 뒤에서 들려오는 거친 숨소리 . . .')
            print('')
            time.sleep(0.5)
            print('제발 저리 가라! 저리 가!')
            time.sleep(0.5)
            print('안 되겠다. 죽은 척이라도 .. 곰이 부디 배고프지 않길 .. ㅜㅜ;\n')
            time.sleep(0.5)
            print('다가온 곰이 일으켜 세우며 말하길 "왜 소릴지르는거야! 나도 놀랬잖아."\n')
            print('펭수따라 한국에 온 꼼수라고!!!')

#시나리오 2
    else:
        print('''"그래 결심했어! 한 번 해 보는거야!"
마음 먹은 당신... 주변을 둘러봅니다.''')
        time.sleep(0.5)
        print('\n☆★☆ 획득 ☆★☆ 몽둥이를 얻었습니다.')
        time.sleep(0.5)
        print('친구는? ... 어느 새 칼에 갑옷까지!')
        time.sleep(0.5)
        print('뭔가 현질의 냄새가 물씬 . . . --;')
        time.sleep(0.5)
        print('\n어쨌거나 준비성 좋은 친구와 당신은 7번의 공격 안에 공을 물리쳐야 합니다.')
        time.sleep(0.5)
        print('지금부터 공격!!!\n')

        def attack():
            bearstamina = 100
            attackcount = 1
            while attackcount<=7 and bearstamina>=0 :
                myhitpoint = random.randint(0, 9)
                friendhitpoint= random.randint(0,9)
                
                print('☆★☆'+ str(attackcount)+ '차 공격 개시 ☆★☆')
                print('친구와 공격 합을 잘 맞추면 콤보 공격(공격 포인트 합 + 10)이 됩니다.')
                comboattack = str(random.randint(1,3))
                
                if input("어디를 공격할까요? 머리(1),몸통(2),다리(3) '1~3'중 한가지만 고르세요.\n")==comboattack:
                        bearstamina= bearstamina - (myhitpoint+friendhitpoint+10)
                        print('☆★☆ 콤보 공격 성공 ☆★☆\n')
                        print('친구와 환상 콤비! 콤보 공격 성공!!' + str(myhitpoint) + '+' + str(friendhitpoint)+"+"+ '10'+'의 피해를 입혔습니다.')
                        print('곰의 남은 체력은'+ str(bearstamina)+'입니다.\n\n')
                else:
                        bearstamina = bearstamina - (myhitpoint+friendhitpoint)
                        print('당신은 공격으로'+ str(myhitpoint)+'의 피해를 입혔습니다.')
                        print('친구는 공격으로'+ str(friendhitpoint)+'의 피해를 입혔습니다.')
                        print('곰의 남은 체력은'+ str(bearstamina)+'입니다.\n\n')
            return bearstamina

        bearstamina=attack()    
        
        if bearstamina<=0:
                print('☆★☆ 승리 ☆★☆ 웅담 포션과 곰발바닥 x 2 을 얻었습니다.\n')
                print('이 참에 나도 곰가죽 갑옷을 한 벌 마련해볼까나~~!')

        else:
                print('아아악! 갑옷입은 친구와 호흡이 안 맞더라....ㅜ')
                

