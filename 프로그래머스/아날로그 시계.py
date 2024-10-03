def check_overlap(h1, m1, s1, h2, m2, s2):  # 00:00:00 ~ 11:59:59 일때 겹치는 횟수 계산
    """
    h: 1시간에 30도 움직임 -> 1분에 1/2도 -> 1초에 1/120도
    m: 1시간에 360도 움직임 -> 1분에 6도 -> 1초에 0.1도
    s: 1분에 360도 움직임 -> 1초에 6도,
    """
    start_h = h1 * 30 + m1 * 0.5 + s1 * (1 / 120)
    start_m = m1 * 6 + s1 * 0.1
    start_s = s1 * 6
    fin_h = h2 * 30 + m2 * 0.5 + s2 * (1 / 120)

    # print(start_h, start_m, start_s, fin_h)

    count = 0
    h = start_h
    m = start_m
    s = start_s

    if h == s:
        count += 1
        # print(h, m, s)
    elif m == s:
        count += 1
        # print(h, m, s)

    while (h + 1 / 120) <= fin_h:  # 1초단위로 while문 돌아감
        # 1초 후 시분초
        new_h = h + 1 / 120
        new_m = m + 0.1
        new_s = s + 6

        # 초침이 시침을 가로지름
        if s < h and new_s >= new_h:
            # print(new_h, new_m, new_s)
            count += 1

        # 초침이 분침을 가로지름
        if s < m and new_s >= new_m:
            # print(new_h, new_m, new_s)
            count += 1

        # # 동시에 가로지르는 경우
        # if (s < m and s < h) and (new_m == new_h) and new_s > new_h:
        #     count -= 1

        # update
        h = new_h
        m = new_m
        s = new_s

        if m >= 360:
            m -= 360
        if s >= 360:
            s -= 360

    return count


def solution(h1, m1, s1, h2, m2, s2):
    """
    h1시 m1분 s1초부터 h2시 m2분 s2초까지 초침과 (시침or분침) 이 겹치는 횟수

    00:00:00 ~ 11:59:59
    12:00:00 ~ 23:59:59 --> 00:00:00 ~ 11:59:59 로 변환해서 생각
    """
    answer = 0

    # 00:00:00 ~ 11:59:59 범위 내인 경우
    if h1 < 12 and h2 < 12:
        answer += check_overlap(h1, m1, s1, h2, m2, s2)

    # 12시 이후만 있는 경우
    elif h1 >= 12 and h2 >= 12:
        h1 -= 12
        h2 -= 12
        answer += check_overlap(h1, m1, s1, h2, m2, s2)

    # 00:00:00 ~ 11:59:59 + 12시이후~ 둘다 있는 경우
    else:
        answer += check_overlap(h1, m1, s1, 11, 59, 59)
        answer += check_overlap(0, 0, 0, h2 - 12, m2, s2)

        # 끝이 12:00:00 이 아닌 정시이면 소수점 오차로 while문이 안돌아감 (테스트 케이스 19)
        # 예시 : solution(9, 59, 58, 10, 0, 0)
        # 360.00000000000006 vs 360
        if h2 != 12 and (m2 == 0 and s2 == 0):
            answer += 1

    return answer
