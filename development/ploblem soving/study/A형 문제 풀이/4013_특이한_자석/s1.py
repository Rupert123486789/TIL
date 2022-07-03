import sys
sys.stdin = open('input.txt', 'r')

def DFS(N, D):
    visited[N] = 1
    if N < 3:
        if arr[N][2] != arr[N+1][6] and visited[N+1] == 0:  # 자성이 다르고 붙어있는 자석을 방문하지 않았으면
            DFS(N+1, -1*D)                                  # 붙어있는 자석 반대 방향으로 회전

    if N > 0:
        if arr[N][6] != arr[N-1][2] and visited[N-1] == 0:  # 자성이 다르고 붙어있는 자석을 방문하지 않았으면
            DFS(N-1, -1*D)                                  # 붙어있는 자석 반대 방향으로 회전

    if D == 1:                                              # 시계 방향 회전
        arr[N] = [arr[N].pop()] + arr[N]
    else:                                                   # 반시계 방향 회전
        A = arr[N].pop(0)
        arr[N] = arr[N] + [A]


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        N, D = map(int, input().split())
        visited = [0] * 4                       # DFS 함수 밖에서 방문 배열만들기
        DFS(N-1, D)

    res = 0
    for i in range(4):                          # 점수 계산
        res += arr[i][0] * (2 ** i)

    print(f'#{tc} {res}')


# 1. 회전 시킨다
# 2. 인접한 자석끼리 2번과 6번 자리 값을 본다
# 3. 점수 합산
# 1, 3번은 쉬움
# 2번에서 DFS를 생각하지 못함 -> DFS 연습 필요


