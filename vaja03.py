# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:21:09 2020
VAJA 03@S.I.
rabi: 
@author: mz8202
"""

import numpy as np
import image_handler_v2 as ih
from PIL import Image
import webbrowser


def naloga_1():

    '''
    #maskiranje s pravokotnikom?
    mI = np.zeros_like(I)
    
    x1 = 129 #zgornji levi kot
    y1 = 59
    
    x2 = 154 #spodnji desni kot
    y2 = 139

    
    M = ih.maskRectangle(mI, x1, y1, x2, y2, 1)
    Im = I * M
    ih.displayImage(Im, 'Pravokotno območje')
    
    ih.displayImage(I, 'Pravokotno območje', [129, 154], [59, 139])    
    '''
    

    ih.displayImage(cona, 'Pravokotno območje')

    return
    
def naloga_2():
   
    obmocje = (300, 500)
    
    oblika = cona.shape[ : :-1]
    
    I_0 = ih.interpolate0Image(cona, oblika , obmocje)
    red_0 = I_0[0]
    
    
    a_x = np.arange(300)*I_0[1][0] 
    a_y = np.arange(500)*I_0[1][1]
    
    
    I_1 = ih.interpolate1Image(cona, oblika, obmocje)
    red_1 = I_1[0]
    
    b_x = np.arange(300)*I_1[1][0] 
    b_y = np.arange(500)*I_1[1][1]
    
    
    ih.displayImage(red_0, 'Interpolacija 0. reda', a_x, a_y)
    
    ih.displayImage(red_1, 'Interpolacija 1. reda', b_x, b_y)
    
    return

def naloga_3():
    odg = '''

3. Kaj so prednosti in kaj slabosti interpolacije ničtega reda? 
______________________________________________________________________________________

/.../Interpolacija reda 0 priredi točki (x, y) sivinsko vrednost
najbližje točke na diskretni mreži vzorčnih točk./.../
    
    [PREDNOST: hitra evalvacija]   

Interpolacija reda 0 se hitreje evalvira:
generira edino tiste vrednosti pixlov,
ki že nastopajo v prvotni sliki.

/../ Interpolacija reda 0 je hitro izračunljiva,
vendar nezvezna v točkah, ki so od vzorčnih točk enako oddaljene./../
    
    [SLABOST: pixelacija/artefakti]
    
Torej, če iščem sivinsko vrednost v (x, y) in
je slučajno ta točka med štirimi drugimi ravno na sredi bo tam obdelava nezvezna/sekana.

Na pogled postane slika polna blokov, kjer bi sicer naj imela lepe linije.
Slika se zdi nerazločna in neprijetno nazobčana - je polna artefaktov.
______________________________________________________________________________________



Kaj so prednosti in slabosti interpolacije prvega reda? 
______________________________________________________________________________________

    [PREDNOST: evalvirana slika brez artefaktov interpolacije reda 0]

Interpolacija reda 1 odpravlja slabosti interpolacije reda 0, ker
sivinsko vrednost točke določa kot utež sosednjih štirih vzorčnih točk,
s čimer postane zvezna povsod.
Slika območja postane gladkejša, brez artefaktov: 
bolj je razločna in bolj prijetno - nenazobano deluje.

    [SLABOST: navidezna zveznost & manjši kontrast => popačenje]

Ista rutina naredi sliko zvezno po celi domeni, medtem ko ostane nezvezna
na meji diskretne mreže. Slika nastane zvezna tudi tam, kjer v resnici ni.
Izgubi informacijo jasnih robov - ima manjši kontrast:
razlika med temnim in svetlim je tudi zvezna; slika se popači!
______________________________________________________________________________________



Kaj dosežemo z interpolacijami višjih redov? 
npr. z interpolacijo drugega reda (bikubična interpolacija)?
______________________________________________________________________________________

V kolikor je nujna zveznost odvodov na vsej diskretni mreži, 
potem je nujna interpolacija višjega reda.

Bikubična npr. utež računa kot polinomsko vsoto,
"spline" interpolacije pa s pomočjo polinoma med parom sosednjih točk. 

Z interpolacijo reda 2 ali 3 se slika zdi še bolj zvezna,
bolj gladka: zvezna je po mejah in po celi diskretni mreži.
Slika torej pridobi na kvaliteti.

Vse to pomeni, da poteka bolj zahteven izračun.
Posledično rabi več procesorskega časa in sredstev za evalvacijo.
______________________________________________________________________________________
''' 
    print(odg)
    
    return


def naloga_4():
    odg = '''
    
4. Naštejte nekaj primerov, kjer potrebujemo učinkovito interpolacijo slik.
______________________________________________________________________________________
/.../ Interpolacijo uporabljamo pri številnih postopkih prikazovanja in preslikovanja slik,
kot so tvorjenje prerezov, projekcij in upodobitev, povečevanje slik s povečevanjem vzorčne frekvence,
pri ponovnem enakomernem vzorčenju slik, zajetih z neenakomernim vzorčenjem po posameznih koordinatah, 
ter pri geometrijskih preslikavah slik./.../

    1) sliko povečaj brez, da bi prikrajšal kvaliteto: premajhna slika, ne vidi se dobro ==> zoom in & poglej  (?)  [POVEČAVA]
    
    2) prerez slike: prirezana slika - spremenjena geometrija  (?) [LINIJSKI PREREZ]

    3) (?) :c [ENAKOMERNO VZORČENJE]
    
    4) zavrti sliko, brez artefaktov ==> vsaj interpolacija 1. reda!  (?) [PRESLIKAVA]
    
- vrtenje slike, brez artefaktov
- odpravljanje artefaktov/ ogled brez šuma
- dodajanje raznih efektov (vrtinec, filter ...)
- povečanje slike, brez izgube kvalitete
______________________________________________________________________________________

    '''
    image = Image.open('primeri_uporabe.png')
    image.show()
    print(odg) 
    link = "https://www.unioviedo.es/compnum/labs/labs_pdf/lab05_interpol_images.pdf"
    print("primeri uporabe, src = ", link)
    webbrowser.open(link)
    return


def vse_naloge():
  naloga_1()
  naloga_2()
  naloga_3()
  naloga_4()
  dodatek()
  return


def slika():
    
    ih.displayImage(I, 'Originalna slika')
    
    return

def dodatek():
    nal = '''
Napišite funkcijo za decimacijo (podvzorčenje) slike:
def decimateImage(iImage, iKernel, iLevel)
kjer je iImage slika, ki jo decimirate, iKernel je jedro c(i, j) digitalnega filtra velikosti
M×M, iLevel pa je celoštevilčna stopnja decimacije. Funkcija vrne decimirano sliko oImage.
Decimirajte dano sliko z jedrom c(i, j) digitalnega filtra velikosti M = 1 in M = 2 ter poljubno
celoštevilčno stopnjo decimacije (npr. iLevel=3).
1. Kaj so prednosti in kaj slabosti decimacije?
2. S kakšnim faktorjem upada velikost slike pri decimaciji? S kakšnim faktorjem upada število
podatkov, potrebnih za zapis slike?

3. Kakšne pogoje morajo izpolnjevati koeficienti jedra c(i, j) digitalnega filtra, ki ga upora-
bljate pri decimaciji slike?

4. Če bi želeli pri decimaciji preprosto vzorčiti vsak drugi slikovni element brez zmanjševanja
frekvenčne širine slike, kakšna bi bila v takem primeru oblika in kakšne bi bile vrednosti
jedra c(i, j) digitalnega filtra?    
'''
    print(nal)
    print("\n \n nič ta teden, je bilo dovolj zahtevno :(")
    return

if __name__ == '__main__':
    
    I = ih.loadImage('bled-256x256-08bit.raw', (256, 256), np.uint8)
    
    koordinate = ((129, 59), (129+25, 59+80))
    
    cona = I[koordinate[0][1]:koordinate[1][1] , koordinate[0][0]:koordinate[1][0]]


######################################################################################################################################################################

    #dict nalog in dict funkcij naloga_1... 6
    
    naloga = {1: naloga_1, 2: naloga_2, 3: naloga_3, 4: naloga_4, 5: slika, 6: vse_naloge}
    naloga_opcije = {1: "naloga 1", 2: "naloga 2", 3: "naloga 3", 4: "naloga 4", 5: "Originalna slika", 6: "Vse naloge"}

######################################################################################################################################################################
#UX: izbira naloge
    print("Iz opcij spodaj...")
    #print vse opcije
    for key, val in naloga_opcije.items():
      print (key, "=>", val)
    print("... si izberi številko od 1 do 6 \n prikazale se bodo rešitve \n in se shranile v novo jpg datoteko ali izpisale sem. \n Stisni ENTER za dodatno nalogo =)")       
    ukaz = input("Naloga? (od 1 do 6):     ")
    try:
      naloga_ukaz = int(ukaz)
      naloga.get(naloga_ukaz)()
    except:
      dodatek() 
######################################################################################################################################################################