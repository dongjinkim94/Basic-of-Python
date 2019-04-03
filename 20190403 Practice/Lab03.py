# 20190403 Lab03
# 문자열을 받아서 모음을 전부 없애는 코드는 다음과 같이 작성할 수 있다.(모음:aeiou AEIOU)
import string

noString = 'aeiouAEIOU'
ans = ''
inputstr = input("문자열을 입력하시오: ")
for i in inputstr:
    if i not in noString:
        ans += i
print(ans)



