import cv2
import random

class rsp:
    def make_cp(): #컴퓨터 가위바위보 선택. cp_pick이 변수명으로 더 나았을듯
        rsp_list = ["가위", "바위", "보"]
        return random.choice(rsp_list)
    
    def input_user(): #유저한테 가위바위보 중 하나 받기
        while(1):   #무한 반복문으로 셋 중 하나만 입력하도록 만듦
            a = input("가위, 바위, 보 중 하나만 내세요 : ")
            if a != "가위" and a != "바위" and a != "보":
                print("올바른 걸로 다시 입력하세요.")
            else:
                break
        return a
    def show_cp_pick(cp_pick):  #컴퓨터가 선택한 것 이미지로 화면에 띄우기
        if cp_pick == "가위":
            imgFile = "C:\\Users\\Haejun\\Desktop\\GitHub\\First_in_hufs\\PYTHON\\rock_scissors_paper\\rsp_image\\scissor.png"
        elif cp_pick == "바위":
            imgFile = "C:\\Users\\Haejun\\Desktop\\GitHub\\First_in_hufs\\PYTHON\\rock_scissors_paper\\rsp_image\\rock.jpg"
        elif cp_pick == "보":
            imgFile = "C:\\Users\\Haejun\\Desktop\\GitHub\\First_in_hufs\\PYTHON\\rock_scissors_paper\\rsp_image\\paper.png"
        
        img = cv2.imread(imgFile, cv2.IMREAD_COLOR)     #경로의 이미지 출력옵션 선택
        cv2.imshow('가위_바위_보', img)                 #이미지 출력

        cv2.waitKey(5000)                   #5초동안
        cv2.destroyAllWindows()             #그 이후 자동 창 닫힘

    def bring_it_on(cp, usr):               #승패를 가르는 함수
        if cp==usr:
            print("무승부")
        elif (cp=="가위" and usr=="바위") | (cp=="바위" and usr=="보") | (cp=="보" and usr=="가위"):
            print("승리")
        else:
            print("패배")
        
    cp = make_cp()
    b = input_user()
    show_cp_pick(cp)
    bring_it_on(cp, b)
