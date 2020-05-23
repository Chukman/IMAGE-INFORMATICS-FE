# -*- coding: utf-8 -*-
"""
Created on Tue Apr  28 09:45:55 2020
VAJA 08@S.I.
@author: mz8202
"""

import numpy as np
import asdf_movie_handler as ih



def naloga_1():
    
    # naloži in prikaži testno sliko
    
    I = ih.loadImage('test-128x256-08bit.raw', [128, 256], np.uint8)  
   
    
    # strukturni element
    SE = np.array([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]])
    
    # erozija in dilacija slike
    eI = ih.morphErosion(I, SE)
    ih.displayImage(eI, 'Erozija testne slike')
    dI = ih.morphDilation(I, SE)
    ih.displayImage(dI, 'Dilacija testne slike')
    
    # odpiranje (dilacija erozije) in zapiranje (erozija dilacije) slike
    oI = ih.morphOpening(I, SE)
    ih.displayImage(oI, 'Odpiranje testne slike')
    cI = ih.morphClosing(I, SE)
    ih.displayImage(cI, 'Zapiranje testne slike')
    
    return
    
def naloga_2():
           
    # naloži in prikaži realno sliko
    I = ih.loadImage('real-256x256-08bit.raw', [256, 256], np.uint8)
    
    # strukturni element
    SE = np.array([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]])
    
    # erozija in dilacija slike
    eI = ih.morphErosion(I, SE)
    ih.displayImage(eI, 'Erozija realne slike')
    dI = ih.morphDilation(I, SE)
    ih.displayImage(dI, 'Dilacija realne slike')
    
    # odpiranje (dilacija erozije) in zapiranje (erozija dilacije) slike
    oI = ih.morphOpening(I, SE)
    ih.displayImage(oI, 'Odpiranje realne slike')
    cI = ih.morphClosing(I, SE)
    ih.displayImage(cI, 'Zapiranje realne slike')
    
    return
    
def naloga_3():
    
    
    vpr = '''
    
    3. Kakšen je rezultat morfoloških operacij, 
    če uporabimo strukturni element velikosti 3×1,
    ki je podan v navodilih?
    
    Kakšen je rezultat, če ta strukturni element zavrtimo za 90◦ 
    in postane torej velikosti 1×3? Obrazložite odgovor.

'''
    
    print(vpr)
    
    odg = ''' 
                        1
    1  1  1   proti     1    strukturni element?
                        1
   V kolikor bo eden od zajetih pikslov sovpadal s pikslom elementa, 
   bo okolica elementa  privzela vrednost skupnega maksimuma.
   Dodajo se piksli, ki privzamejo nove vrednosti na izhodni sliki.
   
   V PRIMERU DILACIJE:
   V prvem primeru bo 3x1 element horizontalno širil objekte na izhodni sliki.
   V drugem pa bo 1x3 element vertikalno širil objekte na izhodni sliki.
    
   DILACIJA IN EROZIJA STA DUALNI OPERACIJI:
       če prva dodaja, druga odvzema...
   1x3 element vertikalno odvzema, krči objekte na izhodni sliki,
   3x1 pa horizontalno.
   
   Povzeto torej strukturni element vpliva 
   na smer odvzemanja/dodajanja pikslov na izhodni sliki

   
   Zakaj? 
   Strukturni element je matrika, ki poišče piksel v sliki, 
   ki se procesira in deklarira okolico v procesiranju vsakega piksla;
   je oblika maske, ki jo uporabimo v morfoloških operatorjih.
   
   Tipično se izbere strukturni element iste velikosti in oblike
   kot so objekti, ki jih želimo procesirat na vhodni sliki.
    
   Efekt dilacijskega operatorja na sivinski ali binarni sliki je ta, 
   da postopoma povečuje meje regij osprednih pikslov (tipično belih - sol).
   
   To pomeni, da okolica osprednih pikslov zraste po velikosti,
   medtem ko pa istočasno postajajo vmesne vrzeli manjše.
     
   Za vsak vhodni piksel (ozadje),
   superponiramo strukturni element povrh slike tako, 
   da njegove koordinate sovpadajo s pozicijo piksla. 
   (Vsak strukturni element ima izhodišče.)
   
   Če vsaj en piksel v strukturnem elementu sovpada z osprednimi piksli in 
   piksli slike pod elementom, 
   potem je vhodni piksel nastavljen na vrednost ospredja.
   
   Če pa so vsi sovpadni piksli v sliki ozadni, 
   potem vhodni piksel tudi ostane na vrednosti ozadja.
   
   Dilacija torej širi piksle slike; 
   uporabljena je na primer za širjenje elementa A
   z uporabo strukturnega elementa B.
   Dilacija doda piksle na mejah objektov.
   Vrednost izhodnega pa je maksimum vrednosti vsek okolišnih pikslov.   
   
    
'''  
    print(odg)
    
    # naloži in prikaži testno sliko
    I = ih.loadImage('test-128x256-08bit.raw', [128, 256], np.uint8)
   

    SE1 = np.ones((3,1)) # MxN=1x3 (stolpec)
    SE2 = np.ones((1,3)) # MxN=3x1 (vrstica)
    
    # erozija in dilacija slike
    eI = ih.morphErosion(I, SE1)
    ih.displayImage(eI, 'Erozija testne slike 1x3')
    
    dI = ih.morphDilation(I, SE1)
    ih.displayImage(dI, 'Dilacija testne slike 1x3')
    
    # erozija in dilacija slike
    eI = ih.morphErosion(I, SE2)
    ih.displayImage(eI, 'Erozija testne slike 3x1')
    
    dI = ih.morphDilation(I, SE2)
    ih.displayImage(dI, 'Dilacija testne slike 3x1')

    return

