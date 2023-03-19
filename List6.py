input = [
    {
        "nama":"Budi",
        "nilai":90
    },
    {
        "nama":"Dwi",
        "nilai":85
    },
    {
        "nama":"Tri",
        "nilai":75
    }
]
nilai = []
for value in range(len(input)):
    print(input[value]['nilai'])
    nilai.append(input[value]['nilai'])

print(nilai)
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)

print("Nilai tertinggi : ",nilai_tertinggi)
print("Nilai terendah : ",nilai_terendah)

nama_tertinggi = input[nilai.index(nilai_tertinggi)]['nama']
print(nama_tertinggi)

nama_terendah = input[nilai.index(nilai_terendah)]['nama']
print(nama_terendah)

output = {
    'nama_nilai_tertinggi': nama_tertinggi,
    'nama_nilai_terendah': nama_terendah
}

print(output)