print("Selamat datang di program kalkulator sederhana")

x = int(input("masukkan bilangan pertama : "))
operasi = str(input("masukkan operasi aritmatika : "))
y = int(input("masukkan bilangan kedua : "))

if operasi == "+":
  hasil = x + y
  print("operasi yang anda pilih adalah penjumlahan")
  print(x, "+", y, "=", hasil)
elif operasi == "-":
  hasil = x - y
  print("operasi yang anda pilih adalah pengurangan")
  print(x, "-", y, "=", hasil)
elif operasi == "*":
  hasil = x * y
  print("operasi yang anda pilih adalah perkalian")
  print(x, "*", y, "=", hasil)
elif operasi == "/":
  hasil = x / y
  print("operasi yang anda pilih adalah pembagian")
  print(x, "/", y, "=", hasil)
else:
  print("jenis operasi yang anda masukkan salah")
  print("syntax error 404!!!")