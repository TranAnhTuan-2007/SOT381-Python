#Bài 6: Đảo ngược số – Nhập một số và in ra số đảo ngược của nó
so = int(input("Nhập số cần đảo ngược: "))
so_dao_nguoc = 0
while so > 0:
    chu_so = so % 10
    so_dao_nguoc = so_dao_nguoc * 10 + chu_so 
    so //= 10
print(f"Số đảo ngược: {so_dao_nguoc}")