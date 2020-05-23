# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:01:34 2020
VAJA 04@S.I.
@author: mz8202
"""
import numpy as np
import matplotlib.pyplot as pp





def displayImage(iImage, iTitle, gridX=None, gridY=None):
    pp.figure()
    pp.title(iTitle)
    if gridX is not None and gridY is not None:
        stepX = gridX[1] - gridX[0]
        stepY = gridY[1] - gridY[0]
        extent = (gridX[0] - 0.5*stepX, gridX[-1] + 0.5*stepX,
                  gridY[-1] + 0.5*stepY, gridY[0] - 0.5*stepY)
        pp.imshow(iImage, cmap=pp.cm.gray, vmin=0, vmax=255, extent=extent)

    else:
        pp.imshow(iImage, cmap=pp.cm.gray, vmin=0, vmax=255)
        pp.show()



def loadImage3D(iPath, iSize, iType):

    fid = open(iPath, 'rb')

    oImage = np.ndarray((iSize[1],iSize[0],iSize[2]), dtype=iType, buffer=fid.read())

    fid.close()

    return oImage


def loadImage(iPath, iSize, iType):
    
    fid = open(iPath, 'rb')
    
    oImage = np.ndarray(
            (iSize[1],iSize[0]),
            dtype=iType,
            buffer=fid.read()
            )
    
    fid.close()
    return oImage


#Erozija slike s strukturnim elementom.

def morphErosion(iImage, iStruct):

    # inicializacija izhodne slike in dimenzije
    oImage = np.zeros_like(iImage)
    # dimenzije strukturnega elementa
    m = int((iStruct.shape[1]-1)/2)
    n = int((iStruct.shape[0]-1)/2)
    # priredi strukturni element glede na definicijo
    iStruct = np.rot90(iStruct, 2)
    # razširitev slikovne domene (max=255)
    iImage_padded = np.pad(iImage, ((n,n), (m,m)),

    mode='constant', constant_values=255)

    # erozija dane slike (min)
    for y in range(iImage.shape[0]):
        for x in range(iImage.shape[1]):
            iArea = iImage_padded[y:y+2*n+1, x:x+2*m+1] * iStruct
            oImage[y, x] = np.min(iArea[iStruct != 0])
    return oImage


#Dilacija slike s strukturnim elementom

def morphDilation(iImage, iStruct):
    # inicializacija izhodne slike in dimenzije
    oImage = np.zeros_like(iImage)
    # dimenzije strukturnega elementa
    m = int((iStruct.shape[1]-1)/2)
    n = int((iStruct.shape[0]-1)/2)
    # priredi strukturni element glede na definicijo
    iStruct = np.rot90(iStruct, 2)
    # razširitev slikovne domene (min=0)
    iImage_padded = np.pad(iImage, ((n, n), (m, m)), mode='constant', constant_values=0)

    # dilacija dane slike (max)
    for y in range(iImage.shape[0]):
        for x in range(iImage.shape[1]):
            iArea = iImage_padded[y:y+2*n+1, x:x+2*m+1] * iStruct
            oImage[y, x] = np.max(iArea[iStruct != 0])
    return oImage



#Odpiranje slike s strukturnim elementom.

def morphOpening(iImage, iStruct):
    # odpiranje = dilacija erozije
    oImage = morphDilation(morphErosion(iImage, iStruct), iStruct)
    return oImage


#Zapiranje slike s strukturnim elementom.

def morphClosing(iImage, iStruct):
    # zapiranje = erozija dilacije
    oImage = morphErosion(morphDilation(iImage, iStruct), iStruct)
    return oImage




# Statistično filtriranje.

def statisticalFiltering(iImage, iLength, iFunc):

    # inicializacija filtrirane slike in dolžine jedra filtra

    oImage = np.zeros_like(iImage)

    n = int((iLength-1)/2)

    # razširi slikovno domeno

    iImage_padded = np.pad(iImage, n, mode='edge')

    # filtriranje slike

    for y in range(iImage.shape[0]):

        for x in range(iImage.shape[1]):

            iArea = iImage_padded[y:y+2*n+1, x:x+2*n+1]
    
            oImage[y, x] = iFunc(iArea)
    
    return oImage





# Razteg dinamičnega območja slike na 8 bitov

def scale2range(iImage):

    oImage = 255/(iImage.max()-iImage.min()) * (iImage - iImage.min())

    return oImage



# vrni jedro Gauss filtra pri poljubni sigmi

def gauss_jedro_filtra(dimenzija, sigma):
    
    m,n = [(ss - 1.) / 2. for ss in dimenzija]
    
    y,x = np.ogrid[-m:m+1, -n:n+1]
    
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
   
    sumh = h.sum()
    
    if sumh != 0:
        
        h /= sumh
  
    return h



# Prostorsko filtriranje slike z jedrom.

def kernelFiltering(iImage, iKernel):

    # inicializacija filtrirane slike in dolžine jedra filtra
    
    oImage = np.zeros_like(iImage, dtype=np.float)
    
    n = int((iKernel.shape[0]-1)/2)
    
    # razširi slikovno domeno
    
    iImage_padded = np.pad(iImage, n, mode='edge')
    
    # priredi jedro za konvolucijo
    
    iKernel = np.rot90(iKernel, 2)
    
    # filtriranje slike
    
    for y in range(iImage.shape[0]):
    
        for x in range(iImage.shape[1]):
        
            iArea = iImage_padded[y:y+2*n+1, x:x+2*n+1]
            
            oImage[y, x] = np.sum(iKernel * iArea)
    
    return oImage


#Določanje osnovnega ravninskega prereza.

def getCrossSection(iImage, iPlane, iNum):

    # stranska ravnina (stolpci v X smeri)

    if iPlane == 'stranska':

        oSection = iImage[:,iNum,:].T

        # čelna ravnina (vrstice v Y smeri)

    elif iPlane == 'celna':

        oSection = iImage[iNum,:,:].T

        # prečna ravnina (plasti v Z smeri)

    elif iPlane == 'precna':

        oSection = iImage[:,:,iNum]
    

    return np.array(oSection) # nujno kopija, saj ne vemo, kaj bomo s tem delali




#Določanje pravokotne projekcije

def getOrthogonalProjection(iImage, iPlane, iFunc):

    # stranska projekcija

    if iPlane == 'stranska':

        oProjection = iFunc(iImage, axis=1).T

        # čelna projekcija

    elif iPlane == 'celna':
    
        oProjection = iFunc(iImage, axis=0).T
        
        # prečna projekcija
    
    elif iPlane == 'precna':
    
        oProjection = iFunc(iImage, axis=2)
    
    return np.array(oProjection)



#Interpolacija reda 0.

def interpolate0Image(iImage, iSize, oSize):
    # inicializacija končne (prevzorčene) slike
    oImage = np.zeros((oSize[1], oSize[0]))
    # korak interpolacije (dx, dy)
    oStep = [(iSize[0]-1)/(oSize[0]-1), (iSize[1]-1)/(oSize[1]-1)]
    # interpolacija slike (najbližji sosedi - sprehodimo se po končni sliki)
    for y in range(oSize[1]):
        for x in range(oSize[0]):
            # izračunaj koordinate točke (končne slike na začetni)
            point = [x*oStep[0], y*oStep[1]]
            # izračunaj koordinate slikovnega elementa (začetne slike)
            pixel = [round(point[0]), round(point[1])]
            # priredi sivinsko vrednost
            oImage[y,x] = iImage[pixel[1],pixel[0]]
    
    return oImage, oStep

def gammaImage(iImage, iGamma):
    
    '''
    Gama preslikava slike
    '''
    
    # gama preslikava glede na dano vrednost
    
    oImage = 255**(1-iGamma) * iImage**iGamma
    
    return oImage


def thresholdImage(iImage, iThreshold):
    
    '''
    Upragovljanje slike.
    '''
    
    #inicializiraj izhodno sliko
    
    oImage = np.array(iImage)
    
    #vrednosti pod mejo praga so 0
    
    oImage[iImage <= iThreshold] = 0
    
    #vrednosti nad mejo praga so 255
    
    oImage[iImage > iThreshold] = 255
    
    return oImage


def windowImage(iImage, iCenter, iWidth):
    '''
    Linearno oknenje slike.
    '''
    # inicializiraj izhodno sliko
    oImage = np.array(iImage, dtype=np.float)
    # dinamično območje monitorja
    L_0 = 2**8
    # vrednosti pod spodnjo mejo okna so 0
    oImage[iImage < iCenter-iWidth/2] = 0
    # vrednosti nad zgornjo mejo okna so 255
    oImage[iImage > iCenter+iWidth/2] = L_0-1
    # vrednosti znotraj mej okna so linearno preslikane
    idx = np.logical_and(iImage >= iCenter-iWidth/2, iImage <= iCenter+iWidth/2)
    oImage[idx] = (iImage[idx] - (iCenter - iWidth/2)) * (L_0-1)/iWidth
    return oImage



def scaleImage(iImage, iSlope, iIntersection):
    
    '''
    Linearna preslikava slike.
    '''
    
    #linearna preslikava glede na premico
    
    oImage = iImage*iSlope + iIntersection
    
    
    return oImage


#Interpolacija reda 1.


def interpolate1Image(iImage, iSize, oSize):
    
    # inicializacija končne (prevzorčene) slike
    oImage = np.zeros((oSize[1],oSize[0]))
    
    # korak interpolacije (dx, dy)
    oStep = [(iSize[0]-1)/(oSize[0]-1), (iSize[1]-1)/(oSize[1]-1)]
    
    # interpolacija območja (bilinearna)
    for y in range(oSize[1]):
        for x in range(oSize[0]):
            
            # izračunaj koordinate točke (končne slike na začetni)
            point = [x*oStep[0], y*oStep[1]]
            
            # izračunaj koordinate slikovnega elementa (začetne slike)
            pixel = [int(point[0]), int(point[1])]
            
            # izračunaj uteži
            
            a = (pixel[0]+1 - point[0]) * (pixel[1]+1 - point[1])
            b = -(pixel[0] - point[0]) * (pixel[1]+1 - point[1])
            c = -(pixel[0]+1 - point[0]) * (pixel[1] - point[1])
            d = (pixel[0] - point[0]) * (pixel[1] - point[1])
            
            # izračunaj pripadajoče sivinske vrednosti
            
            sa = iImage[pixel[1], pixel[0]]
            sb = iImage[pixel[1], min(pixel[0]+1, iSize[0]-1)]
            sc = iImage[min(pixel[1]+1, iSize[1]-1), pixel[0]]
            sd = iImage[min(pixel[1]+1, iSize[1]-1), min(pixel[0]+1, iSize[0]-1)]
            
            # priredi sivinsko vrednost
            
            oImage[y,x] = a*sa + b*sb + c*sc + d*sd
            
    return oImage, oStep


#Izračun histograma.
def computeHistogram(iImage):
    # poišči najmanjšo in največjo sivinsko vrednost
    minL = int(np.floor(np.min(iImage)))
    maxL = int(np.ceil(np.max(iImage)))
    # sivinske vrednosti in robovi razredov
    oLevels = np.arange(minL, maxL + 1)
    edges = np.arange(minL, maxL + 2) - 0.5
    # izračun histograma
    oHist = np.histogram(iImage, bins=edges)[0]
    # vrni vektor histograma
    return oHist, oLevels

'''
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
'''

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
    #var = 0.1
    #sigma = var**0.5

    #oNoise = np.random.normal(iStd,sigma,(row,col))
    
    oNoise = np.random.normal(0, iStd, (row, col))
    oNoise = oNoise.reshape(row,col)

    oImage = iImage + oNoise

    return oImage, oNoise