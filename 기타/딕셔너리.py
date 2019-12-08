addr={}

addr['최재원']='010-1111-1234'
addr['최지윤']='010-2222-1234'
addr['김연수']='010-3333-1234'
addr['김연우']='010-4444-1234'
addr['김가현']='010-5555-1234'
addr['김혜현']='010-6666-1234'
print (addr)
n=str(input('search name: '))
print(addr.get(n,'not Found'))
