from datetime import datetime
import sys

while (1):
    menu = int(input("1. 시세 등록 | 2. 구매 등록 | 3. 처분 기록 | 4. 프로그램 종료 : "))
    path = "/log.txt"

    if menu == 1:
        print("\n\n ====  시세 등록 ==== ")
        path = "/quote.txt"
        tmp = int(input("지금 시세를 입력하세요 | 만원단위로 : "))

        with open(path, mode='at') as f:
            f.write(f'{datetime.today().strftime("%Y/%m/%d %H")} | {tmp} 만원')
        print(f'{datetime.today().strftime("%Y/%m/%d %H")} | {tmp} 만원 // 등록 완료')
    
    elif menu == 2:
        print("\n\n ====  구매 등록 ==== ")
        tmp = int(input("구매 가격을 입력하세요 | 만원단위로 : "))
        amount = int(input("몇개 구매했나요? : "))

        with open(path, mode='at') as f:
            f.write(f'{tmp}만원 | {amount}개 구매')
        print(f'{tmp} | {amount} 구매 등록 완료')
        
    elif menu == 3:
        print("\n\n ====  처분 기록 ==== ")
        tmp = int(input("판매 가격을 입력하세요 | 만원단위로 : "))
        amount = int(input("몇개 판매했나요? : "))

        with open(path, mode="at") as f:
            f.write(f'{tmp}만원 | {amount}개 판매')
        print(f'{tmp} | {amount} 판매 등록 완료')

    elif menu == 4:
        sys.exit()
    else:
        print("올바른 값을 입력하세요.")
        continue
