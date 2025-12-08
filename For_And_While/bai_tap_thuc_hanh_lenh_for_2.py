#Bài tập 2: Phân loại học sinh
diem_so = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]
for diem in diem_so:
    if diem >= 8:
        phan_loai = "giỏi"
    elif diem >=6.5 and diem <=7.9:
        phan_loai = "khá"
    else:
        phan_loai = "trung bình"
    print(f"Điểm ({diem}), xếp loại: {phan_loai}")