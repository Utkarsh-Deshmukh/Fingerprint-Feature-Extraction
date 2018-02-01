# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:13:36 2018

@author: Utkarsh
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import skimage.morphology
import skimage

from getTerminationBifurcation import getTerminationBifurcation;
from removeSpuriousMinutiae import removeSpuriousMinutiae

if __name__ == "__main__":
    img = cv2.imread('../enhanced/1.jpg',0);
    img = np.uint8(img>128);
    
    skel = skimage.morphology.skeletonize(img)
    skel = np.uint8(skel)*255;
    
    mask = img*255;
    (minutiaeTerm, minutiaeBif) = getTerminationBifurcation(skel, mask);
    
    minutiaeTerm = skimage.measure.label(minutiaeTerm, 8);
    RP = skimage.measure.regionprops(minutiaeTerm)
    minutiaeTerm = removeSpuriousMinutiae(RP, np.uint8(img), 10);
    
    BifLabel = skimage.measure.label(minutiaeBif, 8);
    TermLabel = skimage.measure.label(minutiaeTerm, 8);
    
    minutiaeBif = minutiaeBif * 0;
    minutiaeTerm = minutiaeTerm * 0;
    
    (rows, cols) = skel.shape
    DispImg = np.zeros((rows,cols,3), np.uint8)
    DispImg[:,:,0] = skel; DispImg[:,:,1] = skel; DispImg[:,:,2] = skel;
    
    
    RP = skimage.measure.regionprops(BifLabel)
    for i in RP:
        (row, col) = np.int16(np.round(i['Centroid']))
        minutiaeBif[row, col] = 1;
        (rr, cc) = skimage.draw.circle_perimeter(row, col, 3);
        skimage.draw.set_color(DispImg, (rr,cc), (255,0,0));
    
    
    RP = skimage.measure.regionprops(TermLabel)
    for i in RP:
        (row, col) = np.int16(np.round(i['Centroid']))
        minutiaeTerm[row, col] = 1;
        (rr, cc) = skimage.draw.circle_perimeter(row, col, 3);
        skimage.draw.set_color(DispImg, (rr,cc), (0, 0, 255));
    
    cv2.imshow('a',DispImg);
    cv2.waitKey(0)