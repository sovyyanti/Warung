import os
################################
#Aplikasi Warung Kopi Sederhana#
################################

os.system("cls")
#menggunakan if dan looping
print("----------------------------------")
print("| Slemat datang di Warung Kopi...|")
print("----------------------------------")
print(" \n -----Menu-----  ")
print(" Drings : ")

#variabel menu dengan list
minuman = ["Americano","Capucino","Avocado","Air Mineral","Gula Aren"]
harga_minuman = {minuman[0]:25000,minuman[1]:23000,minuman[2]:27000,minuman[3]:5000,minuman[4]:18000}

for m in minuman:
    print(f"{minuman.index(m)+1} . {m} Rp. {harga_minuman.get(m):,}")

print(" \n Snack : ")

#variabel untuk snack
snack = ["Sosis Goreng","Nuget","Dimsum","Pisang Krispi","mix"]
harga_snack = {snack[0]:20000,snack[1]:15000,snack[2]:30000,snack[3]:15000,snack[4]:18000}

for s in snack:
    print(f"{snack.index(s)+1}. {s} Rp. {harga_snack.get(s):,}")

print("-------------------------------")
#input pesanan
daftar_pesanan =[]
pemesan = input("Nama Pemesan : ")
while True: 
    pilih_drings = int(input("Pilih Minuman(1/2/3/4/5) : "))
    if pilih_drings == 1: p1 = minuman[0]
    elif pilih_drings == 2: p1 = minuman[1]
    elif pilih_drings == 3: p1 = minuman[2]
    elif pilih_drings == 4: p1 = minuman[3]
    elif pilih_drings == 5: p1 = minuman[4]
    else: p1="Pilihan Anda Salah"

    pilih_snack = int(input("Pilih Snack(1/2/3/4/5) : "))
    if pilih_snack == 1: p2 = snack[0]
    elif pilih_snack == 2: p2 = snack[1]
    elif pilih_snack == 3: p2 = snack[2]
    elif pilih_snack == 4: p2 = snack[3]
    elif pilih_snack == 5: p2 = snack[4]
    else: p2="Pilihan Anda Salah"


    pesanan_baru = [p1,p2]
    daftar_pesanan.append(pesanan_baru)


    #output menu yang dipesan
    print("\n-------------------------------")
    print("Pesana atas nama :",pemesan)
    print("no.\t| minuman\t| snack")
    for p in daftar_pesanan:
        print(f"{daftar_pesanan.index(p)+1}.\t| {p[0]}\t| {p[1]}")
    print("-------------------------------")

    is_lanjut = input("Apakah mau pesan lagi?(y/n) : ")
    if is_lanjut == "n":
        break
print ("\n\n-----------Pesanan Selesain-----------\n\n")