panjang = int(input("Masukkan Panjang: "))
miring = int (input("Masukkan miring : "))
for j in range(miring,0,-1):
    for k in range(0,j-1):
        print("*",end="")
    for l in range(0,panjang):
        print("*",end="")
    print()