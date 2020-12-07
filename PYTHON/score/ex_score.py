from score import *

ban = [] #student 리스트를 요소로 받을 리스트 선언 

for x in range(5):
    student = []    #student 빈 리스트 선언
    student.append(input("성명 : "))    #빈 리스트이므로 append(변수)를 할 시 student[0]번 인덱스에 들어가게 된다.
    student.append(int(input("국어점수 : ")))   #0번 인덱스가 차 있으므로 1번 인덱스에 추가된다
    student.append(int(input("영어점수 : ")))   #1번 인덱스가 차 있으므로 2번 인덱스에 추가된다.
    student.append(int(input("수학점수 : ")))   #2번 인덱스가 차 있으므로 3번 인덱스에 추가된다.   
    ban.append(student)        #국어 영어 수학 점수를 채운 리스트를 ban에 리스트 상태로 넣는다.

for i in ban:
    i.append(total(i)) #ban에 있는 student 하나씩 꺼내와서 총점 추가
    i.append(ave(i))#ban에 있는 student 하나씩 꺼내와서 평균 추가
    i.append(grade(i))#ban에 있는 student 하나씩 꺼내와서 학점 추가
    print(f'{i[0]} : 국어:{i[1]} 영어:{i[2]} 수학:{i[3]} 총점:{i[4]} 평균:{i[5]} 학점:{i[6]}')

print(f'2명 성적 비교하여 더 좋은 점수의 학생 찾기')
print(f'{ban[2][0]} : 국어:{ban[2][1]} 영어:{ban[2][2]} 수학:{ban[2][3]} 총점:{ban[2][4]} 평균:{ban[2][5]} 학점:{ban[2][6]}')
print(f'{ban[4][0]} : 국어:{ban[4][1]} 영어:{ban[4][3]} 수학:{ban[4][3]} 총점:{ban[4][4]} 평균:{ban[4][5]} 학점:{ban[4][6]}')

m_stu = max_student(ban[2], ban[4])
print("성적이 더 좋은 학생")
print(f'{m_stu[0]} : 국어:{m_stu[1]} 영어:{m_stu[2]} 수학:{m_stu[3]} 총점:{m_stu[4]} 평균:{m_stu[5]} 학점:{m_stu[6]}')

print(f'3명 성적 비교하여 더 좋은 점수의 학생 찾기')
print(f'{ban[1][0]} : 국어:{ban[1][1]} 영어:{ban[1][2]} 수학:{ban[1][3]} 총점:{ban[1][4]} 평균:{ban[1][5]} 학점:{ban[1][6]}')
print(f'{ban[2][0]} : 국어:{ban[2][1]} 영어:{ban[2][2]} 수학:{ban[2][3]} 총점:{ban[2][4]} 평균:{ban[2][5]} 학점:{ban[2][6]}')
print(f'{ban[3][0]} : 국어:{ban[3][1]} 영어:{ban[3][2]} 수학:{ban[3][3]} 총점:{ban[3][4]} 평균:{ban[3][5]} 학점:{ban[3][6]}')

m_stu = max_student(ban[1], ban[2], ban[3])
print("성적이 가장 좋은 학생")
print(f'{m_stu[0]} : 국어:{m_stu[1]} 영어:{m_stu[3]} 수학:{m_stu[3]} 총점:{m_stu[4]} 평균:{m_stu[5]} 학점:{m_stu[6]}')


