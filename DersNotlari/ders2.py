faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

# Type Conversition
# stringden int çeviremeyiz. print(int(krediAdi)) olmaz.
print(int(vade)+12)
faiz = str(faiz)
print(type(faiz))

vade = 30  # int(input("Lütfen istediğiniz vade sayısını giriniz: "))
# Kullanıcıdan alınan input default olarak str sayılır pythonda.
# Ya vade = int(input("Sayı girin")) olarak int'e çeviririz. Ya da işlem sırasında int yaparız ama bu anlık bir dönüşüm olur.
print(type(vade))
vade = vade + 12

# String interpolation
print("Seçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(
    vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")


isim = "Rabia"  # input("İsminizi giriniz : ")
metin = "Merhaba {name}".format(name=isim)
print(metin)

# f-string : {buranın içinde istediğimiz kodu yazabiliriz sadece değişken çağırmak değil}
metin = f"Hoşgeldiniz {isim}"
print(metin)

# listeler

dizi = ["İhtiyaç Kredisi", 10, 5.2]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler))  # length
# print(krediler[3]) => hata verir

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

# pop defaul olarak (-1).elemanı siler o da son eleman demektir.Hiçbir şey vermezsek son eleman silinir.
# pop index sayısı ile çalışır remove adıyla
krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)


krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)


# döngüler

# for döngüsü
# 10 dahil değil
for i in range(10):
    print("xx")
    print(i)

print("**********************")
for i in range(5, 10):
    print(i)

print("**********************")
for i in range(0, 51, 10):
    print(i)

print("**********************")
for kredi in krediler:
    print(kredi)

print("**********************")
for i in range(len(krediler)):
    print(krediler[i])

print("***********************")
array = [0.1, 0.5]
for i in array:
    print(i)

# while döngüsü

# sonsuz döngü
# print("************************")
# while True:
#     print("x")


print("*************************")
i = 0
while i < 5:
    print("x")
    i += 1
print("y")


print("*************************")
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0
while i < len(krediler):
    i += 1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break


# fonksiyonlar

fiyat = 100
indirim = 20
# definition define


def calculate():
    print(100-20)


def calculateWithParams(fiyat, indirim):
    print(fiyat-indirim)


def sayHello(name):
    print(f"Merhaba {name}")


calculate()
calculate()
calculate()
calculate()
calculateWithParams(50, 20)
sayHello("Kahramanmaraş")

# Farklı olmak zorunda değil.Her parametre isim kendi içinde çalışır.


def calculatePrice(fiyat, indirim):
    print(fiyat-indirim)


def calculateAndReturn(fiyat, indirim):
    return fiyat-indirim


yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat+10)

fonk1 = calculatePrice(100, 50)
fonk2 = calculateAndReturn(300, 200)
# Bir değer döndürmez çünkü return demedik bu fonksiyona none void
print(f"164.satır: {fonk1}")
print(f"165.satır: {fonk2}")
