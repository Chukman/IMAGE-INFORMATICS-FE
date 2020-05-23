# -*- coding: utf-8 -*-

import numpy as np
from skimage import __version__ as sk_ver
from skimage import feature

def loadImage(iPath, iSize, iType):
    
    '''
    Naloži sliko.
    '''
    
    fid = open(iPath, 'rb')
    
    oImage = np.ndarray(
            (iSize[1],iSize[0]), 
            dtype=iType, 
            buffer=fid.read()
    )
    
    fid.close()
    
    return oImage

def findEdgesCanny(iImage, low_iThreshold, high_iThreshold, iStdDev):
    
    # preveri verzijo scikit-image
#    if int(sk_ver[2:4]) < 17:
#        low_iThreshold = np.iinfo(iImage.dtype).max * low_iThreshold
#        high_iThreshold = np.iinfo(iImage.dtype).max * high_iThreshold
#    
    # izvede iskanje robov
    oImage = feature.canny(iImage, sigma=iStdDev, low_threshold=low_iThreshold, 
                           high_threshold=high_iThreshold, use_quantiles=True)
    
    return oImage


#Houghova preslikava v 2D za 2 parametra.


def houghTransform2D2P(iImage, stepR, stepF):

    # določimo velikost vhodne slike robov v št. pikslov
    Y, X = iImage.shape
    
    # določimo diskretno mrežo "r" glede na korak
    D = np.sqrt((X-1)**2+(Y-1)**2)
    d = stepR * np.ceil(D/stepR) # malce večji razpon deljiv s "stepR"
    rangeR = np.arange(-d, d + stepR, stepR) # zadnje točke funkcija np.arange ne šteje
    
    # določimo diskretno mrežo "fi" glede na korak
    rangeF = np.arange(-90, 90, stepF)
    rangeFrad = np.deg2rad(rangeF)
    idxF = np.arange(rangeF.size)
    
    # incializacija akumulatorja
    oAcc = np.zeros((rangeR.size, rangeF.size))
    
    # sprehodimo se po binarni sliki robov iImage
    
    for y in range(Y):
        for x in range(X):
            # točka, ki pripada robu (iImage vsebuje logične binarne vredosti)
            if iImage[y,x]:
                r = x * np.cos(rangeFrad) + y * np.sin(rangeFrad)
                idxR = np.round((r - rangeR[0])/stepR).astype(np.int)
                oAcc[idxR, idxF] += 1
    return oAcc, rangeR, rangeF


def findLocalMaxima(iAcc, rangeR, rangeF, iIntersect, maxIntersectFlag):

    # logično podatkovno polje, kamor zapisujemo lokacije maksimumov
    accFlag = np.zeros_like(iAcc)
    
    # iskanje globalnega maksimuma akumulatorja
    if maxIntersectFlag:
        rIdx, fIdx = np.unravel_index(iAcc.argmax(), iAcc.shape)
        accFlag[rIdx, fIdx] = 1      
        
    # iskanje lokalnih maksimumov akumulatorja
    else:
        # okolica iskanja
        n = 1
        
        # povečaj akumulator za izbrano okolico iskanja "n"
        oAcc = np.pad(iAcc, n, mode='symmetric')
        
        for rIdx in range(rangeR.size):
            for fIdx in range(rangeF.size):
                
                area = oAcc[rIdx:rIdx+2*n, fIdx:fIdx+2*n]
                
                # če je središčni maksimalen, je kandidat za lokalni maksimum
                if area[n, n]== area.max():
                    accFlag[rIdx, fIdx] = 1
                    
    # poišči točke v akumulatorju z najmanj iIntersect premicami
    rIdx, fIdx = np.where(accFlag==1)
    i = np.where(iAcc[(rIdx, fIdx)]>=iIntersect)[0]
    
    maxR = rangeR[rIdx[i]]
    maxF = rangeF[fIdx[i]]
    maxRIdx = rIdx[i]
    maxFIdx = fIdx[i]
    
    return maxR, maxF, maxRIdx, maxFIdx