# -*- coding: utf-8 -*-
"""
Created on Fri Apr  24 09:05:55 2020
VAJA 07@S.I.
@author: mz8202
"""

import numpy as np
import asdf_movie_handler as ih



def naloga_1():
    vpr = ''' 
    
    1. Zapišite jedro filtra velikosti N×N = 5×5:
        za glajenje z aritmetičnim povprečjem, 
        za glajenje z uteženim povprečjem ter 
        za glajenje z Gaussovim jedrom pri σ = 2.   
   
'''
    print(vpr)
    Gauss_jedro = ih.gauss_jedro_filtra((5,5), 2)
    odg0 = '''
    Gaussovo jedro za glajenje.
    '''
    print(odg0)

    print(Gauss_jedro)
    
    matrika_enic = np.full((5,5), 1)
    
    odg1 = '''
    Jedro za glajenje z aritmetičnim povprečjem.
    '''
    print(odg1)

    print(matrika_enic)
    
    odg2 = '''
    Jedro za glajenje z uteženim povprečjem.
    '''
    print(odg2)
    
    rocna_matrika = [[1, 4, 6, 4, 1],[4, 16, 24, 16, 4],[6, 24, 36, 24, 6],[4, 16, 24, 16, 4],[1, 4, 6, 4, 1]]
    
    print(rocna_matrika)
    
    return
    
def naloga_2():
    
    vpr = ''' 
    
    2. Priložite slike, 
    zglajene aritmetičnim povprečjem (N×N = 3×3), 
    uteženim povprečjem (N×N = 3×3) ter
    Gaussovim jedrom (N×N = 3×3 in σ = 0, 5).
    Za kaj se v splošnem uporablja glajenje slik?
   
'''
    
    print(vpr)
    # naloga 2
    # glajenje slike z aritmetičnim povprečjem
    
    avgA_F = 1/9 * np.array([[1, 1, 1], [1, 1, 1],[1, 1, 1]])
    
    avgA_I = ih.kernelFiltering(I, avgA_F)
    
    ih.displayImage(avgA_I, 'Glajenje z aritmetičnim povprečjem')
    
    
    # glajenje slike z uteženim povprečjem
    
    avgW_F = 1/16 * np.array([[1, 2, 1], [2, 4, 2],[1, 2, 1]])
    
    avgW_I = ih.kernelFiltering(I, avgW_F)
    
    ih.displayImage(avgW_I, 'Glajenje z uteženim povprečjem')
    
    # glajenje slike z Gaussovo funkcijo, sigma=0.5
    
    #avgG_F = np.array([[0.01, 0.08, 0.01], [0.08, 0.64, 0.08], [0.01, 0.08, 0.01]])
    avgG_F = np.array(ih.gauss_jedro_filtra((3,3), 0.5))
    
    avgG_I = ih.kernelFiltering(I, avgG_F)
    
    ih.displayImage(avgG_I, 'Glajenje z Gaussovo funkcijo')

    odg = ''' 
    
   Namen glajenja je izničevanje nepravilnosti slik.
   Uporablja se na primer za:
       - glajenje ostrih robov na sliki, 
       - izničitev šumov, 
       - ustvarjanje zveznih linij
    
'''
    
    print(odg)
    return
    
def naloga_3():
    
    avgG_F = np.array([[0.01, 0.08, 0.01], [0.08, 0.64, 0.08], [0.01, 0.08, 0.01]])
    
    avgG_I = ih.kernelFiltering(I, avgG_F)

    
    # naloga 3.1
    
    c = 2
    
    lap_F = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    
    lap_R = ih.kernelFiltering(I, lap_F)
    
    lap_I = I - c * lap_R
    
    ih.displayImage(ih.scale2range(lap_R), 'Slika odziva Laplaceovega operatorja')
    
    ih.displayImage(lap_I, 'Ostrenje z Laplaceovim operatorjem')


    # naloga 3.2
    c = 2
    
    msk_R = I - avgG_I
    
    msk_I = I + c*msk_R
    
    ih.displayImage(ih.scale2range(msk_R), 'Slika maske pri ostrenju z maskiranjem neostrih področij')
    
    ih.displayImage(msk_I, 'Ostrenje z maskiranjem neostrih področij')

    
    vpr = ''' 
    
    3. Priložite slike, izostrene z Laplaceovim operatorjem 
    ter z maskiranjem neostrih področij.
    
    Uporabite velikost jedra filtrov N×N = 3×3, 
    standardni odklon σ = 2 in 
    stopnjo ostrenja c = 2.
    
    Priložite tudi sliko odziva na Laplaceov operator ter 
    sliko maske neostrih področij. 
    
    Za kaj se v splošnem uporablja ostrenje slik? 
    
    Kaj je pomanjkljivost ostrenja, 
    ki je opazna tudi na pridobljenih slikah?
   
'''
    
    print(vpr)
    
    odg = ''' 
    
    Z ostrenjem se poudarja prehode različno svetlih področij. 
    Slika postane jasnejša (kontrast je povečan; izostritev).
    
    Slabosti slabljenja so:
    - poudari se šum
    - duši povsod, kjer se vrednosti počasi spreminjajo (ali so konstantne)
    - dodan kontrast tam, kjer ga original nima
        
'''
    
    print(odg)

    return

