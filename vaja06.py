# -*- coding: utf-8 -*-
"""
Created on Sun Apr  19 15:20:13 2020
VAJA 06@S.I.
@author: mz8202
"""


import numpy as np
import asdf_handler as ih


if __name__ == '__main__':
    
    iSize = [256, 512]
    iPixelSize = [2, 1]
    
    gridX = np.arange(0, iSize[0]) * iPixelSize[0]
    gridY = np.arange(0, iSize[1]) * iPixelSize[1]
    
    test = ih.loadImage('lena-256x512-08bit.raw', iSize, np.uint8)
    ih.displayImage(test, 'Originalna slika',gridX,gridY )
    
    c00 = [0,0]
    cSredisce = [128,256]
    
    strigA = [0.1, 0.5];rotA = 0;transA = [0, 0];scalA = [1, 1]
    TA = ih.getAffineMatrix2D(strigA, rotA, transA, scalA)
    cxA1, cyA1 = ih.affineTransform2D(gridX, gridY, c00, np.linalg.inv(TA))
    cxA2, cyA2 = ih.affineTransform2D(gridX, gridY, cSredisce, np.linalg.inv(TA))
    Ia1 = ih.imageInterpol(test, iPixelSize, c00, cxA1, cyA1, 255)
    Ia2 = ih.imageInterpol(test, iPixelSize, cSredisce, cxA2, cyA2, 255)

    ih.displayImage(Ia1, 'Strig [0,0]', gridX, gridY)
    ih.displayImage(Ia2, 'Strig (sredisce)', gridX, gridY)
    
    strigB = [0, 0];rotB = -30;transB = [0, 0];scalB = [1, 1]
    TB = ih.getAffineMatrix2D(strigB, rotB, transB, scalB)
    cxB1, cyB1 = ih.affineTransform2D(gridX, gridY, c00, np.linalg.inv(TB))
    cxB2, cyB2 = ih.affineTransform2D(gridX, gridY, cSredisce, np.linalg.inv(TB))
    Ib1 = ih.imageInterpol(test, iPixelSize, c00, cxB1, cyB1, 255)
    Ib2 = ih.imageInterpol(test, iPixelSize, cSredisce, cxB2, cyB2, 255)

    ih.displayImage(Ib1, 'Rotacija [0,0]', gridX, gridY)
    ih.displayImage(Ib2, 'Rotacija (sredisce)', gridX, gridY)
    
    strigC = [0, 0];rotC = 0;transC = [20, -30];scalC = [1, 1]
    TC = ih.getAffineMatrix2D(strigC, rotC, transC, scalC)
    cxC1, cyC1 = ih.affineTransform2D(gridX, gridY, c00, np.linalg.inv(TC))
    cxC2, cyC2 = ih.affineTransform2D(gridX, gridY, cSredisce, np.linalg.inv(TC))
    Ic1 = ih.imageInterpol(test, iPixelSize, c00, cxC1, cyC1, 255)
    Ic2 = ih.imageInterpol(test, iPixelSize, cSredisce,cxC2, cyC2, 255)

    ih.displayImage(Ic1, 'Translacija [0,0]', gridX, gridY)
    ih.displayImage(Ic2, 'Translacija (sredisce)', gridX, gridY)
    
    strigD = [0, 0];rotD = 0;transD = [0, 0];scalD = [0.7, 1.4]
    TD = ih.getAffineMatrix2D(strigD, rotD, transD, scalD)
    cxD1, cyD1 = ih.affineTransform2D(gridX, gridY, c00, np.linalg.inv(TD))
    cxD2, cyD2 = ih.affineTransform2D(gridX, gridY, cSredisce, np.linalg.inv(TD))
    Id1 = ih.imageInterpol(test, iPixelSize, c00, cxD1, cyD1, 255)
    Id2 = ih.imageInterpol(test, iPixelSize, cSredisce,cxD2, cyD2, 255)
    
    ih.displayImage(Id1, 'Skaliranje [0,0]', gridX, gridY)
    ih.displayImage(Id2, 'Skaliranje (sredisce)', gridX, gridY)
    
    strigE = [0, 0];rotE = -30; transE = [20, -30];scalE = [1, 1]
    TE = ih.getAffineMatrix2D(strigE, rotE, transE, scalE)
    cxE1, cyE1 = ih.affineTransform2D(gridX, gridY, c00, np.linalg.inv(TE))
    cxE2, cyE2 = ih.affineTransform2D(gridX, gridY, cSredisce, np.linalg.inv(TE))
    Ie1 = ih.imageInterpol(test, iPixelSize, c00, cxE1, cyE1, 255)
    Ie2 = ih.imageInterpol(test, iPixelSize, cSredisce,cxE2, cyE2, 255)
    
    ih.displayImage(Ie1, 'Toga preslikava [0,0]', gridX, gridY)
    ih.displayImage(Ie2, 'Toga preslikava (sredisce)', gridX, gridY)
    
    strigF = [0, 0];rotF = -30; transF = [20, -30];scalF = [0.7, 1.4]
    TF = ih.getAffineMatrix2D(strigF, rotF, transF, scalF)
    cxF1, cyF1 = ih.affineTransform2D(gridX, gridY, c00, np.linalg.inv(TF))
    cxF2, cyF2 = ih.affineTransform2D(gridX, gridY, cSredisce, np.linalg.inv(TF))
    If1 = ih.imageInterpol(test, iPixelSize, c00, cxF1, cyF1, 255)
    If2 = ih.imageInterpol(test, iPixelSize, cSredisce,cxF2, cyF2, 255)
    
    ih.displayImage(If1, 'Afina preslikava [0,0]', gridX, gridY)
    ih.displayImage(If2, 'Afina preslikava (sredisce)', gridX, gridY)