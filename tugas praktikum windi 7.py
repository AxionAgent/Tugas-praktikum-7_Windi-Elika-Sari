## Soal 1: Manipulasi List
#DIBERIKAN LIST BERIKUT
kendaraan = ["motor","mobil","sepeda","bus"]

# a. Tambahkan "truk" di akhir list
kendaraan.append("truk")
print(kendaraan)

# b. sisipkan "becak" pada index ke-1
kendaraan.insert(1, "becak")
print(kendaraan)

# c. Hapus data yang berada paling belakang dari list tersebut
kendaraan.pop()
print(kendaraan)

# d. Ubah elemen "sepeda" menjadi "skuter"
#"sepeda" sekarang berada di indexs ke-3 setelah proses insert sebelumnya
kendaraan[3] = "skuter"
print(kendaraan)

# e. Tampilkan informasi jumlah total data di dalam list tersebut
panjang_kendaraan = len(kendaraan)
print(f"Jumlah total data : {panjang_kendaraan}")

#Soal 2:Operasi Nilai pada List angka
#DIBERIKAN LIST BERIKUT
angka = [75, 80, 90, 75, 85, 100, 65]

# a. Cari tahu di indeks ke berapa skor 100 berada
index_100 = angka.index(100)
print(f"Angka 100 berada di index ke: {index_100}")

# b. Hitung ada berapa banyak siswa yang mendapatkan skor 75
jumlah_75 = angka.count(75)
print(f"Banyak siswa yang mendapatkan skor 75: {jumlah_75}")

# c. Urutkan List tersebut dari niali terkecil hingga terbesar
print(f"Data sebelum diurutkan: \n{angka}")
angka.sort()
print(f"Data setelah diurutkan dari yang terkecil: \n{angka}")

# d. Balikan urutan list yang sudah diurutkan (terbesar ke terkecil)
angka.reverse()
print(f"Dsta setelah diurutkan dari yang terbesar:\n{angka}")

#Soal 3: Penggabungan List Menu
# menu_utama = ["Nasi Goreng", "Mie Ayanm"]
# menu_tambahan ["Kerupuk", "Es Teh"]
# Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan tersebut.
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
print(f"List sebelum dibagikan \n{menu_utama} dan {menu_tambahan}")
print(f"List sebelum digunakan \n{menu_utama} dan {menu_tambahan}")
menu_utama.extend(menu_tambahan)
print(f"List setelah digabungkan \n{menu_utama}")

#Soal 4:Akses dan Perulangan Nested List(List Bersarang)
# Diberikan data nested List berupaa informasi nama barang dan harganya:
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Tampilkan harga dari "Pensil" (Baris index 1, kolom index 1)
pensil = data_barang[1][1]
print(f"nama barang dan harga: {data_barang[1][0]} {pensil}")

# b. Gunakan perulangan untuk menampilkan format "Nama: [nama barang], Harga: [harga]"
for i in data_barang:
    print(f"Nama barang\t: {i[0]}")
    print(f"Harga barang\t: {i[1]}")

    