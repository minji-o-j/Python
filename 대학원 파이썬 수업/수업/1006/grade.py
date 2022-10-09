score = int(input("enter score: "))

grade = ""
if score >90:
    grade = "A"
elif score >80:
    grade = "B"
elif score > 60:
    grade = "C"
elif 0<score <=60:
    grade = "F"
else:
    grade = "잘못 입력하셨습니다"

print("Your grade is {}".format(grade))
