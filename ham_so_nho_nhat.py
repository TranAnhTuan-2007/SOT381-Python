def so_lon_nhat(a,b,c):
    so_lon=a
    if b>so_lon:
        so_lon=b
    if c>so_lon:
        so_lon=c
    return so_lon
a=float(input("nhập a: "))
b=float(input("nhập b: "))
c=float(input("nhập c: "))
print(f"số lớn nhất là {so_lon_nhat(a,b,c)}")