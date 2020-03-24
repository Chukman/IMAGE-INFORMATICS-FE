# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:08:32 2020
VAJA 02@S.I.
rabi head-256x256-08bit.raw sliko
@author: mz8202
"""
import numpy as np
import image_handler as ih

def naloga_3():
    
    slika()
    
    # prikaz slik S1, S2 in N
    ih.displayImage(S1, 'Slika signala S1')
    ih.displayImage(S2, 'Slika signala S2')
    ih.displayImage(N, 'Slika šuma N')
   
    # izračun histogramov S1, S2 in N
    histS1, levelsS1 = ih.computeHistogram(S1)
    histS2, levelsS2 = ih.computeHistogram(S2)
    histN, levelsN = ih.computeHistogram(N)
   
    # prikaz histogramov S1, S2 in N
    ih.displayHistogram(histS1, levelsS1, 'Histogram signala S1')
    ih.displayHistogram(histS2, levelsS2, 'Histogram signala S2')
    ih.displayHistogram(histN, levelsN, 'Histogram šuma N')
    
    
    
    return
    
def naloga_4():
    vpr = """
Izračunajte amplitudno (SNRA), 
diferencialno (SNRD) ter 
močnostno (SNRM) razmerje
signal/šum za dana območja 
signalov in šuma. 
Vrednosti podajte tudi 
v decibelih (dB).

Kaj pomenijo te vrednosti, 
če upoštevamo dana 
območja računanja?
    """
    
    
    
    # amplitudno razmerje signal/šum (S1-N in S2-N)
    SNR_A1 = S1_f.mean()/N_f.std(ddof=1)
    SNR_A2 = S2_f.mean()/N_f.std(ddof=1)
    LOG_SNR_A1 = 20*np.log10(SNR_A1)
    LOG_SNR_A2 = 20*np.log10(SNR_A2)
    
    
    print("Amplitudno razmerje signal/šum (S1/N):   \n", SNR_A1, "\n")
    print("Amplitudno razmerje signal/šum (S1/N), v dB:   \n", LOG_SNR_A1, "dB\n")


    print("Amplitudno razmerje signal/šum (S2/N):   \n", SNR_A2, "\n")
    print("Amplitudno razmerje signal/šum (S2/N), v dB:   \n", LOG_SNR_A2, "dB\n")
    print(vpr)
    
    odg = """
SNR je merilo zanesljivosti zaznave
nekega signala iz šuma.

Amplitudni SNR: 
    amplituda proti standardni deviaciji signala
    amp(g(t)) / amp(n(t))
    
Diferencialni SNR: 
    kontrast signala proti standardni deviaciji signala
    amp(g_a(t) - g_b(t)) / amp(n(t))

Močnostni SNR:
    razmerje kvadratov varianc signala in šuma
    moč(g(t)) / moč(n(t))
    
"""
    print(odg)
    return

def naloga_5():

    # diferencialno razmerje signal/šum (način 1 in način 2)
    SNR_D1 = (S1_f.mean()-S2_f.mean())/N_f.std(ddof=1)
    SNR_D2 = np.abs(S1_f.mean()-S2_f.mean())/np.sqrt(S1_f.std(ddof=1)**2+S2_f.std(ddof=1)**2)
    
    LOG_SNR_D1 = 20*np.log10(SNR_D1)
    LOG_SNR_D2 = 20*np.log10(SNR_D2)
    
    
    print("Diferencialno razmerje signal/šum (način 1):   \n", SNR_D1, "\n")
    print("Diferencialno razmerje signal/šum (način 1), v dB:   \n", LOG_SNR_D1, "dB\n")

    
    print("Diferencialno razmerje signal/šum (način 2):   \n", SNR_D2, "\n")
    print("Diferencialno razmerje signal/šum (način 2), v dB:   \n", LOG_SNR_D2, "dB\n")
    
    vpr = """
Kako veliko območje je smiselno določiti za področje šuma N?    
    """
    print(vpr)
    
    odg = """
MR slike imajo defakto piksle vrednosti 0.
Vse izven znanega objekta je torej šum, če ni črno. 

Območje šuma naj bo torej toliko veliko, da 
v celoti leži le v območju MR slike, 
ki naj bi bilo sicer defakto 0 (črni del).

S tem pristopom je zajet intrinzični šum.
In natančneje določena standardna deviacija šuma    
    """
    print(odg)
    print("Območje S1:  ", areaS1)
    print("Območje N:   ", areaN)
    return


def naloga_6():
    
    # močnostno razmerje signal-šum
    SNR_M = np.abs(S1.mean()-S2.mean())**2/(S1.std(ddof=1)**2+S2.std(ddof=1)**2)
    LOG_SNR_M = 10*np.log(SNR_M)
    print("Močnostno razmerje signal/šum:   \n", SNR_M, "\n")
    
    print("Močnostno razmerje signal/šum, v dB:   \n", LOG_SNR_M, "dB\n")
    
    return


def vse_naloge():
  histogram_slika()
  naloga_3()
  naloga_4()
  naloga_5()
  naloga_6()
  GAUSS()
  return


def histogram_slika():
    
    #add noise funkcija
    histS1, levelsS1 = ih.computeHistogram(S1)
    histogram_slike, nivo_slike = ih.computeHistogram(I)
    ih.displayHistogram(histogram_slike, nivo_slike, "Histogram Slike head-256x256-08bit")
    print("Prikazal histogram slike \n ")
    
    return

def slika():
    
    ih.displayImage(I, 'head-256x256-08bit')
    
    return

def GAUSS():
    inputStd = input("Vpiši standardni odklon dodanega šuma:    ")
    iStd = int(inputStd)
    
    print("Dodajam Gaussov Šum sliki. . .", iStd)
    
    image, gauss = ih.addNoise(I, iStd)
    ih.displayImage(image, 'Slika z Gaussovim šumom')
    hist_G, nivo_G = ih.computeHistogram(gauss)
    ih.displayHistogram(hist_G, nivo_G, "Histogram Slike z Gaussovim šumom")
    
    return

if __name__ == '__main__':
    
    I = ih.loadImage('head-256x256-08bit.raw', (256, 256), np.uint8)
   
    # območja zanimanja
    areaS1 = ((150, 182), (157, 192), 'S1')
    areaS2 = ((160, 162), (167, 172), 'S2')
    
    #območje šuma N
    areaN = ((211, 1), (253, 44), 'N')
    
    S1 = I[areaS1[0][1]:areaS1[1][1] + 1, areaS1[0][0]:areaS1[1][0] + 1]
    S2 = I[areaS2[0][1]:areaS2[1][1] + 1, areaS2[0][0]:areaS2[1][0] + 1]
    
    N = I[areaN[0][1]:areaN[1][1] + 1, areaN[0][0]:areaN[1][0] + 1]
    
    # pretvori območja v decimalni format
    S1_f = np.array(S1, dtype=np.float)
    S2_f = np.array(S2, dtype=np.float)
    N_f = np.array(N, dtype=np.float)

    #dict nalog in dict funkcij naloga_1... 6
    naloga = {1: slika, 2: vse_naloge, 3: naloga_3, 4: naloga_4, 5: naloga_5, 6: naloga_6, 7: histogram_slika}
    naloga_opcije = {1: "Osnovna slika", 2: "Vse naloge", 3: "naloga 3", 4: "naloga 4", 5: "naloga 5", 6: "naloga 6", 7: "histogram slike"}

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
      GAUSS() 
######################################################################################################################################################################