# -*- coding: utf-8 -*-
"""
Created on Fri Apr  10 19:10:03 2020
VAJA 05@S.I.
@author: mz8202
"""

import numpy as np
import asdf_movie_handler as ih



def naloga_1():
    
    vpr = ''' 
   1) Priložite stranske, čelne in prečne prereze 3D slik:
        pri x = 103, y = 233 in z = 52, in sicer za slike 
        
        oImage, sImage (a = 1, b = −1024), 
        wImage (c = 400, w = 2000), tImage (t = 127) in
        gImage (γ = 2). 
    Velikost slik naj bo prilagojena velikosti slikovnega elementa.
'''
    print(vpr)

    
    ih.displayImage(oImage_s, 'Originalni stranski prerez', oI_gridY, oI_gridZ)
    ih.displayImage(oImage_c, 'Originalni čelni prerez', oI_gridX, oI_gridZ)
    ih.displayImage(oImage_p, 'Originalni prečni prerez', oI_gridX, oI_gridY)
    
    ih.displayImage(sImage_s, 'Linearno preslikani stranski prerez', oI_gridY, oI_gridZ)
    ih.displayImage(sImage_c, 'Linearno preslikani čelni prerez', oI_gridX, oI_gridZ)
    ih.displayImage(sImage_p, 'Linearno preslikani prečni prerez', oI_gridX, oI_gridY)
    
    ih.displayImage(wImage_s, 'Linearno oknjeni stranski prerez', oI_gridY, oI_gridZ)
    ih.displayImage(wImage_c, 'Linearno oknjeni čelni prerez', oI_gridX, oI_gridZ)
    ih.displayImage(wImage_p, 'Linearno oknjeni prečni prerez', oI_gridX, oI_gridY)
    
    ih.displayImage(tImage_s, 'Upragovljeni stranski prerez', oI_gridY, oI_gridZ)
    ih.displayImage(tImage_c, 'Upragovljeni čelni prerez', oI_gridX, oI_gridZ)
    ih.displayImage(tImage_p, 'Upragovljeni prečni prerez', oI_gridX, oI_gridY)
    
    ih.displayImage(gImage_s, 'Gama preslikani stranski prerez', oI_gridY, oI_gridZ)
    ih.displayImage(gImage_c, 'Gama preslikani čelni prerez', oI_gridX, oI_gridZ)
    ih.displayImage(gImage_p, 'Gama preslikani prečni prerez', oI_gridX, oI_gridY)
    
    return
    
def naloga_2():
    
    vpr = ''' 
    
   2) Zapiši dinamično območje: [Lmin . . . Lmax] za slike:
       oImage, sImage, wImage, tImage in gImage. 
       
   Kaj se zgodi pri prikazu slikovnih elementov, 
   ki so izven dinamičnega območja prikaza 8-bitnega monitorja? 
   Obrazloži.
   
'''
    
    print(vpr)
    odg = ''' 
    
    Vrednosti dinamičnih območij vrne computeHistogram: 
        oImage: [0, 1, 2, …, 2391, 2392, 2393]
        sImage: [-1024, -1023, -1022, …, 1367, 1368, 1369]
        wImage: [0, 1, 2, …, 250, 251, 252]
        tImage: [0, 1, 2, …, 255]
        gImage: [0, 1, 2, …, 246, 247, 248]

    Pikslom izven območja dinamike vrednosti med 0 in 255,
    se ob preslikavi pri-/odšteje tista multipla 256,
    da so znova v dinamičnem območju.
    
    Primer: 
        1 piksel; sivinska vrednost = 260 
        preslikava, shranil ==> 260 – 1*256 = vrednost 4  !!
    
    To pomeni, da se slika popači: 
    piksli imajo sedaj spremenjene sivinske vrednosti! 
    
'''
    
    print(odg)
    return
    
def naloga_3():
    
    vpr = ''' 
    
    3. Ali je preslikane slike smiselno uporabljati le za prikazovanje 
    ali tudi za shranjevanje? 
    Obrazloži.
    
''' 
    print(vpr)
    odg = ''' 
    
    Le za prikazovanje:
        sivinska preslikava onemogoči možnost inverzne operacije;
        po preslikavi brezizgubne povrnitve slike v original ni.
    Preostane le, da se originalna slika ohrani z vsemi sivinskimi vrednostmi. 
   
'''
    print(odg)
    return

