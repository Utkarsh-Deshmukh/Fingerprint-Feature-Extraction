# FingerprintFeatureExtraction
The important fingerprint minutiae features are the ridge endpoints (a.k.a. Terminations) and Ridge Bifurcations.

![image](https://user-images.githubusercontent.com/13918778/35665327-9ddbd220-06da-11e8-8fa9-1f5444ee2036.png)

The feature set for the image consists of the location of Terminations and Bifurcations and their orientations

# Running the source files
- run the file main.py
- the input image is stored in the folder "enhanced". If the input image is not enhanced, the minutiae features will be very noisy

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

