import argparse


def dodawanie(x):
    suma = 0
    for x in argumenty.x:
        suma += x
    return suma

def odejmowanie(x):
    roznica = 2 * argumenty.x[0]
    for x in argumenty.x:
        roznica -= x
    return roznica

def mnozenie(x):
    iloczyn = 1
    for x in argumenty.x:
        iloczyn *= x
    return iloczyn

def dzielenie(x):
    iloraz = pow(argumenty.x[0], 2)
    for x in argumenty.x:
        iloraz /= x
    return iloraz

parser = argparse.ArgumentParser()
parser.add_argument('x', help="numer/-y", type = int, nargs='*')
parser.add_argument('-sum', help="dodawanie", action = "store_true")
parser.add_argument('-odej', help="odejmowanie", action = "store_true")
parser.add_argument('-mnoz', help="mnozenie", action = "store_true")
parser.add_argument('-dzie', help="dzielnie", action = "store_true")

argumenty = parser.parse_args()

if argumenty.sum:
    print(dodawanie(argumenty.x), "<- suma")

if argumenty.odej:
    print(odejmowanie(argumenty.x), "<- roznica")

if argumenty.mnoz:
    print(mnozenie(argumenty.x), "<- iloczyn")

if argumenty.dzie:
    print(dzielenie(argumenty.x), "<- iloraz")