giai_thua=1
n=int(input("nhập n:"))
if n>0 and n<10:
    for i in range (1,n+1):
        giai_thua = giai_thua * i
    print(f"n!={giai_thua}")
