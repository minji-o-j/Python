a=int(input("9999이하의 정수를 입력해주세요: "))
fst=a%10
snd=a%100//10
trd=a%1000//100
fth=a//1000
print("자릿수의 합: ",fst+snd+trd+fth)
