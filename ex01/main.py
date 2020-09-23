# -*- coding: utf-8 -*-

def handling(a, b):
    temps = a
    dist = b
    try:
        v = dist/temps
    except ZeroDivisionError:
        print("ERROR")
    else:
        return v


if __name__ == '__main__':
    try:
        file = open("INPUT.TXT", "r")
    except FileNotFoundError:
        print("ERROR")
    else:
        for lines in file.readlines():
            try:
                tab = lines.split(";")
                if len(tab) != 2:
                    raise Exception
                temps = float(tab[0])
                dist = float(tab[1])

            except Exception:
                print("ERROR")

            else:
                try:
                    print('{:.1f}'.format(handling(temps, dist)))
                except Exception:
                    print("ERROR")
        file.close()
