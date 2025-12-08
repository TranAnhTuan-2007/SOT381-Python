#Bài 8: Kiểm tra số đối xứng – Kiểm tra xem một số/chuỗi có đối xứng không
so = input("Nhập số hoặc chuỗi: ")
if so == so[::-1]:
    print("Là số/chuỗi đối xứng")
else:
    print("Không phải số/chuỗi đối xứng")