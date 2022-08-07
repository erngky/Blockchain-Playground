class Ogrenci():
    okul_ismi = "YTÜ"

    def __init__(self, numara, bolum, bolum_dili, giris_yili, ortalama):
        self.numara = numara
        self.bolum = bolum
        self.bolum_dili = bolum_dili
        self.giris_yili = giris_yili
        self.ortalama = ortalama

    def ort_hesapla(self):
        ort = self.ortalama * 25
        print("Ortalama 4 üzerinden {}, 100 üzerinden {}.".format(self.ortalama, ort))

    def mezuniyet_yili(self):
        if self.bolum_dili == "ingilizce":
            mez_yili = self.giris_yili + 5
            print("{} numaralı öğrenci {} yılı mezunudur.".format(self.numara, mez_yili))
        else:
            mez_yili = self.giris_yili + 4
            print("{} numaralı öğrenci {} yılı mezunudur.".format(self.numara, mez_yili))


Eren = Ogrenci(1, "işletme", "ingilizce", 2020, 3)
Elif = Ogrenci(2, "kimya", "türkçe", 2021, 3.5)
Ahmet = Ogrenci(3, "matematik", "türkçe", 2019, 2)
Selami = Ogrenci(4," fizik", "ingilizce", 2022, 2)