def naloga_4():
    
    # računanje odziva na Sobelov operator v x smeri
    
    sobX_F = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    
    sobX_I = ih.kernelFiltering(I, sobX_F)
    
    ih.displayImage(ih.scale2range(sobX_I), 'Odziv na Sobelov operator v X smeri')
    
    # računanje odziva na Sobelov operator v y smeri
    
    sobY_F = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    sobY_I = ih.kernelFiltering(I, sobY_F)
    
    ih.displayImage(ih.scale2range(sobY_I), 'Odziv na Sobelov operator v Y smeri')
    
    # računanje amplitudne slike gradienta
    
    sobA_I = np.sqrt(sobX_I**2 + sobY_I**2)
    
    ih.displayImage(ih.scale2range(sobA_I), 'Amplitudna slika gradienta')


    vpr = ''' 
    
    4. Priložite slike Sobelovih gradientov v x in y smeri 
    ter amplitudno sliko Sobelovega gradienta. 
    Uporabite velikost jedra filtra velikosti N×N = 3×3. 
    
    Za kaj se v splošnem uporablja določanje gradientov slik?
   
'''
    
    print(vpr)
    
    odg = ''' 
   
    Uporaba določanja gradientov?
   
    - za merjenje sprememb intenzitete pikslov originalne slike v določeni smeri...    
   (sliki gradientov v osi x ali y zadosti možen razpon)
    
   - za detekcijo robov (piksli z največjimi gradientnimi vrednostmi) 
   
   - za opazovanje spremembe intenzitete v okolici enega piksla
    
'''
    
    print(odg)
    
    return

def naloga_5():
    
    # naloga 6
    # statistično filtriranje z vrednostjo mediane
    
    med_I = ih.statisticalFiltering(I, 3, np.median)
    
    ih.displayImage(med_I, 'Statistično filtriranje - median')
    
    # statistično filtriranje z maksimalno vrednostjo
    
    max_I = ih.statisticalFiltering(I, 3, np.max)
    
    ih.displayImage(max_I, 'Statistično filtriranje - max')
    
    # statistično filtriranje z minimalno vrednostjo
    
    min_I = ih.statisticalFiltering(I, 3, np.min)
    
    ih.displayImage(min_I, 'Statistično filtriranje - min')
    
    vpr = ''' 
    
    5. Priložite slike, filtrirane z medianinim filtrom, 
    filtrom maksimalne vrednosti in 
    filtrom minimalne vrednosti. 
    
    Uporabite velikost jedra filtra N×N = 3×3. 
    
    Za kaj se v splošnem uporablja statistično filtriranje slik?
    
    Kaj povzroči uporaba vsakega od navedenih filtrov na sliki? 
    
    Kakšna je bistvena razlika med filtriranjem z medianinim filtrom 
    in s filtri za glajenje slik?
   
'''
    
    print(vpr)
    
    odg = ''' 
    
   > Za kaj se v splošnem uporablja statistično filtriranje slik?
   
   - odstranjevanje šuma (npr. sol, poper)
   
   > Kaj povzroči uporaba vsakega od navedenih filtrov na sliki? 
   - Medianin filter:
        _dobro odstranjuje šum,
        _ohrani ostre prehode na sliki. 
   
   
   - Maksimalna vrednost:
        _maksimalni filter poudari najsvetlejše točke na sliki 
        _odstrani temni impulzni šum (poper) 
   
   - Minimalna vrednost:
       _poudari najtemnejše točke
       _odstrani svetli impulzni šum (sol) 
   
   > Kakšna je bistvena razlika med filtriranjem z medianinim filtrom in s filtri za glajenje slik?
   
   - Medianin filter izbere vrednosti okoliščnih pikslov, torej
   nova slika nima novih vrednosti pikslov; hkrati ohrani ostre robove.
   
   
   - Filter aritmetične sredine vrne danemu pikslu precej drugačno vrednost,
   proti vrednostim okolišnih pikslov. Tudi bolje gladi sliko kot filter mediane.  
    
'''
    
    print(odg)
    
    return

def vse_naloge():
  naloga_1()
  naloga_2()
  naloga_3()
  naloga_4()
  naloga_5()
  ih.displayImage(I, 'Originalna slika')
  return



if __name__ == '__main__':
    
    # naloži sliko fotografa
    I = ih.loadImage('cameraman-256x256-08bit.raw', (256, 256), np.uint8)

######################################################################################################################################################################

    #dict nalog in dict funkcij naloga_1... 6
    
    naloga = {1: naloga_1, 2: naloga_2, 3: naloga_3, 4: naloga_4, 5: naloga_5}
    naloga_opcije = {1: "naloga 1", 2: "naloga 2", 3: "naloga 3", 4: "naloga 4", 5: "naloga_5"}

######################################################################################################################################################################
#UX: izbira naloge
    print("Iz opcij spodaj...")
    #print vse opcije
    for key, val in naloga_opcije.items():
      print (key, "=>", val)
    print("... si izberi številko od 1 do 5 \n prikazale se bodo rešitve \n in se izpisale sem. \n Stisni ENTER za vse naloge =)")       
    ukaz = input("Naloga? (od 1 do 5):     ")
    try:
      naloga_ukaz = int(ukaz)
      naloga.get(naloga_ukaz)()
    except:
      vse_naloge() 
######################################################################################################################################################################