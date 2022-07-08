class BentukKeramik():
    kotak = 20
    segitiga = 50
    persegipanjang = 80

    def turun(self, x):
        if x <= self.kotak:
            return 0
        elif x >= self.segitiga:
            return 1
        else:
            return bawah(x, self.segitiga, self.kotak)

    def pas(self, x):
        if self.kotak < x < self.segitiga:
            return atas(x, self.kotak, self.segitiga)
        elif self.segitiga < x < self.panjang:
            return bawah(x, self.segitiga, self.persegipanjang)
        elif x == self.segitiga:
            return 1
        else:
            return 0

    def naik(self, x):
        if x >= self.segitiga:
            return 1
        elif x <= self.persegipanjang:
            return 0
        else:
            return up(x, self.persegipanjang, self.segitiga)

class BahanKeramik():
    halus = 20
    kasar = 40
    batu = 60

    def sedikit(self, x):
        if x >= self.halus:
            return 0
        elif x <= self.kasar:
            return 1
        else:
            return down(x, self.kasar, self.halus)
    
    def cukup(self, x):
        if self.kasar < x < self.halus:
            return up(x, self.kasar, self.halus)
        elif self.halus < x < self.batu:
            return down(x, self.halus, self.batu)
        elif x == self.halus:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.batu:
            return 1
        elif x <= self.halus:
            return 0
        else:
            return up(x, self.halus, self.batu)

class BentukUkiran():
    tiakada = 20
    sedikit = 40
    jelas = 60

    def sedikit(self, x):
        if x >= self.sedikit:
            return 0
        elif x <= self.tidakada:
            return 1
        else:
            return down(x, self.tidakada, self.sedikit)
    
    def cukup(self, x):
        if self.tidakada < x < self.sedikit:
            return up(x, self.tidakada, self.sedikit)
        elif self.sedikit < x < self.jelas:
            return down(x, self.sedikit, self.jelas)
        elif x == self.sedikit:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.jelas:
            return 1
        elif x <= self.sedikit:
            return 0
        else:
            return up(x, self.sedikit, self.jelas)

class Warna():
    merah = 30
    hijau = 50
    kuning = 70
   
    def sedikit(self, x):
        if x >= self.hijau:
            return 0
        elif x <= self.merah:
            return 1
        else:
            return down(x, self.merah, self.hijau)
    
    def cukup(self, x):
        if self.merah < x < self.hijau:
            return up(x, self.merah, self.hijau)
        elif self.hijau < x < self.kuning:
            return down(x, self.hijau, self.kuning)
        elif x == self.hijau:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.kuning:
            return 1
        elif x <= self.hijau:
            return 0
        else:
            return up(x, self.hijau, self.kuning)
