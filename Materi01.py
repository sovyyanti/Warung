# MATERI TIPE DATA, VARIABEL, OPERATOR ARITMATIK dan input output
print("=====Aplikasi Kalkulator Sederhana=====")
#variabel dan iput data
angka1 = int(input("Masukkan angka pertama :"))#casting tipe data(merubah dari str(string) ke int (integer))
angka2 = int(input("Masukkan angka kedua :"))#karna input("") default nya str(string)
#operator aritmatik
print("1. Penjumlahan")
hasil=angka1+angka2
print (angka1,"+",angka2,"=",hasil)

print("2. Pengurangan")
hasil=angka1-angka2
print (angka1,"-",angka2,"=",hasil)

print("3. Perkalian")
hasil=angka1*angka2
print (angka1,"x",angka2,"=",hasil)

print("4. Pembagian")
hasil=angka1/angka2
print (angka1,":",angka2,"=",hasil)

#untuk modulus (%) atau sisa bagi
#untuk pangkat **
#untuk kebalikan dari modulus //