print("\nSelamat datang di program kalkulator sederhana")
print("==============================================\n")

j = 0
while j < 1:
  x = int(input("masukkan bilangan pertama : "))
  i = 0
  while i < 1:
    operasi = str(input("masukkan operasi aritmatika : "))
    if (operasi == "+") or (operasi == "-") or (operasi == "*") or (operasi == "/"):
      i += 1
    else:
      print("jenis operasi yang anda masukkan salah!!!")
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
  k = 0
  
  choise = str(input("apakah anda ingin keluar dari program (y/n): "))
  if choise == "y":
    j += 1
    print("Sampai jumpa kembali :)")