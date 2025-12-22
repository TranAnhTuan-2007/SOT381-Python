n=int(input("nhập số lượng bài hát yêu thích: "))
danh_sach_bai_hat=[]
for i in range(n):
    ten_bai=input("nhập tên bài mới: ")
danh_sach_bai_hat.append(ten_bai)
print(danh_sach_bai_hat)
danh_sach_in_hoa=[bai.upper() for bai in danh_sach_bai_hat]
print(danh_sach_in_hoa)
for i in range(n):
    ten=danh_sach_bai_hat
if ten.find("yêu"):
    print("bài  {i}: {ten}")
