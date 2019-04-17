# 20190417 Lab04
# 점수의 평균, 최고, 최저 (실습)
# 점수의 평균을 구해보자. (점수는 0과 100점 사이, 종료는 음수)
# 100점을 넘는 인원은 제외.
# 음수를 입력하면 입력 종료 및 총 인원과 평균, 최고, 최저 점수 출력

sum = 0
count = 0
scoreMax = -1
scoreMin = 101
while True:
    score =int(input("점수를 입력해주세요 (종료는 음수입력): "))
    if score < 0:
        break
    elif score >= 100:
        print("점수가 백점을 초과하였습니다.")
    else:
        scoreMax = max(scoreMax, score)
        scoreMin = min(scoreMin, score)
        count += 1
        sum += score
print("종료되었습니다.")
print("총",count,"명의 전체 평균은",sum/count,"입니다.")
print("최고점수는",scoreMax,"입니다.")
print("최저점수는",scoreMin,"입니다.")
