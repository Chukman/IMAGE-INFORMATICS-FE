# -*- coding: utf-8 -*-
"""
Created on Fri May 15 17:11:54 2020
VAJA 10@S.I.
@author: mz8202
"""

import numpy as np
import handlerinatorinator as ih



def naloga_1():
    # naloži in prikaži sliko
    I = ih.loadImage('coins-300x246-08bit.raw', (300, 246), np.uint8)
    ih.displayImage(I, 'Originalna slika')
    # upragovljanje slike
    tI = ih.thresholdImage(I, 80)
    ih.displayImage(tI, 'Upragovljena slika')
    # označevanje slike
    lI = ih.labelImage(tI)
    ih.displayImage(lI*25, 'Označena slika')
    print('Število oznak na sliki: ', lI.max())
    # barvno kodiranje označene slike
    cI = ih.encodeColors(lI)
    ih.displayImage(cI, 'Barvno kodirana označena slika')
    
    return

def naloga_2():

    # naloži in prikaži sliko
    I = ih.loadImage('coins-300x246-08bit.raw', (300, 246), np.uint8)
    ih.displayImage(I, 'Originalna slika')
    
    # upragovljanje slike prag = 70
    tI = ih.thresholdImage(I, 70)
    ih.displayImage(tI, 'Upragovljena slika')
    
    # označevanje slike
    lI = ih.labelImage(tI)
    ih.displayImage(lI*25, 'Označena slika')
    print('Število oznak na sliki: ', lI.max())

   
    
    # upragovljanje slike prag = 90
    tI = ih.thresholdImage(I, 90)
    ih.displayImage(tI, 'Upragovljena slika')
    
    # označevanje slike
    lI = ih.labelImage(tI)
    ih.displayImage(lI*25, 'Označena slika')
    print('Število oznak na sliki: ', lI.max())

    return



def naloga_3():
    
    I = ih.loadImage('coins-300x246-08bit.raw', (300, 246), np.uint8)
    #iz vaje02:
    # območje zanimanja
    areaS1 = ((0, 0), (299, 245), 'S1')

    S1 = I[areaS1[0][1]:areaS1[1][1] + 1, areaS1[0][0]:areaS1[1][0] + 1]

    # izračun histograma
    #kje so sivine?
    histogram, nivo = ih.computeHistogram(S1)

    ih.displayHistogram(histogram, nivo, 'Histogram: iščem optimalni prag za ločevanje slike na ozadje in ospredje!')
    
    
    ozadje = ih.determineThreshold(I, 80, 0.2)
    ospredje = ih.determineThreshold(I, 160, 0.2)
    
    prag = (ozadje + ospredje) / 2

    print("Optimalna vrednost pragu: ", prag)
    return

def vse_naloge():
  naloga_1()
  naloga_2()
  naloga_3()
  return


if __name__ == '__main__':

######################################################################################################################################################################

    #dict nalog in dict funkcij naloga_1... 6
    
    naloga = {1: naloga_1, 2: naloga_2, 3: naloga_3}
    naloga_opcije = {1: "naloga 1", 2: "naloga 2", 3: "naloga 3"}

######################################################################################################################################################################
#UX: izbira naloge
    print("Iz opcij spodaj...")
    #print vse opcije
    for key, val in naloga_opcije.items():
      print (key, "=>", val)
    print("... si izberi številko od 1 do 3 \n prikazale se bodo rešitve \n in se izpisale sem. \n Stisni ENTER za vse naloge naenkrat!")       
    ukaz = input("Naloga? (od 1 do 3):     ")
    try:
      naloga_ukaz = int(ukaz)
      naloga.get(naloga_ukaz)()
    except:
      vse_naloge() 
######################################################################################################################################################################