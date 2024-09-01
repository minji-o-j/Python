def solution(n):
    answer = 0
    if n%2 != 0:
        return 0
    
    n2 = n//2
    
    sol_list = [0,3,11] #f0, f2, f4

    if n2<=2 :
        return sol_list[n2]
    
    for i in range(2, n2):
        nmin2 = 3 * sol_list[i] + sum(sol_list[:i]) * 2 + 2 # 3f(n-2) + 2(f(n-4)+f(n-6)+...) +2
        sol_list.append(nmin2)
        
    answer = sol_list[-1]

    return answer%1000000007
