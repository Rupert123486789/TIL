import sys
sys.stdin = open('input.txt', 'r')

def DFS(n, cost):
    global res
    # 4. 가지치기

    # 1. 종료 조건
    if n > 12:
        # 2. 정답 처리
        if res > cost:
            res = cost
        return

    # 3. 하부 함수 호출
    DFS(n+1, cost+lst[n]*day)   # 일
    DFS(n+1, cost+mon)          # 달
    DFS(n+3, cost+mon_3)        # 3달
    DFS(n+12, cost+year)        # 년
       

T = int(input())
for tc in range(1, T+1):
    day, mon, mon_3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))         # 인덱스 번호 맞추기 위해 0번째 달 추가
    res = 987654321
    DFS(1, 0)
    print(f'#{tc} {res}')
