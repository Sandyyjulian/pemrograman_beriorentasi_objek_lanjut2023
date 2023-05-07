class Kendaraan:

    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna

    def berhenti(self):
        print("Kendaraan ini sedang berhenti.")

class SepedaMotor(Kendaraan):

    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc

    def berhenti(self):
        print("Sepeda motor ini sedang berhenti.")

motorA = SepedaMotor("Sepeda Motor", "Aerox", "Hitam", 155)
motorA.berhenti() 
motorA.berhenti() 