import cv2
import numpy as np
def color_hist(img, nbins) :
    Hist = []
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H = cv2.calcHist([img_hsv], [0], None, [nbins[0]], [0, 360])
    S = cv2.calcHist([img_hsv], [1], None, [nbins[1]], [0, 1])
    V = cv2.calcHist([img_hsv], [2], None, [nbins[2]], [0, 1])
    hist_temp = np.concatenate((H, S, V), axis = 0)
    for i in  hist_temp.tolist() :
        Hist.append(i[0])
    return Hist
