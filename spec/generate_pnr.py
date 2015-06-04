#encoding: utf-8

from future_builtins import map

def generate(birth_date, country, organ):
    """
    :param birth_date: Datum då personen föddes, Array
    :param country: Län där personen föddes, String
    :param organ: Personens könsorgan, String
    :return: Personens personnummer
    """
    personnummer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    personnummer[0] = birth_date[0]
    personnummer[1] = birth_date[1]
    personnummer[2] = birth_date[2]
    personnummer[3] = birth_date[3]
    personnummer[4] = birth_date[4]
    personnummer[5] = birth_date[5]

    if organ == "vagina":
        personnummer[8] = 8
    elif organ == "penis":
        personnummer[8] = 7
    else:
        print "Unknown Organ"

    if country == "skaraborg":
        personnummer[6] = 6
        personnummer[7] = 0



    first = personnummer[0]
    second = personnummer[1]
    third = personnummer[2]
    fourth = personnummer[3]
    fifth = personnummer[4]
    sixth = personnummer[5]
    seventh = personnummer[6]
    eighth = personnummer[7]
    ninth = personnummer[8]
    tenth = personnummer[9]

    value_first = first * 2
    value_second = second * 1
    value_third = third * 2
    value_fourth = fourth * 1
    value_fifth = fifth * 2
    value_sixth = sixth * 1
    value_seventh = seventh * 2
    value_eighth = eighth * 1
    value_ninth = ninth * 2


    if value_first >= 10:
        value_first=sum(map(int, str(value_first)))

    if value_second >= 10:
        value_second=sum(map(int, str(value_second)))

    if value_third >= 10:
        value_third=sum(map(int, str(value_third)))

    if value_fourth >= 10:
        value_fourth=sum(map(int, str(value_fourth)))

    if value_fifth >= 10:
        value_fifth=sum(map(int, str(value_fifth)))

    if value_sixth >= 10:
        value_sixth=sum(map(int, str(value_sixth)))

    if value_seventh >= 10:
        value_seventh=sum(map(int, str(value_seventh)))

    if value_eighth >= 10:
        value_eighth=sum(map(int, str(value_eighth)))

    if value_ninth >= 10:
        value_ninth=sum(map(int, str(value_ninth)))


    summ = value_first + value_second + value_third + value_fourth + value_fifth + value_sixth + value_seventh + value_ninth + tenth

    summ=(map(int, str(summ)))
    if summ[1] == 0:
        personnummer[9] = 0
    if summ[1] == 1:
        personnummer[9] = 9
    if summ[1] == 2:
        personnummer[9] = 8
    if summ[1] == 3:
        personnummer[9] = 7
    if summ[1] == 4:
        personnummer[9] = 6
    if summ[1] == 5:
        personnummer[9] = 5
    if summ[1] == 6:
        personnummer[9] = 4
    if summ[1] == 7:
        personnummer[9] = 3
    if summ[1] == 8:
        personnummer[9] = 2
    if summ[1] == 9:
        personnummer[9] = 1




    print personnummer

generate(birth_date=[9, 7, 0, 4, 2, 2], country="skaraborg", organ = "penis")