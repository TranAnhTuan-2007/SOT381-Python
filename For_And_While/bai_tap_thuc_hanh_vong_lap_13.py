#Bài 13: Tính giai thừa – Tính giai thừa của số n
n = int(input("Nhập số nguyên dương: "))
giai_thừa = 1
i=1
while i<n:
    i+=1
    giai_thừa *= i
print(f"{n}! = {giai_thừa}")