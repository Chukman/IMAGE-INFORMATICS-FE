# -*- coding: utf-8 -*-

import numpy as np

def imageInterpol(iImage, iPixelSize, iCoorX, iCoorY, iBgr):
    
    '''
    Bilinearna interpolacija v 2D.
    '''
    
    # velikost slike
    yDim, xDim = iImage.shape
    
    # nastavi začetno sliko ozadja
    oImage = np.ones_like(iImage)*iBgr
    
    # pretvori koordinate iz [mm] v [pixel]
    iCoorX = iCoorX/iPixelSize[0]
    iCoorY = iCoorY/iPixelSize[1]

    # interpolacija območja (bilinearna)
    for y in range(yDim):
        for x in range(xDim):
        	
            # izračunaj koordinate točke (preslikane slike na referenčni)
            point = [iCoorX[y,x], iCoorY[y,x]]
            
            # ali je vrednost znotraj referenčne slike
            if point[0] >= 0 and point[0] <= xDim - 1 \
                and point[1] >= 0 and point[1] <= yDim - 1:
                # izračunaj koordinate slikovnega elementa (referenčne slike)
                pixel = [int(point[0]), int(point[1])]
                
                # izračunaj uteži
                a = (pixel[0]+1 - point[0]) * (pixel[1]+1 - point[1])
                b = -(pixel[0] - point[0]) * (pixel[1]+1 - point[1])
                c = -(pixel[0]+1 - point[0]) * (pixel[1] - point[1])
                d = (pixel[0] - point[0]) * (pixel[1] - point[1])
                
                # izračunaj pripadajoče sivinske vrednosti
                sa = iImage[pixel[1], pixel[0]]
                sb = iImage[pixel[1], min(pixel[0]+1, xDim-1)]
                sc = iImage[min(pixel[1]+1, yDim-1), pixel[0]]
                sd = iImage[min(pixel[1]+1, yDim-1), min(pixel[0]+1, xDim-1)]
                
                # priredi sivinsko vrednost
                oImage[y,x] = a*sa + b*sb + c*sc + d*sd
    
    return oImage 
