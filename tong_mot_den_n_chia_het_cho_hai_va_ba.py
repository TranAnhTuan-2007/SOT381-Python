n = int(input("nhập số n: "))
tong=0
for i in range (1,n+1):
    if i%2==0 and i%3==0:
        tong = tong + i
print(f"tổng các số 1->n chia hết cho 2 và 3: {tong}")