# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:44:22 2018

@author: Utkarsh
"""

import cv2
import numpy as np
import skimage.morphology
import skimage


def removeSpuriousMinutiae(minutiaeList, img, thresh):
    img = img * 0;
    SpuriousMin = [];
    numPoints = len(minutiaeList);
    D = np.zeros((numPoints, numPoints))
    for i in range(1,numPoints):
        for j in range(0, i):
            (X1,Y1) = minutiaeList[i]['centroid']
            (X2,Y2) = minutiaeList[j]['centroid']
            
            dist = np.sqrt((X2-X1)**2 + (Y2-Y1)**2);
            D[i][j] = dist
            if(dist < thresh):
                SpuriousMin.append(i)
                SpuriousMin.append(j)
                
    SpuriousMin = np.unique(SpuriousMin)
    for i in range(0,numPoints):
        if(not i in SpuriousMin):
            (X,Y) = np.int16(minutiaeList[i]['centroid']);
            img[X,Y] = 1;
    
    img = np.uint8(img);
    return(img)