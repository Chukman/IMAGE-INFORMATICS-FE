# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:34:32 2020
VAJA 01@S.I.
rabi head-CT && head-MR sliki
@author: mz8202
"""
from PIL import Image,ImageDraw
import numpy as np
import matplotlib.pyplot as pp

#iz vaja00:
# funkcija, ki nalozi sliko iz lokalnega direktorija
def loadImage(iPath, iSize, iType):
    #nalozi slikco
    
    fid = open(iPath, 'rb')
    oImage = np.ndarray((iSize[1], iSize[0]),
                        dtype = iType, 
                        buffer = fid.read())
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html
    fid.close()        
    return oImage

#funkcija za prikaz slik
def displayImage(iImage, iTitle):
    
    pp.figure()
    pp.title(iTitle)
    pp.imshow(iImage,
              cmap = pp.cm.gray,
              vmin = 0, #https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.pyplot.scatter.html
              vmax = 255,
              extent = (0-0.5, iImage.shape[1] - 0.5, 
              iImage.shape[0] - 0.5, 0 - 0.5))
    pp.show()
    

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

def saveImage(iImage, iPath, iType):
    
    fid = open(iPath, 'wb')
    oImage = np.array(iImage, dtype = iType) #sprememba podatkovnega tipa
    fid.write(oImage.tobytes())
    fid.close()    



def naloga_1():
    navodila1="""
\n 1. Priložite sliko maske v obliki pravokotnika ter sliko rezultata maskiranja CT slike z
masko v obliki pravokotnika. Za parametre pravokotnika uporabite (x1, y1) = (165, 150) in
(x2, y2) = (225, 355).
"""
    print(navodila1)
    
    #maskiraj s pravokotnikom
    x1 = 165    #zgornji levi kot
    y1 = 150
    x2 = 225    #spodnji desni kot
    y2 = 355
    
    ctM = maskRectangle(mI, x1, y1, x2, y2, 1) #binarna - maskiranje je binarno
    ctIm = ctI * ctM
    displayImage(ctIm, 'Maskirana CT slika (pravokotnik)')
    
    #shrani sliko
    pp.imsave('Maskirana_CT_slika_pravokotnik.jpg', ctIm)

    return
    
def naloga_2():
    navodila2 = """
\n 2. Priložite sliko maske v obliki elipse ter 
sliko rezultata maskiranja MR slike z masko v obliki elipse. 
Za parametre elipse uporabite (x, y) = (190, 130), a = 120 in b = 100.
"""
    print(navodila2)
    # maskiraj z elipso
    x0 = 190
    y0 = 130
    a0 = 120
    b0 = 100
    
    
    eM = maskEllipse(mI, x0, y0, a0, b0, 255)
    #displayImage(eM, 'Maska v obliki elipse!')

    mrM = maskEllipse(mI, x0, y0, a0, b0, 1)
    
    mrIm = mrI * mrM
    
    displayImage(mrIm, 'Maskirana MR slika (elipsa)')

    #shrani sliko
    pp.imsave('Maskirana_MR_slika_elipsa.jpg', mrI)

    return
    
def naloga_3():
    
    navodila3 = """
\n 3. Priložite sliko maske, ki ste jo pridobili z združevanjem maske v obliki pravokotnika in
maske v obliki elipse. Za parametre pravokotnika in elipse uporabite enake parametre kot
pri predhodnih vprašanjih. Priložite sliko rezultata maskiranja CT slike in sliko rezultata
maskiranja MR slike s tako dobljeno združeno masko.
"""

    print(navodila3)

    #3. naloga: zdruzi maski v novo masko; ohrani parametre; maskiranju primerne vrednosti
    
    ctM = maskRectangle(mI, x1, y1, x2, y2, 255)
    ctM = maskEllipse(ctM, x0, y0, a0, b0, 255)
    
    #displayImage(ctM, 'Kombinirana maska (pravokotnik & elipsa)')
    
    ctM = maskRectangle(mI, x1, y1, x2, y2, 1)
    ctM = maskEllipse(ctM, x0, y0, a0, b0, 1)
    
    ctIm = ctI * ctM
    
    mrIm = mrI * ctM
    
    displayImage(ctIm, 'Maskirana CT slika (zdruzena maska)')
    displayImage(mrIm, 'Maskirana MR slika (zdruzena maska)')
    
    #shrani sliki
    
    pp.imsave('Maskirana_CT_slika_zdruzena_maska.jpg', ctIm)
    pp.imsave('Maskirana_MR_slika_zdruzena_maska.jpg', mrIm)

    return
    
def naloga_4():
    navodila4 = """
