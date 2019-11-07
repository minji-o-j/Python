t=int(input("성적을 입력하시오: "))
if t>=90:
    print("A학점입니다.")
    
elif (t<90)and(t>=80):
    print("B학점입니다.")
    
elif (t<80)and(t>=70):
    print("C학점입니다.")

elif (t<70)and(t>=60):
    print("D학점입니다.")
    
else:
    print("F학점입니다.")
