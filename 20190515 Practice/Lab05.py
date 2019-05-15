# 20190515 Lab05
# CSV 파일 분석
# CSV 파일 split() 메소드를 이용하여 파싱 될 수 있다.
# open(), realines(), strip() 메소드를 사용하여서 다음과 같은 CSV 파일에서
# 데이터를 읽는 프로그램을 작성하여 보자.
# open(): 파일열기, readlines(): 파일에서 한 줄씩 가져오기
# string.strip(): 문자열 양쪽 공백 제거

fname = open('Lab05_students.csv')
for line in fname:
    print(line.strip())
    words = line.strip().split(',')
    for word in words:
        print(word)