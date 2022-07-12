# 1분 딘위
# X + T <= M .. limit
# X - R .. 만약 휴식을 선택한 경우
# m < X - R
# 운동을 N분
# minimum value

N, m, M, T, R = map(int, input().split())

current_m = m
# if 5 70 120 25 15
# 5 < X < 70

# for exercise
# pseudo-code
# 5분간 시행

for i in range(1, N+1):
    print(f'{i}번째 실행')
    if (current_m < m):
        current_m = m
    elif (current_m > M):
        continue
    else:
        current_m - R
    current_m += T
    print(current_m)
