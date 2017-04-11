import cv2
import numpy as np
from color_hist import color_hist
def GCH (image1, image2, nbins):
    #image1_path ==> path for image1
    img1 = cv2.imread(image1, 1)
    hist_1 = color_hist(img1, nbins)
    #image2_path ==> path for image2
    img2 = cv2.imread(image2, 1)
    hist_2 = color_hist(img2, nbins)
    dist = 0
    for i in xrange(len(hist_1)):
        dist += abs((hist_1[i]**2)-(hist_2[i]**2))**(0.5)
    print dist
