# -*- coding: utf-8 -*-
"""
..module:: ex01
    :synopsis:: Définir la liste : liste =[17, 38, 10, 25, 72],
             puis effectuez les actions suivantes :
            – triez et affichez la liste ;
            – ajoutez l’élément 12 à la liste et affichez la liste ;
            – renversez et affichez la liste ;
            – affichez l’indice de l’élément 17 ;
            – enlevez l’élément 38 et affichez la liste ;
            – affichez la sous-liste du 2ème au 3ème élément ;
            – affichez la sous-liste du début au 2e élément
            – affichez la sous-liste du 3e élément à la fin de la liste ;
            – affichez la sous-liste complète de la liste ;
            – affichez le dernier élément en utilisant un indexage négatif.
"""

import sys


class ex09:
    """
    ..class:: Class contains the function for the exercise 9

    """

    def __init__(self):
        """
        ..function: definition of the initials values for the list

        """
        self.liste = [17, 38, 10, 25, 72]

    def getList(self):
        """
        ..function: Function that returns the value of the public variable 'liste'

        :return liste: list public variable
        """
        return self.liste

    def action(self, operation, element=0):
        """
        ..function: Function that returns a list after the realisation of operation defined,
                    like add, remove, reverse, sort, ...

        :param operation: type of operation to realize
        :param element: the element to permit to realize the operation

        :return res: the new list or the element extract of the list
        """
        try:
            res = ""
            if operation == 'add':
                self.liste.append(element)
                res = self.getList()
            elif operation == 'remove':
                self.liste.remove(element)
                res = self.getList()
            elif operation == 'reverse':
                self.liste.reverse()
                res = self.getList()
            elif operation == 'sort':
                self.liste.sort()
                res = self.getList()
            elif operation == 'printE':
                res = self.liste[element]
            elif operation == 'printI':
                res = self.liste.index(element)
            return res
        except:
            print("ERROR")

    def subList(self, firstElement, secundElement):
        """
        ..function: Function that returns different type of sub-list

        :param firstElement: the first element to define the sub-list
        :param secundElement: the other element to define the sub-list

        :return res: the sub-list defined
        """
        try:
            l = self.liste
            res = ""
            if isinstance(firstElement, int):
                if isinstance(secundElement, int):
                    res = l[int(firstElement):int(secundElement)]
                elif secundElement == 'oui':
                    res = l[int(firstElement):]
                else:
                    raise Exception
            elif firstElement == 'oui':
                if isinstance(secundElement, int):
                    res = l[:int(secundElement)]
                elif secundElement == 'oui':
                    res = l[::]
                else:
                    raise Exception
            else:
                res = l[int(firstElement):int(secundElement)]
            return res
        except Exception:
            print("ERROR")
            raise Exception


# main function
if __name__ == '__main__':
    # open file TEST.py
    try:
        nameFile = sys.argv[1]
        file = open(nameFile, "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        try:
            exo9 = ex09()
            print(exo9.action('sort'))
            print(exo9.action('add', 12))
            print(exo9.action('reverse'))
            print(exo9.action('printI', 17))
            print(exo9.action('remove', 38))
            print(exo9.subList(1, 3))
            print(exo9.subList('oui', 2))
            print(exo9.subList(2, 'oui'))
            print(exo9.subList('oui', 'oui'))
            print(exo9.action('printE', -1))
        except:
            print("ERROR")
        # close file INPUT.txt
        file.close()
