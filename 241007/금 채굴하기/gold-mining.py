# 입력받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 채굴에 드는 비용을 계산하는 함수
def mining_cost(k):
    return k * k + (k + 1) * (k + 1)

# 주어진 중심점 (x, y)와 반경 k에 대한 마름모 내 금의 개수를 계산하는 함수
def count_gold_in_diamond(x, y, k):
    total_gold = 0
    for i in range(-k, k + 1):
        for j in range(-(k - abs(i)), k - abs(i) + 1):
            nx, ny = x + i, y + j
            if 0 <= nx < n and 0 <= ny < n:
                total_gold += grid[nx][ny]
    return total_gold

# 최대로 얻을 수 있는 금의 개수
max_gold = 0

# 각 좌표를 중심으로 마름모 모양을 그리고, 그 안의 금의 개수를 계산
for x in range(n):
    for y in range(n):
        k = 0
        while True:
            cost = mining_cost(k)
            gold_count = count_gold_in_diamond(x, y, k)
            if cost > gold_count * m:
                break
            max_gold = max(max_gold, gold_count)
            k += 1

# 결과 출력
print(max_gold)