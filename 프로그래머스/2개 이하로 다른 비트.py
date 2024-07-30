
def solution(numbers):
    answer = []
    for n in numbers:
        # 2로 나눠지면 1만 더하면 됨
        if n%2==0:
            answer.append(n+1)
        else:
            b = bin(n)[2:] #이진수 ~ 숫자만
            if '0' in b:
                b = list(b) #
                # 맨 뒤의 0을 1로 변경
                for i in range(len(b)-1,0,-1):
                    if b[i] == '0':
                        b[i]='1'
                        if i != len(b)-1: #맨 뒤가 아닐 경우 
                            b[i+1]='0' # 1로 바꾼 하나 아래 자릿수를 1->0 
                        break
                new_b = ''.join(b)
                answer.append(int('0b'+new_b,2))
                
            else: # 1로만 구성
                new_b = '10'+b[1:]
                answer.append(int('0b'+new_b,2))

    
    
    return answer
