import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    day, mon, mon_3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))     # 인덱스 번호 맞추기 위해 0번째 달 추가

    D = [0] * 13                                    # DP 테이블
    # 어느 시점까지의 최솟값을 계속 구해 나감
    for i in range(1, 13):
        D[i] = D[i-1] + lst[i]*day                  # 일
        D[i] = min(D[i], D[i-1] + mon)              # 월
        if i >= 3:                                  # 3달
            D[i] = min(D[i], D[i-3] + mon_3)
        if i >= 12:                                 # 년
            D[i] = min(D[i], D[i-12] + year)

    print(f'#{tc} {D[12]}')
