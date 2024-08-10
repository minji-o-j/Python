def solution(numbers):
    int_to_str = [str(n) for n in numbers]
    int_to_str.sort(key = lambda x:x*3,reverse=True)
    
    # 0만있는 경우 제외
    if set(int_to_str) == set(["0"]):
        return "0"
    
    return ''.join(int_to_str)

    
    """
    566 56 565 5 55 555 549 54 544
    
    566 # 다른 애들 첫번째 자리는 5이므로 제일 크다
      
    549 54 544
    앞의자리 (5) 를 뒤에 붙였을 때 큰 문자열 순 5495>545>544
    
    56 565  -> 56565  > 56556
    545 54 ->  54554 > 54545
    
    5656 565565
    545545 5454
    자릿수 반복
    
    """
