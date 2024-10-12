def formula_decomp(f):  # 수식분해
    A, op, B, _, C = f.split()
    return A, B, C, op


def ten_to_q(n, q):  # 10 to q진수
    if n==0: return "0"
    tmp  = ""
    while n:
        tmp += str(n%q)
        n = n//q
    return tmp[::-1]


def solution(expressions):
    # x가 있는/없는 수식 구분
    in_x = []
    no_x = []
    min_f = 2
    check = []
    for e in expressions:
        a, b, c, op = formula_decomp(e)
        if c == "X":
            in_x.append((a, b, c, op))
        else:
            no_x.append((a, b, c, op))
        # 최소 진수 확인

        for aa in a:
            check.append(int(aa))
        for bb in b:
            check.append(int(bb))

        if c != "X":
            for cc in c:
                check.append(int(cc))

        check_max = max(check) + 1
        if check_max > min_f:
            min_f = check_max

    # 몇진법인지 체크
    formation_list = []  # 여러 개 진법에서 식이 성립할 수도 있다
    for i in range(min_f, 10):  # 2~9진법
        flag = 0
        for a, b, c, op in no_x:
            check_a = int(a, i)  # i진수 -> 10진수 변환
            check_b = int(b, i)
            check_c = int(c, i)

            if op == "+":
                if check_a + check_b == check_c:
                    pass
                else:  # i진수 계산이 성립하지 않음
                    flag = 1
                    break
            else:  # op == '-'
                if check_a - check_b == check_c:
                    pass
                else:
                    flag = 1
                    break

        if flag == 0:
            formation_list.append(i)

    answer = []
    
    if len(formation_list) == 1:  # 가능한 진수가 하나
        # 계산해서 출력
        for a, b, x, op in in_x:
            
            # 실제 값 계산
            # 10진수 계산

            if op == "+":
                ans_10 = int(a, formation_list[0]) + int(b, formation_list[0])
            else:
                ans_10 = int(a, formation_list[0]) - int(b, formation_list[0])
            c = str(ten_to_q(ans_10, formation_list[0]))
            ans_str = f"{a} {op} {b} = {c}"
            answer.append(ans_str)

    elif len(formation_list) >1:
        # 계산해서 출력
        for a, b, x, op in in_x:
            ans_str = f"{a} {op} {b} = "
            # 실제 값 계산
            check_answer = set([])
            flag2 = 0

            for i in formation_list:  # 진수
                # i들에 대해서 모두 동일한 값을 가지면
                if op == "+":
                    ans_10 = int(a, i) + int(b, i)
                else:
                    ans_10 = int(a, i) - int(b, i)
                
                check_answer.add(ten_to_q(ans_10, i))

                # i에 대해서 하나라도 다른 값을 가지면
                if len(check_answer) > 1:
                    flag2 = 1
                    break

            if flag2 == 0:  # 동일값
                ans_str += ten_to_q(ans_10, i)
                answer.append(ans_str)
            else:
                ans_str += "?"
                answer.append(ans_str)

    return answer
