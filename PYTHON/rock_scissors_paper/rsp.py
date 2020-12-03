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
            #imgFile = "C:\\Users\\Haejun\\Desktop\\GitHub\\First_in_hufs\\PYTHON\\rock_scissors_paper\\rsp_image\\가위.png"
            imgFile = "https://github.com/Back1ash/First_in_hufs/blob/master/PYTHON/rock_scissors_paper/rsp_image/%EA%B0%80%EC%9C%84.png"
        elif cp_pick == "바위":
            imgFile = "C:\\Users\\Haejun\\Desktop\\GitHub\\First_in_hufs\\PYTHON\\rock_scissors_paper\\rsp_image\\바위.jpg"
        elif cp_pick == "보":
            imgFile = "C:\\Users\\Haejun\\Desktop\\GitHub\\First_in_hufs\\PYTHON\\rock_scissors_paper\\rsp_image\\보.png"
        
        img = cv2.imread(imgFile, cv2.IMREAD_COLOR)
        cv2.imshow('가위_바위_보', img)

        cv2.waitKey(500)
        cv2.destroyAllWindows()

    def bring_it_on(cp, usr):
        if cp==usr:
            print("승리")
        

    
    make_cp()
    b = input_user()
    show_cp_pick(b)
