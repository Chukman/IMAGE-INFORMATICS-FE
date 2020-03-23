# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:21:34 2020
VAJA 02@S.I.
@author: mz8202
"""
import numpy as np
import matplotlib.pyplot as pp

def displayImage(iImage, iTitle):
    pp.figure()
    pp.title(iTitle)
    pp.imshow(iImage, cmap=pp.cm.gray, vmin=0, vmax=255)
    pp.show()
    pp.savefig(iTitle)
    print("Shranil: ", iTitle, "\n")


def loadImage(iPath, iSize, iType):
    fid = open(iPath, 'rb')
    oImage = np.ndarray(
            (iSize[1],iSize[0]),
            dtype=iType,
            buffer=fid.read()
            )
    fid.close()
    return oImage

'''
#shrani sliko

def saveImage(iImage, iPath, iType):
    
    fid = open(iPath, 'wb')
    oImage = np.array(iImage, dtype = iType) #sprememba podatkovnega tipa
    fid.write(oImage.tobytes())
    fid.close()
'''  
#Izračun histograma.

def computeHistogram(iImage):
   # poišči najmanjšo in največjo sivinsko vrednost
   minL = int(np.floor(iImage.min()))
   maxL = int(np.ceil(iImage.max()))
   # definicija središč razredov histograma
   oLevels = np.arange(minL, maxL + 1)
   # izračun histograma
   oHist = np.zeros((oLevels.size, ))
   for y in range(iImage.shape[0]):
       for x in range(iImage.shape[1]):
           v = int(round(iImage[y, x]))
           idx = v - minL
           oHist[idx] += 1
   # vrni vektor histograma
   return oHist, oLevels

#Prikaz histograma slike.

def displayHistogram(iHist, iLevels, iTitle):
    pp.figure()
    pp.title(iTitle)
    pp.bar(iLevels, iHist, width=1, edgecolor='darkred', color='red')
    pp.xlim((min(0, iLevels.min()) - 0.5, max(255, iLevels.max()) + 0.5))
    pp.ylim((0, 1.05*iHist.max()))
    pp.savefig(iTitle)
    print("Shranil: ", iTitle, "\n")

#maska v obliki pravokotnika
  
def maskRectangle(iMask, iX1, iY1, iX2, iY2, iValue):
    oMask = np.array(iMask)
    oMask[iY1:iY2 +1, iX1:iX2 +1] = iValue
    return oMask

#maska v obliki elipse

def maskEllipse(iMask, iX, iY, iA, iB, iValue):
    oMask = np.array(iMask)
    X, Y = np.meshgrid(np.arange(iMask.shape[1]), np.arange(iMask.shape[0]))
    oMask[((X-iX)/iA)**2 + ((Y-iY)/iB)**2 <= 1] = iValue
    return oMask

#k nalogi 6: maska v obliki šahovnice! ==> diagonalna in antidiagonalna polja

def maskChessboard(iMask, iW, iH, iValue1, iValue2):
    oMask = np.array(iMask)
    X, Y = np.meshgrid(np.arange(iMask.shape[1]), np.arange(iMask.shape[0]))
    oMask[(X//iW + Y//iH)%2 == 0] = iValue1 #diagonalna in
    oMask[(X//iW + Y//iH)%2 == 1] = iValue2 #antidiagonalna polja
    return oMask

def addNoise(iImage, iStd):

    row,col = iImage.shape
    var = 0.1
    sigma = var**0.5

    oNoise = np.random.normal(iStd,sigma,(row,col))
    oNoise = oNoise.reshape(row,col)

    oImage = iImage + oNoise

    return oImage, oNoise


'''


Napišite funkcijo, ki sliki doda aditiven Gaussov šum:
def addNoise(iImage, iStd)
kjer je iImage slika, kateri se dodaja Gaussov šum, iStd pa standardni odklon dodanega
šuma (povprečna amplituda dodanega šuma je μ = 0), ki ga modelirate s pomočjo funkcije
numpy.random.randn(). Funkcija naj vrne sliko z dodanim šumom oImage ter matriko doda-
nega šuma oNoise (matrika ima enake dimenzije kot slika).

• Opazujte slike, pripadajoče histograme ter razmerja signal/šum pri slikah z dodanim šu-
mom različnih standardnih odklonov.

• Na kaj morate biti pozorni pri prikazovanju slike šuma in pri računanju pripadajočega
histograma?

• Kako dodajanje šuma na sliko vpliva na obliko pripadajočega histograma ter na diferenci-
alno razmerje signal/šum SNRD?
'''