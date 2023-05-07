class Manusia:

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def minum(self):
        print(f"{self.nama} sedang minum.")

class Dosen(Manusia):

    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip

    def menulis(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang menulis.")

dosenA = Dosen("SANDY DWI JULIAN", 19, "210511033")
dosenA.minum() 
dosenA.menulis() 