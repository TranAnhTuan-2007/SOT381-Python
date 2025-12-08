#Bài 12: In bảng cửu chương – In bảng cửu chương từ 2 đến 9
i = 2
while i <= 9:
    print(f"Bảng cửu chương {i}")
    j = 1
    while j <= 10:
        ket_qua = i * j
        print(f"{i} x {j} = {ket_qua}")
        j += 1
    i += 1