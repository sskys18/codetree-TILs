def rotate_triangle_belt(n, t, left, right, bottom):
    for _ in range(t):
        # 시계 방향으로 회전
        new_left = [bottom[-1]] + left[:-1]  # bottom의 마지막 요소를 left의 맨 앞으로
        new_right = [left[-1]] + right[:-1]  # left의 마지막 요소를 right의 맨 앞으로
        new_bottom = [right[-1]] + bottom[:-1]  # right의 마지막 요소를 bottom의 맨 앞으로
        
        # 업데이트
        left, right, bottom = new_left, new_right, new_bottom
    
    # 결과 출력
    print(" ".join(map(str, left)))
    print(" ".join(map(str, right)))
    print(" ".join(map(str, bottom)))

# 입력 받기
n, t = map(int, input().split())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
bottom = list(map(int, input().split()))

# 함수 호출
rotate_triangle_belt(n, t, left, right, bottom)