
#              ********** Ödev 2 **************

krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan Alanlara Özel",
            "Mutlu Emekli İhtiyaç Kredisi"]
print(krediler)
print(krediler[0])

print(len(krediler))  # length

krediler[0] = "Çabuk Kredi"
print(krediler)

# print(krediler[5])

ogrenciler = ["ali", "ahmet", "mehmet"]
print(ogrenciler[0])
print(ogrenciler[1])
print(ogrenciler[2])

urunler = ["elektronik", "moda", "ev,yasam,kırtasiye,ofis", "oto,bahce,yapı market",
           "anne,bebek,oyuncak", "spor,outdoor", "kozmetik kisisel bakim"]

for urun in urunler:
    print(urun)

for i in range(len(krediler)):
    print(krediler[i])

# 3 dahil 10 dahil değil
for i in range(3, 10):
    print(i)

# 0 dahil 10 değil 2şer 2şer arttır
for i in range(0, 10, 2):
    print(i)
