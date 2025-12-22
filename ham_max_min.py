def tim_max_min(a,b,c):
    so_lon_nhat=max(a,b,c)
    so_nho_nhat=min(a,b,c)
    return so_lon_nhat, so_nho_nhat
a=float(input("nhập a: "))
b=float(input("nhập b: "))
c=float(input("nhập c: "))
lon, nho=tim_max_min(a,b,c)
print(f"số lớn nhất là {lon}")
print(f"số nhỏ nhất là {nho}")