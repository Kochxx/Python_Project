"""
..module:: ex08
    :synopsis:: Je suis ligoté sur les rails en gare d’Arras.
        Écrire un programme qui affiche un tableau me permettant
        de connaître l’heure à laquelle je serai déchiqueté
        par le train parti de la gare du Nord à 9h
        (il y a 170 km entre la gare du Nord et Arras).
        Le tableau prédira les différentes heures possibles
        pour toutes les vitesses de 100 km/h à 300 km/h, par pas de 10 km/h,
        les résultats étant arrondis à la minute inférieure.
        Écrire une procédure tchacatchac qui reçoit la vitesse du train
        et qui affiche l’heure dudrame. Écrire le programme principal qui affiche le tableau demandé
"""

import math
import sys


class ex08:
    """
       ..class:: Class contains the function for the exercise 8

    """

    def tchacatchac(self, a):
        """
        ..function: Procedure that return the time of arrival of the train
                    according to its speed passed in parameter

        :param a: time value
        :return res: return the string with the speed of the train and the hour of arrival
        """
        # train speed
        v = a
        # distance to go
        dist = 170
        # train departure time 9h00
        hdepart = 9
        try:
            # calculation of train travel time based on speed and distance to be covered
            temps = float(dist)/float(v)
            # number of hours of travel time
            h = int(temps)
            # number of minutes of travel time
            min = int(math.floor((temps-h)*60))
            # Arrival time
            h = h + hdepart
            # stocks the speed of the train and the arrival time associated
            res = (str(v)+"km/h -> "+str(h)+":"+str(min))
            # return the time of train's arrival
            return res
        except Exception:
            raise Exception

    def vitesse(self):
        """
         ..function: Function that returns the speed of the train from 100km/h to 300km/h
                     in 10km/h steps on a table

         :return tab: return the speed of the train
         """
        i = 100
        tab = []
        # use the tchacatchac() function by 10km/h steps
        while i <= 300:
            tab.append(self.tchacatchac(i))
            i = i+10
        return tab


# main function
if __name__ == '__main__':
    try:
        # open file
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        try:
            ex8 = ex08()
            # generates the train's arrival board
            table = ex8.vitesse()
            # print the train's arrival board
            for i in table:
                print(i)
        except Exception:
            print("ERROR")
        # close file INPUT.txt
        file.close()
