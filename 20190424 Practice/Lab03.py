# 20190424 Lab03
# 성적 처리 프로그램
# 학생들의 성적을 처리하는 프로그램을 완성시켜보자.
# 사용자로부터 성적을 입력받아서 리스트에 저장한다.
# 성적의 평균을 구하고 80점 이상 성적을 받은학생의 숫자를 계산하여 출력해보자.

scores=[]
count = 0
sum = 0
students = int(input("몇 명의 학생 점수를 입력할 건가요? "))
for i in range(students):
    scores.append(int(input("성적을 입력하시요: ")))
    sum += scores[i]
    if scores[i]>=80:
        count += 1
scoreAvg = sum / students

print("80점 이상 성적을 받은 학생은",count,"명 입니다.")
print(scores)