import datetime
print("====================================================")
print("                  Kuliner Makanan                   ")
current_date = datetime.date.today()
formatted_date = current_date.strftime("%A, %B %d %Y")
print("ror |", formatted_date)
print("====================================================")
print()
print("====================================================")
PW = input("Password                       :")
print("====================================================")
print("")
if PW == "12345":
  print("PW benar")
  print("Pilihan menu :")
  print("1. Nasi Goremg  4. Teh Manis")
  print("2. Nasi Rames   5. Jus Apple")
  print("3. Nasi Uduk    6. Jus Jeruk")
  FOD = input("Masukkan pilihan Makanan :")
  DRK = input("Masukkan pilihan Minuman :")
  FJPS = input("Jumlah Porsi Makanan           :")
  DJPS = input("Jumlah Porsi Minuman           :")

  if FOD == '1':
    FN = "Nasi Goremg"
    FH = 16000
  elif FOD == '2':
    FN = "Nasi Rames"
    FH = 14000
  elif FOD == '3':
    FN = "Nasi Uduk"
    FH = 7000
  else:
    FN = "Menu Tidak Ditemukan"
    FH = "Menu Tidak Ditemukan"

  if DRK == '4':
    DN = "Teh Manis"
    DH = 5000
  elif DRK == '5':
    DN = "Jus Apple"
    DH = 10000
  elif DRK == '6':
    DN = "Jus Jeruk"
    DH = 7000
  else:
    DN = "Menu Tidak Ditemukan"
    DH = "Menu Tidak Ditemukan"

  if FN == "Menu Tidak Ditemukan":
      TotalMakanan = "Menu Makanan Tidak Ditemukan"
  else:
      TotalMakanan = FH * int(FJPS)

  if DN == "Menu Tidak Ditemukan":
      TotalMinuman = "Menu Minuman Tidak Ditemukan"
  else:
      TotalMinuman = DH * int(DJPS)

  if isinstance(TotalMakanan, (int, float)) and isinstance(TotalMinuman, (int, float)):
      TotalKeseluruhan = TotalMakanan + TotalMinuman
  else:
      TotalKeseluruhan = "Tidak Dapat Menghitung Total Keseluruhan (Menu Tidak Ditemukan)"


  print("Pilihan Makanan         :", FN)
  print("Harga Makanan           :", FH if isinstance(FH, int) else FH)
  print("Total Harga Makanan     :", TotalMakanan)
  print("Pilihan Minuman         :", DN)
  print("Harga Minuman           :", DH if isinstance(DH, int) else DH)
  print("Total Harga Minuman     :", TotalMinuman)
  print("Total Harga Keseluruhan :", TotalKeseluruhan)
  print("")
  print("====================================================")
  print("")

  if isinstance(TotalKeseluruhan, (int, float)) and TotalKeseluruhan >= 50000:
    DSK = TotalKeseluruhan * 0.2
    TotalAkhirSetelahDiskon = TotalKeseluruhan - DSK
    print("Diskon                 :", DSK)
  else:
    DSK = 0
    TotalAkhirSetelahDiskon = TotalKeseluruhan
    print("Diskon                 :", DSK)
  print("")
  print("====================================================")
  print("")

  BYR = float(input("Tunai                   : "))
  if isinstance(TotalAkhirSetelahDiskon, (int, float)):
      KEMBALIAN = BYR - TotalAkhirSetelahDiskon
      print("KEMBALIAN          :",KEMBALIAN)
  else:
      print("Tidak dapat menghitung kembalian karena total tidak valid.")

  print("")
  print("====================================================")
  print("          Terima Kasih Atas Pembeliannya.           ")
  print("====================================================")

else:
  print("PW salah")
  print("Pembayaran dibatalkan due to incorrect password.")
