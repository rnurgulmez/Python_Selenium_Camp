# alias
import matematik as m
# bir modulden istedigimiz alani import edebiliriz ancak boyle oldugunda matematik. seklinde degil topla(10,20) olarak kullaniriz
from matematik import topla as toplamaIslemi #, bol as bolmeIslemi
from ders2 import sayHello
# class da import edebiliyoruz
from ders3 import Human
# built in modules
import random
# package

# import etsek bile matematik.topla() demeliyiz direkt topla olmuyor. 
print(toplamaIslemi(20,30))
print(random.randint(0,100))

human1 = Human("Rabia")
human1.talk("Merhaba")

# packages
