# liste oluşturduk
ogrenciler = ["Ayşe Bahar", "Ahmet Yılmaz", "Esra Genç", "Ali Öz"]

# listemize kullanıcıdan aldığımız yeni bir eleman girdik
yeniOgrenci1 = input("Lütfen eklemek istediğini öğrencinin adını giriniz : ")
ogrenciler.append(yeniOgrenci1)

# listeden kullanıcının istediği bir elemanı kaldırdık
silinenOgrenci = input(
    "Lütfen kaldırmak istediğiniz öğrencinin adını giriniz : ")
ogrenciler.remove(silinenOgrenci)

# kullanıcının girdiği 2 öğrenciyi listemize ekleyen bir fonksiyon yaptık


def ogrenciEkle():
    ogrenci1 = input("Eklemek istediğiniz öğrencinin adı : ")
    ogrenci2 = input("Eklemek istediğiniz öğrencinin adı : ")
    ogrenciler.extend([ogrenci1, ogrenci2])
    return ogrenciler

# listemizdeki değerleri tek tek görüntüleyen bir fonksiyon yazdık


def listeGoruntule():
    for i in range(len(ogrenciler)):
        print(ogrenciler[i])
        return ogrenciler

# index numaralarını öğrenci numarası olarak kabul edip öğrenci adlarını ve numaralarını aynı anda aldık.


def ogrenciNumarasıOgren():
    i = 0
    while i < len(ogrenciler):
        print(f"{ogrenciler[i]},{ogrenciler.index(ogrenciler[i])}")
        i += 1
        return ogrenciler

# listeden birden fazla öğrenci silen fonksiyon döngü kullanılarak?? (in progress:D)


# fonksiyonlarımızı çağırdığımız alan
print(ogrenciler)
ogrenciNumarasıOgren()
listeGoruntule()
ogrenciEkle()
print(ogrenciler)
