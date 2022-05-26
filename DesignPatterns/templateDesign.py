from abc import ABCMeta, abstractstaticmethod

# problem bir sureci olan islem oldugunu dusunelim bu islem suresince program verilmis bilgileri kullanirken ekstra olarak
# kullanicidanda bilgi aldigini varsayalim. program donusunde bir obje olusuyor.

# bu ornek uzerinde bir restoranda menu siparisi veriyoruz. Menude sabit olan bir yiyecek ve bir tane sos olacak.
# kullanici ise bu menudeki icecegi ve ikinci sosu secip siparisini veriyor. bunun icin iki secenegi var.
# 1. kola ve ranch sosu
# 2. ayran ve ketcap sosu

class MenuBirinciSecenek(metaclass=ABCMeta):
    
    def yiyecek(self): print('Yiyecek: hamburger')#
    def sosbir(self): print('Birinci Sos: mayonez')
    def sosiki(self): print('Sos secilmedi')
    def icecek(self): print('Icecek secilmemis')


    def siparisi_tamamla(self):
        self.yiyecek()
        self.sosbir()
        self.sosiki()
        self.icecek()
        

# simdi subclass olusturuyoruz. secenekler burada devreye giriyor.

class secenekbir(MenuBirinciSecenek):
    def sosiki(self): print('Ikinci Sos: ranch')
    def icecek(self): print('Icecek: kola')

class secenekiki(MenuBirinciSecenek):
    def sosiki(self): print('Ikinci Sos: ketcap')
    def icecek(self): print('Icecek: ayran')

class secenekuc(MenuBirinciSecenek):
    def sosiki(self): print('Ikinci Sos: mayonez')
    def icecek(self): print('Icecek: su')

# bu iki seceneki kullanicidan alip bu secenekleri kullanarak siparisini yapiyoruz.

# siparis1 = secenekbir()
# siparis1.siparisi_tamamla()
# print('\n')
# siparis2 = secenekiki()
# siparis2.siparisi_tamamla()

# template desing odevi : kullanici kisiel bir araba siparis etmek istiyor. araba markasi , 4 tane tekerlegi , 4 tane kapisi
# kullanici ise bu arabanin rengini, motor gucunu ve bagaj kapasitesini kg bazinda secip siparisini veriyor.