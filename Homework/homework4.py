# classlar konusunu çalışırken yaptığım denemeler ve notlar
class Banka:
    def krediBasvur(self):
        print("Kredi başvurusu yapıldı")

    def krediHesapla(self):
        print("Hesaplar yapıldı")


banka = Banka()
banka.krediBasvur()


class Person():
    def __init__(self, name, lastName):
        # person için dışarıdan erişebilir name ve last name oluşturduk
        self.name = name
        self.lastName = lastName


musteri1 = Person("Ahmet", "Demirog")
musteri2 = Person("Kerem", "Varış")
musteri3 = Person("İlker", "Tural")

print(musteri1.name)


class Matematik:
    # constructer bloğu --> yapıcı blok self istediği için self yazmak zorundayız
    def __init__(self, sayi1, sayi2):
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik başladı (referans oluştu)")

    def topla(self):
        return self.s1 + self.s2

    def cikar(self):
        return self.s1 - self.s2

    def bol(self):
        return self.s1 / self.s2

    def carp(self):
        return self.s1 * self.s2


matematik = Matematik(14, 7)
sonuc = matematik.bol()
print(f"Sonuç : {sonuc}")


class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        # ebeveyn sınıfı super
        super().__init__(sayi1, sayi2)

    def varyansHesapla(self):
        return self.s1 * self.s2


istatistik = Istatistik()
istatistik.carp(3, 5)