\n 4. Priložite sliko maske v obliki šahovnice diagonalnih in antidiagonalnih polj. 
Za parametre šahovnice uporabite w = 60 in h = 40, vrednost maske pa nastavite prikazu primerno.
"""  
    print(navodila4)
   
    #naloga 4: maska v obliki šahovnice!

    w = 60
    h = 40
    chsM = maskChessboard(mI, w, h, 0, 255) 
    displayImage(chsM, 'Maska v obliki šahovnice')
    
    #shrani sliko
    pp.imsave('Maska_v_obliki_sahovnice.jpg', chsM)

    return
    
def naloga_5():
    
    navodila5 = """
\n 5. Priložite sliko, ki ste jo pridobili z združitvijo CT slike, 
maskirane z masko v obliki šahovnice diagonalnih polj, ter MR slike,
maskirane z masko v obliki šahovnice antidiagonalnihpolj. 
Za parametre šahovnice obakrat uporabite w = 60 in h = 40.
"""
    
    print(navodila5)
    
    #naloga 5: CT sliko kaži z masko šahovnice diagonalno, MR pa antidiagonalna polja 
    
    ctM = maskChessboard(mI, w, h, 1, 0)
    mrM = maskChessboard(mI, w, h, 0, 1) 
    
    ctIm = ctI * ctM
    mrIm = mrI * mrM
    displayImage(ctIm, 'Maskirana CT slika (šahovnica)')
    displayImage(mrIm, 'Maskirana MR slika (šahovnica)')
    
    #shrani sliki
    
    pp.imsave('Maskirana_CT_slika_sahovnica.jpg', ctIm)

    pp.imsave('Maskirana_MR_slika_sahovnica.jpg', mrIm)

    return
    
def naloga_6():

    navodila6 = """
\n 6. Sinteza maskirane CT in maskirane MR slike 
v obliki komplementarne šahovnice 
omogoča prikazovanje razlik med slikama.
Na kakšen način bi še lahko prikazali 
razliko med slikama in 
na kaj je potrebno paziti pri takem prikazovanju? 
Obrazložite odgovor.
    """
    
    print(navodila6) 

    #naloga 6: združi sliki maskirani s šahovnico diag in antidiag.
    
    ctM = maskChessboard(mI, w, h, 1, 0)
    mrM = maskChessboard(mI, w, h, 0, 1) 

    ctIm = ctI * ctM
    mrIm = mrI * mrM
    
    #nova, sintetizirana slika
    sIm = ctIm + mrIm

    displayImage(sIm, 'Združeni CT & MR')
    
    #shrani sliko

    pp.imsave('Združeni CT & MR.jpg', sIm)
    
    odgovor =  """
\n K 6. nalogi: obrazlaga prikaza razlik med slikami
a) številsko
b) vizualno

a)

Razlika dveh slik pomeni odštevanje istoležnih 
slikovnih elementov, hranjenih v arrayu (pikslov).

To je možno le, če so pretvorjeni v float format:
sicer pride do preskoka čez 255 (vrh lestve možnih vrednosti; prevrtenje vrednosti).

Če 8-bitna slika (255 vrednosti per piksel), se lahko zgodi
da je vrednost določenega piksla (istoležni!) manjša od parnega,
na sliki, s katero odštevam.

Z nastalim arrayem razlik nato še ugotovim normo (norma vektorja);
iz norme pa razliko dveh slik (številska vrednost).


