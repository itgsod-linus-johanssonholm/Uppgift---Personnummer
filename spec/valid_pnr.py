#encoding: utf-8

from future_builtins import map

def valid(personnummer):
    """
    Personnummersvalideraren

    :param Personnummer: Array

    :Return: Valid or Invalid
    """

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

    #sätter variabler till varje siffra i personnumret

    value_first = first * 2
    value_second = second * 1
    value_third = third * 2
    value_fourth = fourth * 1
    value_fifth = fifth * 2
    value_sixth = sixth * 1
    value_seventh = seventh * 2
    value_eighth = eighth * 1
    value_ninth = ninth * 2

    #mulitplicerar dessa värden på rätt sätt

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

    #sätter de multiplicerade värdena till två stycken ensiffriga tal om de är tvåsiffriga

    summ = value_first + value_second + value_third + value_fourth + value_fifth + value_sixth + value_seventh + value_ninth + tenth

    #plussar ihop alla talen

    if summ % 10 == 0:
        print "Valid"
    else:
        print "Invalid"

    #kontrollerar om talen är jämnt delbara med tio

personnummer = [9, 7, 0, 4, 2, 2, 6, 0, 7, 6]
valid(personnummer)