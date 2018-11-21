from czech_stemmer import *
import nltk
from data import *

def vytvor_features(slovo):
    return {slovo: True}

def vytvor(pesnicka):
    slova = pesnicka.lower().split()
    ostemovaneSlova = []
    stopSlova = nacitajStopSlova()

    for slovo in slova:
            slovo = ''.join(re.split(r'[-.;!?,)(]', slovo))
            if slovo not in stopSlova:
                ostemovaneSlova.append(cz_stem(slovo))

    return dict(('%s' % w, True) for w in ostemovaneSlova)

def vytvorKlasifikator(train_set):
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    return classifier


def clasifikuj(clf, pesnicka):
    list = clf.prob_classify(vytvor(pesnicka))

    print('Pesnicka je rychla s pravdepodobnostou:', list.prob('rychle')*100)
    print('Pesnicka je pomala s pravdepodobnostou:', list.prob('pomale')*100)

    return clf.classify(vytvor(pesnicka))