b)
Sliko bi lahko prikazal tudi z odštevanjem elementov arraya pikslov obeh slik.
To najbrž pomeni, da bo tokrat vsaka vrednost manjša od nič ostala nič (ne pride do vrtenja)
Vse kar je temno sivkasto na prvi sliki bo na novi dejansko črnina ali belina.
"""

    print(odgovor)
    
    sctIR = mrIm - ctIm
    sImR = ctIm - mrIm
        
    displayImage(sctIR, 'Razlika MR - CT')
    displayImage(sImR, 'Razlika slik CT - MR')
    
    
    #shrani sliki
    pp.imsave('Razlika_MR_CT.jpg', sctIR)
        
    pp.imsave('Razlika_CT_MR.jpg', sImR)

    return


def vse_naloge():
  naloga_1()
  naloga_2()
  naloga_3()
  naloga_4()
  naloga_5()
  naloga_6()
  return
'''
def dodatno():
    x1 = 230
    x2 = 50
    x3 = 300

    y1 = 20
    y2 = 250
    y3 = 340
    
    X_ = [x1, x2, x3]
    Y_ = [y1, y2, y3]
    

    tr = maskTriangle(mI, X_, Y_, 255)
 
    displayImage(tr, 'Maska v obliki trikotnika!')
    
    #shrani sliko
    pp.imsave('Maska_v_obliki_trikotnika.jpg', tr)
    
#maska v obliki trikotnika

def maskTriangle(iMask, iX, iY, iValue):
  #https://www.iue.tuwien.ac.at/phd/ertl/node114.html
  #https://www.triangle-calculator.com/?what=vc&a=230&a1=20&3dd=3D&a2=&b=50&b1=250&b2=&c=300&c1=340&c2=&submit=Solve&3d=0
  
  #x1, y1
  x1 = iX[0]
  y1 = iY[0]
  
  #x2, y2
  x2 = iX[1]
  y2 = iY[1]

  #x3, y3
  x3 = iX[2]
  y3 = iY[2]
  
  #for line in oMask:
  #oMask[(X//iW + Y//iH)%2 == 0] = iValue1
  
  #X, Y = np.meshgrid(np.arange(iMask.shape[1]), np.arange(iMask.shape[0]))
  
  #oMask[iY, (iX)%3 +1 == 1 ] = iValue
  
  # Create empty black canvas
  im = Image.new('RGB', (255, 255))

  # Draw red and yellow triangles on it and save
  
  draw = ImageDraw.Draw(im)
  
  lel = draw.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = (255,255,255))
  
  #oMask = np.array(iMask)

  #oMask = lel
  
  #displayImage(lel, 'result!')
  pp.imsave('triangle_mask.jpg', lel)

  #TRI = loadImage('result.jpg', (380, 358), np.uint8)
  
  #print(TRI)
  
  return TRI


    return
'''
def dodatno():
  x1 = 230
  x2 = 50
  x3 = 300
  y1 = 20
  y2 = 250
  y3 = 340
  
  im = Image.new('RGB', (255, 255))

  
  draw = ImageDraw.Draw(im)
  
  lel = draw.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = (255,255,255))
  im.save('result.png')
  im.show('result.png')
  return


#main
if __name__ == '__main__':
    
    ctI = loadImage('head-CT-380x358-08bit.raw', (380, 358), np.uint8)
    #displayImage(ctI, 'CT slika')
    mrI = loadImage('head-MR-380x358-08bit.raw', (380, 358), np.uint8)
    #displayImage(mrI, 'MR slika')
    mI = np.zeros_like(ctI)  #generira polje ničel (dim = ctI)
    
    naloga = {1: naloga_1, 2: naloga_2, 3: naloga_3, 4: naloga_4, 5: naloga_5, 6: naloga_6, 7: vse_naloge}
    
    naloga_opcije = {1: "naloga 1", 2: "naloga 2", 3: "naloga 3", 4: "naloga 4", 5: "naloga 5", 6: "naloga 6", 7: "vse naloge"}

############################################################################################################################

#input prompt za izbiro naloge (int input)

    print("Iz opcij spodaj...")
    #print vse opcije
    for key, val in naloga_opcije.items():
      print (key, "=>", val)

    print("... si izberi številko od 1 do 7 \n prikazala se bo rešitev (slika) \n in se shranila v novo jpg datoteko. \n (easter egg, če pustiš prazno =)")       
    
    ukaz = input("Naloga? (od 1 do 7):     ")

    try:
      naloga_ukaz = int(ukaz)
      naloga.get(naloga_ukaz)()
    except:
      dodatno()
    
############################################################################################################################
    
