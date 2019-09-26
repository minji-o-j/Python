import time

fs=time.time()
minute=fs//60%60
hour=fs//60//60%24

print("현재 시간(영국 그리니치 시각) %d 시 %d분" %(hour,minute))
print(fs)
