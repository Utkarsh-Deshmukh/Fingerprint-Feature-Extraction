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

from src.getTerminationBifurcation import getTerminationBifurcation;
from src.removeSpuriousMinutiae import removeSpuriousMinutiae
from src.CommonFunctions import ShowResults
from src.extractMinutiaeFeatures import extractMinutiaeFeatures


if __name__ == "__main__":
    img = cv2.imread('../enhanced/3.jpg',0);
    img = np.uint8(img>128);
    
    skel = skimage.morphology.skeletonize(img)
    skel = np.uint8(skel)*255;
    
    mask = img*255;
    (minutiaeTerm, minutiaeBif) = getTerminationBifurcation(skel, mask);
    
    minutiaeTerm = skimage.measure.label(minutiaeTerm, connectivity=2);
    RP = skimage.measure.regionprops(minutiaeTerm)
    minutiaeTerm = removeSpuriousMinutiae(RP, np.uint8(img), 10);

    minutiaeTerm = skimage.measure.label(minutiaeTerm, connectivity=2);
    RP2 = skimage.measure.regionprops(np.uint8(minutiaeTerm))

    '''
    minutiaeBif = skimage.measure.label(minutiaeTerm, connectivity=2);
    RP = skimage.measure.regionprops(minutiaeTerm)
    minutiaeBif = removeSpuriousMinutiae(RP, np.uint8(img), 10);
    '''

    BifLabel = skimage.measure.label(minutiaeBif, connectivity=2);
    TermLabel = skimage.measure.label(minutiaeTerm, connectivity=2);

    FeaturesTerm, FeaturesBif = extractMinutiaeFeatures(skel, minutiaeTerm, minutiaeBif)

    ShowResults(skel, TermLabel, BifLabel)