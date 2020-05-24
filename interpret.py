# -*- coding: utf-8 -*-
"""
Author:     Lynne Raynor

Description: takes images of quartered QR code, extracts the pieces from each
             image, then stitches them together to read the 4-digit code
-----------
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import extract as ex


im1 = cv2.imread("1.jpg")
im2 = cv2.imread("2.jpg")
im3 = cv2.imread("3.jpg")
im4 = cv2.imread("4.jpg")


cv2.imwrite('./output/extracted_1.png', ex.get_image(im1, 1))
cv2.imwrite('./output/extracted_2.png', ex.get_image(im2, 2))
cv2.imwrite('./output/extracted_3.png', ex.get_image(im3, 3))
cv2.imwrite('./output/extracted_4.png', ex.get_image(im4, 4))



'''
Partially completed orientation
'''

#Since the completed image is not available, the completed QR code image 
#from the write up will be used to demonstrate this component
raw = cv2.imread('complete.png')
complete = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)
#thresh
retval, threshold = cv2.threshold(complete, 205, 255, cv2.THRESH_BINARY)
cv2.imwrite('./output/threshold.png', threshold)

#Find contours
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
complete_contours = cv2.drawContours(threshold, contours, -1, (100, 50, 100), 4)
cv2.imwrite('./output/contour.png', complete_contours)


'''
Stitching the 4 oriented images together needed here
'''

#sample QR code to be read containing data = 1234
sample = cv2.imread('frame.png')
# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)
    
    
qrDecoder = cv2.QRCodeDetector()
 
# Detect and decode the qrcode
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(sample)
if len(data)>0:
    print("Decoded Data : {}".format(data))
    display(sample, bbox)
    rectifiedImage = np.uint8(rectifiedImage);
    cv2.imshow("Rectified QRCode", rectifiedImage);
else:
    print("QR Code not detected")
    #cv2.imshow("Results", inputImage)
 
