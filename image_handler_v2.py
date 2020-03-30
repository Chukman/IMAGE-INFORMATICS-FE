# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:01:34 2020
VAJA 03@S.I.
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
        
                  gridY[0] - 0.5*stepY, gridY[-1] + 0.5*stepY)
        
        pp.imshow(iImage, cmap=pp.cm.gray, vmin=0, vmax=255, extent=extent)
        
        #pp.savefig(iTitle)
        #print("Shranil: ", iTitle, "\n")
    
    else:
    
        pp.imshow(iImage, cmap=pp.cm.gray, vmin=0, vmax=255)
        #pp.savefig(iTitle)
        #print("Shranil: ", iTitle, "\n")
    
    pp.show()
    
    #pp.savefig(iTitle)
    
    #print("Shranil: ", iTitle, "\n")
    
    return

def loadImage(iPath, iSize, iType):
    
    fid = open(iPath, 'rb')
    
    oImage = np.ndarray(
            (iSize[1],iSize[0]),
            dtype=iType,
            buffer=fid.read()
            )
    
    fid.close()
    return oImage


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
    #var = 0.1
    #sigma = var**0.5

    #oNoise = np.random.normal(iStd,sigma,(row,col))
    
    oNoise = np.random.normal(0, iStd, (row, col))
    oNoise = oNoise.reshape(row,col)

    oImage = iImage + oNoise

    return oImage, oNoise