#두 번 이상 나온 이름 찾기
#입력:이름이 n개 들어 있는 리스트
#출력:이름 n개 중 반복되는 이름의 집합

def find_same_name(a):
    n=len(a)                        #리스트의 자료 개수를 n에 저장// list를 넘김, list의 길이를 반환
    result=set()                    #결과를 저장할 빈 집합// set:집합형 자료형, list와 set는 모두 자료형, set는 중복을 허락하지 않는다!!
    for i in range(0,n-1):          #0부터 n-2까지 반복
        for j in range(i+1,n):      #i+1부터 n-1까지 반복
            if a[i]==a[j]:          #이름이 같으면
                result.add(a[i])    #찾은 이름을 result에 추가
    return result


name=["","","","",""]
name[0]=str(input("첫 번째 친구 이름:"))
name[1]=str(input("두 번째 친구 이름:"))
name[2]=str(input("세 번째 친구 이름:"))
name[3]=str(input("네 번째 친구 이름:"))
name[4]=str(input("다섯 번째 친구 이름:"))

print(find_same_name(name))
print("동명이인인 수는 %d명 입니다." %len(find_same_name(name)))


#친구 이름 입력, 동명 이인 명수
