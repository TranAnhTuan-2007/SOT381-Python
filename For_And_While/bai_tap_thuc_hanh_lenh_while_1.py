#Bài 1: Tính giai thừa
n = int(input("Nhập n: "))
giai_thừa = 1
for i in range(1, n + 1):
    giai_thừa *= i
print(f"{n}! = {giai_thừa}")