jumlah_buku = 10
print(f"ibu berkata, 'Baca semua  bukumu' ")
total_jumlah_baca= 0

jumlah_buku_dibaca_dandipahami = 0
print(f" jumlah buku yang susah dibaca dandipahami {jumlah_buku_dibaca_dandipahami}")


while total_jumlah_baca < jumlah_buku * 2 :
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_dibaca_dandipahami == 9 :
        print(f" buku ke {jumlah_buku_dibaca_dandipahami}")
    else:
        jumlah_buku_dibaca_dandipahami = jumlah_buku_dibaca_dandipahami +1
        print(f"buku ke {jumlah_buku_dibaca_dandipahami} sudah di baca dan di pahami")

print(f'jumlah buku yang sudah di pahami dan di baca {jumlah_buku_dibaca_dandipahami}')
if jumlah_buku_dibaca_dandipahami == jumlah_buku :
    print('semua buku sudah di baca dan dipahami')
else:
    print(f'bu tidak semua buku dipahami'
          f'budi hanya bisa memahami {jumlah_buku_dibaca_dandipahami}')