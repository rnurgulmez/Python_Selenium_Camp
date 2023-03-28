# classlar
# modeules
# paket yonetimi
# self ? arastirmaliyim
# built-in fonksiyonlar arastirilmali
class Human:
    # name = "Rabia"
    # built-in : bir insatance ureildigi anda constructer blok yani init calisir human1 = Human() dendigi anda
    # init : initialize
    # yapici blok her class kullanildiginda calismasini istedigimiz bir sey varsa kullanabiliriz
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi")
    
    def __str__(self):
        return f"STR fonksiyonundan dönen deger : {self.name}"
    def talk(self,sentence):
        name = "Ercan" # self demezsek buradaki name'i kullanir
        # self.name demezsek kendi blogu icinde arar,nesnenin icindeki diger alanlara erisilebilmesi icin self kullanilir.
        print(f"{self.name} : {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

# instance => örnek

human1 = Human("enes")
# burada verdigimiz parametreyi ilkine degil ikinci parametreye atar ilki rezerve oldugu icin
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("halit")
human2.name = "Cem"
human2.talk("Mevlüt")
human2.walk()
print(human2)

# tek satirda Human("Melike").talk("Merhaba") seklinde de calisir.

# Modules : Dosyalar arasi iletisim.Farkli dosyadan kod alabiliyoruz bu sayede