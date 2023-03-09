# Python'da Veri Tipleri

#                     ********* SORU 1 **********
# Metin tipleri    :   str
# Sayısal tipler   :   int , float , complex
# Dizi tipleri     :   list , tuple , range
# Adresleme tipleri:   dict
# Küme tipleri     :   set , frozenset
# Mantıksal tipler :   bool
# Binary tipler    :   bytes , bytearray , memoryview

# Integers : int => Tüm pozitif,negatif tam sayılar
x = 3
print(type(x))
y = -50000
print(type(y))

# Floating Point : float => Tüm pozitif,negatif ondalıklı sayılar
x = 3.15
print(type(x))
y = -54232.4657
print(type(y))

# Strings : str => "char"ların birleşmesinden meydana gelen metinsel veri türleri
# String veri türü ile kullanılan birçok özel metot da vardır.
x = "hello"
print(type(x))
y = 'Rabia'
print(type(y))

# Lists : list => Sıralı nesne dizisi. Köşeli parantez ile kullanılır.
x = [10, "hello", 200.3]
print(type(x))

# Dictionaries : dict => Sırasısız değer çiftleri
x = {"key": "value", "name": "rabia"}
print(type(x))
# Tuples : tup => Sıralı değişmez nesneler dizisi.Read-only.
x = (10, "hello", 200.3)
print(type(x))

# Sets : set => Sırasız benzersiz nesne koleksiyonu
x = {"a", "b"}
print(type(x))

# Booleans : bool => Mantıksal ifade True or False
x = True
print(type(x))

#                  ********** SORU 2 ***********

# Kodlama.io sitesinden veri tipi örnekleri
# string : Kurslarım,Tüm Kurslar,Kariyer ve Sık Sorulan Sorulan
# int : kariyer kısmındaki telefon numarası kısmı,kurs ilerleme yüzdemiz


#                  ********** SORU 3 ***********
# Şart bloğu olabileceğini düşündüğüm kısım her ödev yaptığımızda bitir ve devam et butonuna bastıktan sonra
# %3 tamamlandı daha ekleniyor fakat bu durumu nasıl anlatacağımı bilmediğimden sadece gösterim olarak yaptım.

odevYapildiMi = "false"

if odevYapildiMi == "true":
    print("%3 ilerlediniz")
else:
    print("ilerlemediniz")
