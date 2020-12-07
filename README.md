# FingerprintFeatureExtraction
The important fingerprint minutiae features are the ridge endpoints (a.k.a. Terminations) and Ridge Bifurcations.

![image](https://user-images.githubusercontent.com/13918778/35665327-9ddbd220-06da-11e8-8fa9-1f5444ee2036.png)

The feature set for the image consists of the location of Terminations and Bifurcations and their orientations

## Installation and Running the tests

 ## method 1
 ```
  pip install fingerprint-feature-extractor
 ```
 
 **Usage:**
  ```
  import fingerprint_feature_extractor
  img = cv2.imread('image_path', 0)				# read the input image --> You can enhance the fingerprint image using the "fingerprint_enhancer" library
  FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(img, spuriousMinutiaeThresh=10, invertImage=False, showResult=True, saveResult=True)
```
 ## method 2
- from the src folder, run the file "main.py"
- **the input image is stored in the folder "enhanced".**
***If the input image is not enhanced, the minutiae features will be very noisy***

# Libraries needed:
- opencv
- skimage
- numpy
- math

# Note
use the code https://github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python to enhance the fingerprint image.
This program takes in the enhanced fingerprint image and extracts the minutiae features.

Here are some of the outputs:


![1](https://user-images.githubusercontent.com/13918778/35665568-ae1fdb6c-06db-11e8-937b-33d7445c931d.jpg)   ![enhanced_feat1](https://user-images.githubusercontent.com/13918778/35665578-baddaf82-06db-11e8-8638-d24de65acd31.jpg)


# How to match the extracted minutiae?
Various papers are published to perform minutiae matching.
Here are some good ones:
- "A MINUTIAE-BASED MATCHING ALGORITHMS IN FINGERPRINT RECOGNITION SYSTEMS" by Łukasz WIĘCŁAW
http://www.keia.ath.bielsko.pl/sites/default/files/publikacje/11-BIO-41-lukaszWieclawMIT_v2_popr2.pdf

"A Minutiae-based Fingerprint Matching Algorithm Using Phase Correlation" by Weiping Chen and Yongsheng Gao
https://core.ac.uk/download/pdf/143875633.pdf

"FINGERPRINT RECOGNITION USING MINUTIA SCORE MATCHING" by RAVI. J, K. B. RAJA, VENUGOPAL. K. R
https://arxiv.org/ftp/arxiv/papers/1001/1001.4186.pdf

