def rotate_belt(n, t, top, bottom):
    for _ in range(t):
        # 시계 방향으로 회전
        last_top = top[-1]
        first_bottom = bottom[0]  # 뒤집힌 상태로 처리되므로 첫 번째 요소 사용

        # 위쪽은 한 칸씩 오른쪽으로 밀림
        for i in range(n-1, 0, -1):
            top[i] = top[i-1]
        
        # 아래쪽은 한 칸씩 왼쪽으로 밀림 (이미 뒤집어져 있으므로 왼쪽 이동처럼 처리)
        for i in range(n-1):
            bottom[i] = bottom[i+1]
        
        # 회전된 값들을 갱신
        top[0] = first_bottom
        bottom[-1] = last_top

    return top, bottom

# 입력 받기
n, t = map(int, input().split())
top = list(map(int, input().split()))
bottom = list(map(int, input().split()))[::-1]  # 입력을 받을 때 바로 뒤집어서 처리

# t초 후 상태 계산
top, bottom = rotate_belt(n, t, top, bottom)

# 출력 (밑 줄은 이미 뒤집혀 있으므로 그대로 출력)
print(" ".join(map(str, top)))
print(" ".join(map(str, bottom[::-1])))  # 출력할 때는 다시 뒤집어서 출력