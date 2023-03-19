nama = ["Joko","Budi","Eko","Bagas","Bastian","Ben"]
urutan = 3
print(nama[urutan-1])

# Mendapatkan nama pertama
print("Nama pertama : ",nama[0])

# Mendapatkan data terakhir
print("Nama terakhir : ",nama[-1])

# Mendapatkan panjang list
print(len(nama))

# Nama Terakhir
print("Nama terakhir : ",nama[len(nama)-1])

# Mengecek apakah ada di dalam list
cek_nama = "Ben"
print(cek_nama in nama)

if cek_nama in nama:
    print(f"Ada nama {cek_nama} di dalam list")
else:
    print(f"Tidak ada nama {cek_nama} di dalam list")