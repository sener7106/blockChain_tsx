# 구현 유형문제
# probelm - thinking - solution
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기는 어려운 문제를 지칭합니다.

# 알고리즘은 간단, 코드가 지나칠 만큼 길어짐
# 문자열을 기준에 따라서 끊어 처리해야하는 문제
# 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제.
# 적절한 라이브러리

# 2차원 공간의 행렬 문제의 해결 등..
# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방햑벡터가 자주 활용
# ----------------------------------------#

# 가장 왼쪽 위 좌표는 (1,1).. 가장 오른쪽 아래 좌표는 (N,N)
# L, R, U, D

n = int(input())
x, y = 1, 1
plans = input().split()
# L,R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
