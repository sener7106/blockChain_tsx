# 한번에 만들 수 있는 아이스크림의 개수를 출력합니다
# DFS 혹은 BFS로 해결할 수 있씁니다.
n, m = map(int, input().split)


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당노드 방문 처리
        graph[x][y] = 1
        # 상 하 좌 우 의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)  # 좌
        dfs(x, y - 1)  # 하
        dfs(x + 1, y)  # 우
        dfs(x, y + 1)  # 상
        return True
    return False


# 2차원 리스트의 맵 정보를 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# N x M 행렬
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
