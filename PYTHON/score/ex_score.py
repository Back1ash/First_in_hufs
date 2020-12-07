from score import *

ban = []

for x in range(5):
    student = []
    student.append(input("성명 : "))
    student.append(int(input("국어점수 : ")))
    student.append(int(input("영어점수 : ")))
    student.append(int(input("수학점수 : ")))
    ban.append(student)

for i in ban:
    i.append(total(i))
    i.append(ave(i))
    i.append(grade(i))
    print(f'{i[0]} : 국어:{i[1]} 영어:{i[2]} 수학:{i[3]} 총점:{i[4]} 평균:{i[5]} 학점:{i[6]}')

print(f'2명 성적 비교하여 더 좋은 점수의 학생 찾기')
print(f'{ban[2][0]} : 국어:{ban[2][1]} 영어:{ban[2][2]} 수학:{ban[2][3]} 총점:{ban[2][4]} 평균:{ban[2][5]} 학점:{ban[2][6]}')
print(f'{ban[4][0]} : 국어:{ban[4][1]} 영어:{ban[4][3]} 수학:{ban[4][3]} 총점:{ban[4][4]} 평균:{ban[4][5]} 학점:{ban[4][6]}')

m_stu = max_student(ban[2], ban[4])
print("성적이 더 좋은 학생")
print(f'{m_stu[0]} : 국어:{m_stu[1]} 영어:{m_stu[3]} 수학:{m_stu[3]} 총점:{m_stu[4]} 평균:{m_stu[5]} 학점:{m_stu[6]}')

print(f'3명 성적 비교하여 더 좋은 점수의 학생 찾기')
print(f'{ban[1][0]} : 국어:{ban[1][1]} 영어:{ban[1][2]} 수학:{ban[1][3]} 총점:{ban[1][4]} 평균:{ban[1][5]} 학점:{ban[1][6]}')
print(f'{ban[2][0]} : 국어:{ban[2][1]} 영어:{ban[2][2]} 수학:{ban[2][3]} 총점:{ban[2][4]} 평균:{ban[2][5]} 학점:{ban[2][6]}')
print(f'{ban[3][0]} : 국어:{ban[3][1]} 영어:{ban[3][2]} 수학:{ban[3][3]} 총점:{ban[3][4]} 평균:{ban[3][5]} 학점:{ban[3][6]}')

m_stu = max_student(ban[1], ban[2], ban[3])
print("성적이 가장 좋은 학생")
print(f'{m_stu[0]} : 국어:{m_stu[1]} 영어:{m_stu[3]} 수학:{m_stu[3]} 총점:{m_stu[4]} 평균:{m_stu[5]} 학점:{m_stu[6]}')


