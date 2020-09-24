# -*- coding: utf-8 -*-
import math


class MaClasse:
    x=23
    y = x+5

    def affiche(self):
        z=42
        print("("+str(self.y)+", "+str(z)+")")


if __name__ == '__main__':
    try:
        objet = MaClasse()
        objet.affiche()
    except Exception:
        print("ERROR")