def naloga_4():
  

    vpr = ''' 
    
    4. Kakšni so učinki morfološke erozije oziroma dilacije? Obrazložite odgovor.

    
'''
    
    print(vpr)
    
    odg = ''' 
   
    Po šabloni strukturnega elementa je efekt dilacije oziroma dualne operacije erozije
    dodajanje oziroma odvzem pikslov na mejah objektov.
    
    Na primer, če želimo izboljšati binarno ali sivinsko sliko teksta, ki ima veliko soli
    bi lahko uporabili dilacijo, ki zapolni vmesne vrzeli in tako vrne bolj berljiv tekst.
    
    Efekt erozije pa je odvzem pikslov na mejah objektov:
        strukture se pri operatorju morfološke erozije po velikosti zmanjšajo,
        vmesne vrzeli pa povečajo.
        pri operatorju morf. dilacije ravno obratno: strukture se po velikosti povečajo in
        vmesne vrzeli zmanjšajo - sledeč izbrani obliki šablone ali strukturnega elementa.
    
    Ta element je lahko povsem poljubne oblike, a v praksi se izbere preudarno,
    upoštevajoč oblike, konture, ki nastopajo v vhodni sliki.
    Z ustrezno izbiro oblike te šablone namreč vplivamo na to, 
    katere strukture (objekte ali vrzeli) bo večala, v kateri smeri in koliko.
    
    V kolikor je ta element vrstični (npr. 1x3), bodo vplivane predvsem navpične strukture in vodoravne ohranjene;
    ali stolpični (npr. 3x1), kjer pa bodo navpične ohranjene in vodoravne vplivane. 
    
    Morf. erozija in dilacija torej vplivata na 
    velikost struktur/objektov in vrzeli/praznin na izhodni sliki.
    
'''
    
    print(odg)
    
    return

def naloga_5():

    vpr = ''' 
    
    5. Kakšni so učinki morfološkega odpiranja oziroma zapiranja? Obrazložite odgovor.
    
'''
    
    print(vpr)
    
    odg = ''' 
   
   Morf. odpiranje predvsem deluje podobno kot sama erozija, vendar manj koherentno/intenzivno.
   Manj drastično deluije na same oblike objektov. Je mila oblika erozije torej.
   
   Morf. zapiranje pa po dualnosti deluje kot dilacija, vendar spet je efekt manj drastičen.
   
   To sta torej operaciji, ki manj popačita konkretne oblike struktur, mej objektov in praznin med njimi.
    
'''
    
    print(odg)
   
    I = ih.loadImage('test-128x256-08bit.raw', [128, 256], np.uint8)  
   
    ih.displayImage(I, 'Originalna, testna slika')
    
    SE = np.array([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]])
    
   
    
    # odpiranje (dilacija erozije) in zapiranje (erozija dilacije) slike
    oI = ih.morphOpening(I, SE)
    ih.displayImage(oI, 'Odpiranje testne slike')
    
    cI = ih.morphClosing(I, SE)
    ih.displayImage(cI, 'Zapiranje testne slike')
    
    return

