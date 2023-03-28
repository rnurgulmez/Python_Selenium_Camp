### PyTest'deki Dekoratörler
<html>
<head>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<dl>
<dt> _Dekoratör nedir ?_  <dt>
<dd> Python'da dekoratörler @decorator_name syntaxi ile ifade edilen islevsel ozelliklerdir. Class veya function yapilarinin hemen uzerine yerlestirilir.
Dekoratörler ilgili fonksiyon veya sinifin islevini degistirmeden davranisini degistirir veya ek ozellikler ekler.
<dd>
<dl>

Pytest, bir Python test çerçevesidir ve test yazarken kullanabileceğiniz bir dizi dekoratöre sahiptir. Bu dekoratörler, testleri yürütürken nasıl davranacaklarını belirlemek için kullanılır. Bazı yaygın pytest dekoratörleri şunlardır:

* @pytest.fixture: Bu dekoratör, testlerinizde kullanmak için bir "fixture" oluşturmanızı sağlar. 
  Bir "fixture", örneğin bir veritabanı bağlantısı veya bir örnek gibi, testlerinize bir kaynak sağlar.

* @pytest.mark.parametrize: Bu dekoratör, aynı testin farklı parametrelerle birden çok kez çalıştırılmasını sağlar. 
  Bu özellikle bir dizi girişle çalışan testler için yararlıdır.

* @pytest.mark.skip: Bu dekoratör, bir testin belirtilen nedenlerle atlanmasını sağlar. 
  Örneğin, bir test sadece belirli bir platformda çalışıyorsa, diğer platformlarda bu testi atlayabilirsiniz.

* @pytest.mark.xfail: Bu dekoratör, bir testin başarısız olmasını beklediğinizi belirtir. 
  Bu, hataların düzeltilmesi gereken testler üzerinde çalışırken yararlıdır.

* @pytest.mark.timeout: Bu dekoratör, bir testin belirli bir sürede tamamlanmasını sağlar. 
  Eğer test belirli bir sürede tamamlanamazsa, test hata verir ve başarısız olur.
</body>
</html>
