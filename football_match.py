'''
Se va simula un meci de fotbal intre doua echipe.
Vom defini un teren de fotbal, o minge si pozitia mingii pe terenul de fotbal.
Simularea meciului va consta in definirea numerelor de suturi si contabilizarea tuturor golurilor, outurilor si
cornerelor.
La marcarea golurilor mingea va reveni in centrul terenului.
'''

from random import randint


class Minge:
    def __init__(self, x = 50, y = 25):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x = {self.x}  y = {self.y}"

    def sut(self):
        self.x = randint(0, 101)
        self.y = randint(0, 51)
        return self



class Meci:
    def __init__(self):
        self.e1 = input("Introduceti numele echipei 1: ")
        self.e2 = input("Introduceti numele echipei 2: ")
        self.nr_gol_e1 = 0
        self.nr_gol_e2 = 0
        self.nr_corner_e1 = 0
        self.nr_corner_e2 = 0
        self.nr_out_e1 = 0
        self.nr_out_e2 = 0


    def __repr__(self):
        return f"{self.e1} vs {self.e2} scor {self.nr_gol_e1} - {self.nr_gol_e2}\n" \
            f"Cornere {self.e1} = {self.nr_corner_e1}\n" \
            f"Cornere {self.e2} = {self.nr_corner_e2}\n" \
            f"Outuri {self.e1} = {self.nr_out_e1}\n" \
            f"Outuri {self.e2} = {self.nr_out_e2}\n"

    def simulare(self):
        poz = Minge(50, 25)
        for i in range(1000):
            poz.sut()
            if poz.x == 0 and poz.y >= 20 and poz.y <= 30:
                self.nr_gol_e2 += 1
                poz = Minge()
            elif poz.x == 100 and poz.y >= 20 and poz.y <= 30:
                self.nr_gol_e1 += 1
            elif (poz.x == 0 and poz.y >= 0 and poz.y < 20) or (poz.x == 0 and poz.y > 30 and poz.y < 50):
                self.nr_corner_e2 += 1
            elif (poz.x == 100 and poz.y >= 0 and poz.y < 20) or (poz.x == 0 and poz.y > 30 and poz.y < 50):
                self.nr_corner_e1 += 1
            elif (poz.x >= 0 and poz.x <= 100 and poz.y == 0) or (poz.x >= 0 and poz.x <= 100 and poz.y == 50):
                self.nr_out_e1 += 1

        print(self)

x = Meci()
x.simulare()

