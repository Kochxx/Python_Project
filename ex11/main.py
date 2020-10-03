"""
..module:: ex11
    :synopsis:: Utilisez une liste en compréhension pour obtenir
        la liste ['ad', 'ae', 'bd', 'be', 'cd', 'ce'] à partir
        des chaînes "abc" et "de"
"""
import sys


def sortList(firstString, secondString):
    """
    ..function: function that is using a list of comprehension
                taking two string and merging them into a table

    :param firstString: first string to be merged
    :param secondString: second string to be merged

    :return the comprehension list 
    """
    return [firstElement + secondElement for firstElement in firstString for secondElement in secondString]


# main function
if __name__ == '__main__':
    try:
        print(sortList("abc", "de"))
    except:
        print("ERROR")
