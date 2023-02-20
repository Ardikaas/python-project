print("Selamat datang di program kalkulator sederhana")

x = int(input("masukkan bilangan pertama : "))
operasi = str(input("masukkan operasi aritmatika : "))
y = int(input("masukkan bilangan kedua : "))

if operasi == "+":
  hasil = x + y
  print("operasi yang anda pilih adalah penjumlahan")
  print(x, "+", y, "=", hasil)
else:
  print("operasi yang anda masukkan salah!!!")