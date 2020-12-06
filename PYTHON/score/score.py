def total(student):
    return sum(student[1:])    

def ave(student): 
    return student[4]/3

def grade(student):
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

def output(student):
    for x in student:
        print(x, end=" ")
    print()

def max_student(*student):
    m=0
    for x in student:
        if x[5] > m:
            m=x[5]
            n=x
    return n