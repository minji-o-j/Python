def solution(s):
    save_least = 1000
    # 1은 작성하지 않는다
    for i in range(1, len(s)+1): # 1부터 s길이만큼까지 잘라보기
        now_str = s[:i] # 잘린 str
        now_num = 1
        new_str = "" # 압축된 str
        
        # 몇 토막으로 잘라야하나?
        cutted_len = len(s)//i if len(s)%i==0 else len(s)//i+1
        
        for j in range(1, cutted_len+1): 
            j_str = s[j*i:(j+1)*i]  
            if j_str == now_str:
                now_num+=1
            else:
                if now_num <=1:
                    new_str += now_str
                    now_num=1
                    now_str = j_str
                else: #>=2:
                    new_str += (str(now_num) + now_str)
                    now_num=1
                    now_str = j_str

                    
        if len(new_str)<save_least:
            save_least = len(new_str)

    return save_least
