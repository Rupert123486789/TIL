import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations
from collections import deque

def lunch(people, stairs):
    s = []                          # 계단까지의 이동 시간

    for person in people:
        s.append(abs(person[0] - stairs[0]) + abs(person[1] - stairs[1]))

    s = deque(sorted(s))

    e = deque()                     # 계단을 내려가고 도착하는 시간

    time = 0
    cur = 0

    while s:
        time += 1

        while e and e[0] == time:   # 이동이 완료되었을 때
            e.popleft()
            cur -= 1

        while s[0] < time:
            if cur < 3:             # 계단 이동
                s.popleft()
                if not s:
                    time += arr[stairs[0]][stairs[1]]
                    break
                e.append(time + arr[stairs[0]][stairs[1]])
                cur += 1
            else:
                break
    return time

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:              # 사람
                people.append((r, c))
            elif arr[r][c] >= 2:            # 계단
                stairs.append((r, c))

    res = 987654321
    for i in range(N):
        for people1 in combinations(people, i):                                 # 완전 탐색 -> 조합 사용
            people2 = list(set(people) - set(people1))
            time = max(lunch(people1, stairs[0]), lunch(people2, stairs[1]))    # 계단은 2개
            res = min(res, time)

    print(f'#{tc} {res}')