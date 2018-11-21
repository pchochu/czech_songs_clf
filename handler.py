from klasifikator import *
import random

def klasifikuj(pesnicka):

    pomale = dajSlovaPesniciek('texty/pomale')
    rychle = dajSlovaPesniciek('texty/rychle')

    ostemovanePomale = []
    ostemovaneRychle = []

    for slovo in pomale:
        ostemovanePomale.append(tuple([(cz_stem(slovo)), 'pomale']))

    for slovo in rychle:
        ostemovaneRychle.append(tuple([(cz_stem(slovo)), 'rychle']))

    vsetkySlova = ostemovanePomale + ostemovaneRychle

    featuresets = [(vytvor_features(slovo), typ) for (slovo, typ) in vsetkySlova]
    random.shuffle(featuresets)

    train_set = featuresets[:7000]
    test_set = featuresets[7000:]

    classifier = vytvorKlasifikator(train_set)

    print('------------------------')
    result = (clasifikuj(classifier, pesnicka))
    print('------------------------')
    if result is 'rychle':
        print('Pesnicka je rychla')
    else:
        print('Pesnicka je pomala')




