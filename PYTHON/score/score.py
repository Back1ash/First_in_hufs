def total(student):
    return sum(student[1:])    #각 점수 더한 값 리턴

def ave(student): 
    return student[4]/3         #총점을 3으로 나눠 리턴(평균)

def grade(student):             #평균점수에 따라 학점 부여
    if student[5] >= 90:
        return "A"
    elif student[5] >= 80:
        return "B"
    elif student[5] >= 70:
        return "C"
    elif student[5] >= 60:
        return "D"
    else:
        return "F"

def output(student):        # 출력 메소드 (수정요함)
    for x in student:
        print(x, end=" ")
    print()

def max_student(*student):  #평균이 제일 높은 학생 리턴하는 메소드
    m=0
    for x in student:
        if x[5] > m:
            m=x[5]
            n=x
    return n