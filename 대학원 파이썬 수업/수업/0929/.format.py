
x = 'I got {} score in the test'
print(x.format(90))

x = 'I got {:5d} score in the test' # 우측
print(x.format(90))

x = 'I got {:10d} score in the test' # 우측
print(x.format(90))

x = 'I got {:>10d} score in the test' # 우측
print(x.format(90))

x = 'I got {:<10d} score in the test' # 좌측
print(x.format(90))


x = 'I got {:^10d} score in the test' # 가운데
print(x.format(90))

x = 'I got {:=10d} score in the test' # 부호만 좌측으로
print(x.format(-90))


x = 'I got {:10.3f} score in the test' # 우측
print(x.format(85.78204))

x = 'I got {:>10.3f} score in the test' # 우측
print(x.format(85.78204))

x = 'I got {:<10.3f} score in the test' # 좌측
print(x.format(85.78204))


x = 'I got {:^10.3f} score in the test' # 가운데
print(x.format(85.78204))

x = 'I got {:=10.3f} score in the test' # 부호만 좌측으로
print(x.format(-85.78204))
