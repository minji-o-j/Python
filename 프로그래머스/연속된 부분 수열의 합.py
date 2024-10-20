# 투포인터
def solution(sequence, k):
    seqlen = len(sequence)
    answer = []
    
    end = 0 # end pointer
    checksum = 0
    
    for start in range(seqlen):
        while checksum < k and end < seqlen: # end 늘리기
            checksum += sequence[end]
            end += 1
        
        if checksum == k:
            answer.append([end-1-start,start, end-1])
        
        checksum -= sequence[start] # start 늘리기
    
    answer.sort()
    
    return answer[0][1:]
 