def naloga_4():
    vpr = ''' 
    
    4. Priloži histograme za 3D slike:
        
        oImage, sImage, wImage, tImage in gImage,
    
    pri čemer za prikaz uporabi funkcijo displayHistogram(). 
    
    Kaj se dogaja s histogrami pri sivinskih preslikavah slik? 
    Obrazloži.
    
''' 
    print(vpr)
    
    odg = ''' 
    
    Iz histograma lahko razberem porazdelitev vrednosti sivin vseh pikslov:    
        
        @ oImage: največkrat piksli okrog vrednosti 0,
        
        @ sImage: ~ -1024 (glede na prvo vse vrednosti zamaknjene -1024)    
    
    Podobno tudi pri wImage, tImage in gImage. 

    Spodnja meja okna = -600, zato se vrednosti iz sImage preslikajo v 0.
    ==> histogram wImage tako kaže več pikslov okrog te vrednosti.
    
        @ tImage: prag = 127 
    
    Večina vrednosti pikslov wImage je manj kot 127, torej se jih največ preslika v 0.
    ==> histogram wImage ima najvišjo gostoto pikslov na vrednosti 0 (višja kot pri ostalih histogramih)
 
    
        @ gImage so vrednosti histograma prepolovljene proti histogramu slike wImage, ker je gama = 2  
   
'''
    print(odg)
    
    o1, o2 = ih.computeHistogram(oImage)
    
    ih.displayHistogram(o1, o2, 'Histogram oImage')
    
    s1, s2 = ih.computeHistogram(sImage)
    
    ih.displayHistogram(s1, s2, 'Histogram sImage')
    
    w1, w2 = ih.computeHistogram(wImage)
    
    ih.displayHistogram(w1, w2, 'Histogram wImage')
    
    t1, t2 = ih.computeHistogram(tImage)
    
    ih.displayHistogram(t1, t2, 'Histogram tImage')
    
    g1, g2 = ih.computeHistogram(gImage)
    
    ih.displayHistogram(g1, g2, 'Histogram gImage')
    
    return



def vse_naloge():
  naloga_1()
  naloga_2()
  naloga_3()
  naloga_4()
  return



if __name__ == '__main__':
    
    # naloži originalno 3D sliko    
    
    iSize = (512, 512, 70)
    oImage = ih.loadImage3D('pelvis-512x512x70-16bit.raw', iSize, np.uint16)

    # določi vektorje mreže oziroma središč slikovnih elementov v milimetrih

    iPixelSize = [0.601563, 0.601563, 3.0] 
    
    oI_gridX = np.arange(iSize[0])*iPixelSize[0]
    oI_gridY = np.arange(iSize[1])*iPixelSize[1]
    oI_gridZ = np.arange(iSize[2])*iPixelSize[2]

   
    # določi in prikaži stranski, čelni in prečni ravninski prerez

    oImage_s = ih.getCrossSection(oImage, 'stranska', 102)
    oImage_c = ih.getCrossSection(oImage, 'celna', 232)
    oImage_p = ih.getCrossSection(oImage, 'precna', 51) 
    
    
    #skaliraj sliko
    
    a = 1
    b = -1024
    
    sImage = ih.scaleImage(oImage, a, b)
    
    sImage_s = ih.getCrossSection(sImage, 'stranska', 102)
    sImage_c = ih.getCrossSection(sImage, 'celna', 232)
    sImage_p = ih.getCrossSection(sImage, 'precna', 51)  
    
    
    #oknenje
    
    c = 400
    w = 2000
    
    wImage = ih.windowImage(sImage, c, w)
    
    wImage_s = ih.getCrossSection(wImage, 'stranska', 102)
    wImage_c = ih.getCrossSection(wImage, 'celna', 232)
    wImage_p = ih.getCrossSection(wImage, 'precna', 51)
    
    
    #upragovljanje
    
    t = 127
    
    tImage = ih.thresholdImage(wImage, t)
    
    tImage_s = ih.getCrossSection(tImage, 'stranska', 102)
    tImage_c = ih.getCrossSection(tImage, 'celna', 232)
    tImage_p = ih.getCrossSection(tImage, 'precna', 51)
    
    #gama preslikava
    
    gamma = 2
    
    gImage = ih.gammaImage(wImage, gamma)
    
    gImage_s = ih.getCrossSection(gImage, 'stranska', 102)
    gImage_c = ih.getCrossSection(gImage, 'celna', 232)
    gImage_p = ih.getCrossSection(gImage, 'precna', 51)
    
    
######################################################################################################################################################################

    #dict nalog in dict funkcij naloga_1... 6
    
    naloga = {1: naloga_1, 2: naloga_2, 3: naloga_3, 4: naloga_4}
    naloga_opcije = {1: "naloga 1", 2: "naloga 2", 3: "naloga 3", 4: "naloga 4"}

######################################################################################################################################################################
#UX: izbira naloge
    print("Iz opcij spodaj...")
    #print vse opcije
    for key, val in naloga_opcije.items():
      print (key, "=>", val)
    print("... si izberi številko od 1 do 4 \n prikazale se bodo rešitve \n in se shranile v novo jpg datoteko ali izpisale sem. \n Stisni ENTER za vse naloge =)")       
    ukaz = input("Naloga? (od 1 do 4):     ")
    try:
      naloga_ukaz = int(ukaz)
      naloga.get(naloga_ukaz)()
    except:
      vse_naloge() 
######################################################################################################################################################################