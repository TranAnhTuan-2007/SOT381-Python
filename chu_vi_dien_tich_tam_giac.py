import math
a=float(input("nhập cạnh tam giác a: "))
b=float(input("nhập cạnh tam giác b: "))
c=float(input("nhập cạnh tam giác c: "))
if a+b>c and b+c>a and a+c>b:
    chu_vi=a + b + c
    p= chu_vi/2
    dien_tich= math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"chu vi hình chữ nhật là {chu_vi:.2f}")
    print(f"diện tích hình chữ nhật là {dien_tich:.2f}")
    
