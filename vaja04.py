# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:32:45 2020
VAJA 04@S.I.
@author: mz8202
"""

import numpy as np
import image_handler_v3 as ih



def naloga_1():
    vpr = ''' 
    
    1. Priložite slike osnovnih ravninskih prerezov 3D slike, 
    in sicer sliko stranskega prereza za slikovni element xc = 69, 
    sliko čelnega prereza za slikovni element yc = 54 in 
    sliko prečnega prereza za slikovni element zc = 104.    
    
    '''
    print(vpr)
    
    stranska_slika = ih.getCrossSection(I, 'stranska', 69)
    ih.displayImage(stranska_slika, "Stranski prerez")
    
    celna_slika = ih.getCrossSection(I, 'celna', 54)
    ih.displayImage(celna_slika, "Čelni prerez")
    
    precna_slika = ih.getCrossSection(I, 'precna', 104)
    ih.displayImage(precna_slika, "Prečni prerez")

    return
    
def naloga_2():
   
    vpr = ''' 
    
   2. Priložite slike stranske, čelne in 
   prečne pravokotne projekcije 3D slike, 
   in sicer za projekcijo največjih vrednosti (MIP) in 
   projekcijo povprečnih vrednosti (AvgIP).  
    
    '''
    
    print(vpr)
    
    stranska_projekcija_mip = ih.getOrthogonalProjection(I, 'stranska', np.max)
    ih.displayImage(stranska_projekcija_mip, "Stranska pravokotna projekcija (MIP)")
    
    celna_projekcija_mip = ih.getOrthogonalProjection(I, 'celna', np.max)
    ih.displayImage(celna_projekcija_mip, "Čelna pravokotna projekcija (MIP)")
    
    precna_projekcija_mip = ih.getOrthogonalProjection(I, 'precna', np.max)
    ih.displayImage(precna_projekcija_mip, "Prečna pravokotna projekcija (MIP)")
    
    stranska_projekcija_avg = ih.getOrthogonalProjection(I, 'stranska', np.mean)
    ih.displayImage(stranska_projekcija_avg, "Stranska pravokotna projekcija (AvgIP)")
    
    celna_projekcija_avg = ih.getOrthogonalProjection(I, 'celna', np.mean)
    ih.displayImage(celna_projekcija_avg, "Čelna pravokotna projekcija (AvgIP)")
    
    precna_projekcija_avg = ih.getOrthogonalProjection(I, 'precna', np.mean)
    ih.displayImage(precna_projekcija_avg, "Prečna pravokotna projekcija (AvgIP)")
        
    return
    
def naloga_3():
    
    vpr = ''' 
    
   3. Katere izmed pravokotnih projekcij 
   MIP, AvgIP, MinIP, MedIP, StdIP in VarIP 
   je v primeru prikazovanja CT slik smiselno računati? 
   Obrazložite odgovor.

    '''
    odg = '''
    
    Projekcija maksimalnih vrednosti omogoča dobro opazovanje skeleta,
    ker so kosti najsvetlejše. S tovrstno kontrastno razliko so kosti posebej poudarjene.
    
    Na CT sliki s projekcijo povprečnih vrednosti pa lahko iz CT slike naredimo simulacijo rentgenskih slik.
    
    Preostale projekcije niso smiselne iz praktičnega vidika, ker so iz njih podrobnosti skeleta nerazvidne.
    
    '''
    print(vpr)
    print(odg)
    
    celna_projekcija_mip = ih.getOrthogonalProjection(I, 'celna', np.max)
    ih.displayImage(celna_projekcija_mip, "Čelna pravokotna projekcija (MIP)")
    
    celna_projekcija_var = ih.getOrthogonalProjection(I, 'celna', np.var)
    ih.displayImage(celna_projekcija_var, "Čelna pravokotna projekcija (var)")
    
    celna_projekcija_avg = ih.getOrthogonalProjection(I, 'celna', np.mean)
    ih.displayImage(celna_projekcija_avg, "Čelna pravokotna projekcija (AvgIP)")
    
    celna_projekcija_median = ih.getOrthogonalProjection(I, 'celna', np.median)
    ih.displayImage(celna_projekcija_median, "Čelna pravokotna projekcija (median)")
    
    celna_projekcija_min = ih.getOrthogonalProjection(I, 'celna', np.min)
    ih.displayImage(celna_projekcija_min, "Čelna pravokotna projekcija (min)")
    
    celna_projekcija_std = ih.getOrthogonalProjection(I, 'celna', np.std)
    ih.displayImage(celna_projekcija_std, "Čelna pravokotna projekcija (std)")
    
    return


def vse_naloge():
  naloga_1()
  naloga_2()
  naloga_3()
  dodatek()
  return


def dodatek():
    #na Win7 ni bilo možno montirati potrebnega paketa whl
    #3. 4. 2020: poskus s pip na linux mint 19
    dod = '''Upodabljanje površine (ang. surface rendering) združuje postopke prikazovanja površine danega
3D objekta oz. strukture. Eden izmed najpogosteje uporabljanih postopkov za upodabljanje
površine je ti. izo-površina (ang. iso-surface). Izo-površino lahko opišemo z mrežo trikotnikov, ki
jih dobimo na primer z algoritmom Marching Cubes. Slednji temelji na sprehajanju po celotnem
področju 3D slike, pri čemer testira, katera oglišča slikovnega elementa (voksla) ležijo v področju
objekta in temu primerno določi trikotnike. Področje objekta lahko določimo z enostavnim
upragovljanjem (ang. thresholding) sivinskih vrednosti. Vrednosti nad pragom pripadajo
objektu, vrednosti pod pragom pa ne. V mapi Gradivo se nahaja krajši primer upodabljanja
površine surfaceRender.py, ki vsebuje grafični vmesnik za določanje praga sivinskih vrednosti.
Raziščite, kaj se dogaja z upodabljanjem površine za različne vrednosti praga sivinskih vrednosti.

Datoteka surfaceRender.py mora biti v isti mapi kot datoteki visible-human.mhd in visible-human-
143x082x193-08bit.raw. Za prikaz grafičnega vmesnika boste potrebovali knjižnici PyQt5 in

VTK v programskem jeziku Python. V kolikor uporabljate različico WinPython64-3.7._.0cod ali
WinPython64-3.7._.0, je knjižnica PyQt5 že nameščena. V tem primeru morate samo namestiti
knjižnico VTK, ki jo dobite na spletni strani https://www.lfd.uci.edu/∼gohlke/pythonlibs/#vtk. Za

Python 3.7 in 64-bitno različico prenesite VTK-8.2.0-cp37-cp37m-win_amd64.whl. Knjižnico name-
stite s pomočjo programa WinPython Control Panel.exe, ki ga najdete v isti mapi kot Spyder.exe.

Datoteko knjižnice dodate z Add packages in nato namestite z Install packages.
    '''
    #print(dod)
    
    return

if __name__ == '__main__':
    
    I = ih.loadImage3D('visible-human-143x082x193-08bit.raw', (143, 82, 193), np.uint8)


######################################################################################################################################################################

    #dict nalog in dict funkcij naloga_1... 6
    
    naloga = {1: naloga_1, 2: naloga_2, 3: naloga_3, 4: vse_naloge}
    naloga_opcije = {1: "naloga 1", 2: "naloga 2", 3: "naloga 3", 4: "Vse naloge"}

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