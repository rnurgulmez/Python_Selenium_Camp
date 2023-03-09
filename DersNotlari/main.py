print("kodlama io")
baslik = "Taşıt Kredisi"
print(baslik)
# string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
# int,integer => tam sayı
vade = 36
ekVade = 12
vade2 = "36"

# float,decimal,double
aylikOdeme = 200.50

# bool,boolean => True veya False
yukselisteMi = False

# matematiksel operatörler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# *
print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10 / 2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operator
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

# mantıksal operatorler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(1 < 2)
print(1 > 1)
print(1 <= 1)

# ctrl + k + c yorum satırına alma
# ctrl + k + u yorum satırından çıkarma

print(1 != 1)
print(1 != 2)


# or and

print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)
print(1 > 2 and 5 > 2 and 3 < 2)
print(2 > 1 or 1 > 2 and 3 > 2)

# karar yapıları
# if elif else
sayi1 = 15
sayi2 = 15
# sayi1 sayi2'den büyükse ekrana sayi1 daha büyük yazdır.

# indent

if sayi1 >= sayi2:
    print("sayi1 sayi2'den büyüktür")
    print("Hala if bloğu içerisindeyim")
# eğer if bloğuna girmezse
elif sayi1 == sayi2:
    print("sayi1 sayi2'ye eşittir.")
# eğer if ve elif bloklarına girmezse
else:
    print("sayi1 sayi2'den küçüktür.")
print("**************")

# her if yazdığımızda ayrı ayrı çalışır.
if sayi1 <= sayi2:
    print("sayi1 sayi2'den küçüktür")
if sayi1 == sayi2:
    print("iki sayı eşittir")
else:
    print("sayi1 sayi2'den büyüktür.")

# karar bloğunda bir karar doğruysa diğer kararlara bakılmaz
