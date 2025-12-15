s1=int(input("nhập s1: "))
s2 =int(input("nhập s2: "))
tong_s1=0
tong_s2=10
for i in range(1,s1+1):
    tong_s1 = tong_s1 + 1/i
print(tong_s1)
for s in range(1,s2+1):
    t=s-1
    m=s
    tong_s2 = tong_s2 + t/m
print(tong_s2)

    