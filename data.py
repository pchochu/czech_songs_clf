import os
import re
import glob
import errno

def nacitajData(cesta):
    cestaKuTextom = os.path.abspath(cesta)
    vsetkyTexty = os.path.join(cestaKuTextom, '*.txt')
    texty = glob.glob(vsetkyTexty)

    slovaPesniciek = []
    celePesnicky = []

    for text in texty:
        try:
            with open(text, 'r') as file:
                celePesnicky.append(file.read())
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise

    for pesnicka in celePesnicky:
        riadkyPesnicky = []
        rozdelenaPesnicka = pesnicka.splitlines()
        for riadok in rozdelenaPesnicka:
            if riadok not in riadkyPesnicky:
                riadkyPesnicky.append(riadok)
                for slovo in riadok.split():
                    bezInterpunkcie = ''.join(re.split(r'[-.;!?,]', slovo))
                    #bezDiaAInter = unidecode.unidecode(bezInterpunkcie)
                    #slovaPesniciek.append(bezDiaAInter.lower())
                    slovaPesniciek.append(bezInterpunkcie.lower())

    return slovaPesniciek

def nacitajStopSlova():
    cestaKuStopWords = os.path.abspath('stopWords')
    nazovStopWords = os.path.join(cestaKuStopWords, 'stop.txt')
    stopSlova = []

    with open(nazovStopWords, 'r') as file:
        for riadok in file:
            for slovo in riadok.split():
                #slovoBezDia = unidecode.unidecode(slovo)
                #slovoBezDia.lower()
                #stopSlova.append(slovoBezDia)
                stopSlova.append(slovo)

    return stopSlova

def dajSlovaPesniciek(cesta):

    slova = nacitajData(cesta)

    slovaVsetky = []
    stopSlova = nacitajStopSlova()

    pesnickaBezStop = []

    for slovo in slova:
        if slovo not in stopSlova and slovo != "":
            pesnickaBezStop.append(slovo.lower())
            slovaVsetky.append(slovo)


    return pesnickaBezStop