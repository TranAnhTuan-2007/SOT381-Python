def tinh(n):
    tu=1
    mau=2
    for i in range (1,n+1):
        tu = tu+i
    for j in range (2,n,2):
        mau=mau+j
    S=tu/mau
    return S

n=int(input("nhập n: "))
S=tinh(n)
print(f"đáp số của S là {S}")
    