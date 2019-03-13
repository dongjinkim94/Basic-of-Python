# 20190313 프로그래밍 입문
# 별 도착 시간 계산
# 지구에서 가장 가까운 별은 프록시마 켄타우리(Proxima Centauri) 별이라고 한다.
# 프록시마 켄타우리는 지ㄹ구로부터 (40 X 10^12 Km) 떨어져 있다고 한다.
# 빛의 속도 (3 X 10^8 m/s)로 프록시마 켄타우리까지 간다면 시간이 얼마나 걸리는지 직접 계산해보기로 하자.

speedOfLight = 3 * 10 ** 5
distance = 40 * 10 ** 12

totalTime = speedOfLight / distance * 3600 * 24 * 365
print(totalTime)
