def so_nho_nhat(a,b,c):
    so_nho=a
    if b<so_nho:
        so_nho=b
    if c<so_nho:
        so_nho=c
    return so_nho
a=float(input("nhập a: "))
b=float(input("nhập b: "))
c=float(input("nhập c: "))
print(f"số nhỏ nhất là {so_nho_nhat(a,b,c)}")