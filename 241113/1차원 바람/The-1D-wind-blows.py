# 변수 선언 및 입력
n, t = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# 포인터 초기화 (리스트의 첫 번째 요소를 가리킴)
l_ptr, r_ptr, d_ptr = 0, 0, 0

for _ in range(t):
    # Step 1: 현재 포인터가 가리키는 값을 통해 각 리스트의 가장 마지막 값을 가져옵니다.
    temp_l = l[(l_ptr + n - 1) % n]
    temp_r = r[(r_ptr + n - 1) % n]
    temp_d = d[(d_ptr + n - 1) % n]

    # Step 2: 왼쪽 벨트에서 한 칸 이동
    l_ptr = (l_ptr - 1) % n
    l[l_ptr] = temp_d  # d의 마지막 값을 l의 처음 위치에 설정
    
    # Step 3: 오른쪽 벨트에서 한 칸 이동
    r_ptr = (r_ptr - 1) % n
    r[r_ptr] = temp_l  # l의 마지막 값을 r의 처음 위치에 설정
    
    # Step 4: 아래 벨트에서 한 칸 이동
    d_ptr = (d_ptr - 1) % n
    d[d_ptr] = temp_r  # r의 마지막 값을 d의 처음 위치에 설정

# 출력
# 포인터 위치를 기준으로 실제 값 순서에 맞춰 출력
print(" ".join(str(l[(l_ptr + i) % n]) for i in range(n)))
print(" ".join(str(r[(r_ptr + i) % n]) for i in range(n)))
print(" ".join(str(d[(d_ptr + i) % n]) for i in range(n)))