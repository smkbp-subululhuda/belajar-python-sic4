# Output = 97000
# Rincian
# Ayam  : 2 * 3000
# Sayur : 1 *
# Ikan  : 1 *

data_toko = {
    'Indoramet':{
        "Ayam":3000,
        "Sayur":15000,
        "Buah":20000,
        "Ikan":22000
    }
}

items_to_buy = {
    "Ayam":2,
    "Sayur":1,
    "Ikan":1
}

keylist = list(items_to_buy.keys())
print(keylist)

total = 0

for item in keylist:
    subtotal = data_toko['Indoramet'][item] * items_to_buy[item]
    total += subtotal

print(subtotal)

print(items_to_buy['Ayam'])
print(items_to_buy['Sayur'])
print(items_to_buy['Ikan'])