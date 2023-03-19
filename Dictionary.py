data = {
    "nama_depan" : "Budi",
    "nama_belakang" : "Doremi",
    "umur"  : 13,
    "hobi" : "Memancing"
}
# Cek apakah ada nama_depan
print("nama_depan" in data)

# Cek panjang data
print("Panjang data : ",len(data))

# Generate email
print("Email anda : " + data["nama_depan"]+"."+data["nama_belakang"]+"@gmail.com")

# Sebelum dihapus
print(data)
# Menghapus elemen
data.pop("hobi")
print(data)

# Mengambil value
for x in data.keys():
    print(x)

# Mengambil value
for x in data.values():
    print(x)