def naloga_6():

    vpr = ''' 
    
    6. Prikažite razliko med slikama, pridobljenima z morfološko dilacijo in morfološko erozijo,
    in sicer za testno in za realno sliko. Kaj predstavlja taka slika?
    
'''
    
    print(vpr)
    
    odg = ''' 
   
    Uprabim 5x5 strukturni element / šablono na testni in realni sliki (prstni odtis).
    Pri eroziji opazim manjšanje velikosti objektov, pri dilaciji večanje.
    Pri eroziji opazim večanje praznin, vrzeli; pri dilaciji pa manjšanje.
    
    Izključujoče deluje vsaka od izhodnih slik:
        ena poudarja vrzeli med konturami, minutijami;
        druga pa poudarja minutije same.
        
        ena poudarja vrzeli med objekti in manjša objekte same (erozija),
        druga obratno (dilacija) veča objekte in manjša vrzeli.
        
    Posledično so različno razvidni fini detajli obeh slik.
    
    Na realni:
        - z erozijo so predvsem lepše razvidne minutije, torej je ta metoda primernejša, 
        če želimo npr razbrati lastnika tega odtisa; hkrati je slika tudi bolj temna,
        saj imamo več vrzeli, ki nosijo temne piksle.
        
        - z dilacijo pa zgleda bolj kot ideja odtisa - packa, zmazek; 
        slika je tudi svetlejša, ker je več % beline proti vrzelim 
    
    Na testni:
        - z dilacijo so konture objektov poudarjene, odebeljene
        robovi so bolj zaobljeni, meje pa bolj nejasne
        
        - z erozijo pa konture niso več razvidne, 
        vidi se le še pozicije in grobe oblike objektov
        meje so sicer bolj jasne in gladke,
        a veliko detajlov belih objektov ni več
    
    
    Taka slika lahko predstavlja primerjalno kalibracijo CMOS optičnega skenirnika prstnih odtisov.
    Tovrstni skener mora izločit iz slike izključno minutije, resice na koži prsta.
    Torej je zelo občutljiv na specifične oblike in konture objektov in praznin.
    V bistvu mora biti dovolj občutljiv in ponovljiv ob takšni meritvi, da lahko zazna, 
    kje se minutije razdvojijo; kjer pride do dvojitve, zabeleži koordinate na sliki. 
    Po interpolaciji med koordinatami vrne unikatni vzorec uporabnika, kateremu pripada ta prst.   
    
'''
    
    print(odg)
    
    # naloži in prikaži testno sliko
    
    I = ih.loadImage('test-128x256-08bit.raw', [128, 256], np.uint8)  
   
    ih.displayImage(I, 'Originalna, testna slika')
    
    # strukturni element
    SE = np.array([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]])
    
    # erozija in dilacija slike
    eI = ih.morphErosion(I, SE)
    ih.displayImage(eI, 'Erozija testne slike')
    dI = ih.morphDilation(I, SE)
    ih.displayImage(dI, 'Dilacija testne slike')

    
    I = ih.loadImage('real-256x256-08bit.raw', [256, 256], np.uint8)
    ih.displayImage(I, 'Originalna, testna slika')
    
    # erozija in dilacija slike
    eI = ih.morphErosion(I, SE)
    ih.displayImage(eI, 'Erozija realne slike')
    dI = ih.morphDilation(I, SE)
    ih.displayImage(dI, 'Dilacija realne slike')

    return

def vse_naloge():
  naloga_1()
  naloga_2()
  naloga_3()
  naloga_4()
  naloga_5()
  naloga_6()
  return


if __name__ == '__main__':    
    
######################################################################################################################################################################

    #dict nalog in dict funkcij naloga_1... 6
    
    naloga = {1: naloga_1, 2: naloga_2, 3: naloga_3, 4: naloga_4, 5: naloga_5, 6: naloga_6}
    naloga_opcije = {1: "naloga 1", 2: "naloga 2", 3: "naloga 3", 4: "naloga 4", 5: "naloga_5", 6: "naloga_6"}

######################################################################################################################################################################
#UX: izbira naloge
    print("Iz opcij spodaj...")
    #print vse opcije
    for key, val in naloga_opcije.items():
      print (key, "=>", val)
    print("... si izberi številko od 1 do 6 \n prikazale se bodo rešitve \n in se izpisale sem. \n Stisni ENTER za vse naloge naenkrat!")       
    ukaz = input("Naloga? (od 1 do 6):     ")
    try:
      naloga_ukaz = int(ukaz)
      naloga.get(naloga_ukaz)()
    except:
      vse_naloge() 
######################################################################################################################################################################