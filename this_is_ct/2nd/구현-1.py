# Ch 4. - 실전문제 3. 게임 개발

# N * M의 직사각형에서 1은 바다고 0은 육지
# 캐릭터는 (A, B) 칸에서 북/동/남/서 방향을 바라보고 있
# 현재 위치에서 왼쪽부터 차례대로 갈 방향을 정하는데, 가보지 않은 칸이 있다면 돌아서 전진하고 가본 칸이라면 회전만 하는 것을 반복한다
# 네 방향 모두 가본 칸이거나 바다로 되어 있으면 한 칸 뒤로 가서 위의 방법을 반복한다
# 만약 뒤쪽 방향이 바다라면 움직임을 멈춘다

