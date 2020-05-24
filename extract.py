# -*- coding: utf-8 -*-
"""
Author:     Lynne Raynor

Description: Library for locating QR codes in images and performing a 
             perspective transform
-----------
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import transform 


def cornerHarris_demo(val, image):
    thresh = val
    # Detector parameters
    blockSize = 2
    apertureSize = 3
    k = 0.04
    corners = []
    # Detecting corners
    dst = cv2.cornerHarris(image, blockSize, apertureSize, k)
    # Normalizing
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    cv2.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    dst_norm_scaled = cv2.convertScaleAbs(dst_norm)
    # Drawing a circle around corners
    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i,j]) > thresh:
                cv2.circle(dst_norm_scaled, (j,i), 5, (0), 2)
                corners.append((i, j))

    (x, y) = corners[int(round(len(corners) / 2))]
    return (x, y, dst_norm_scaled)





def get_image(im, id): 
#resize image to fit screen
    r = 1000.0 / im.shape[1]
    dim = (1000, int(im.shape[0] * r))
    resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
    
    #convert image to grayscale
    grayscaled = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
     
    (x, y, dst_norm_scaled) = cornerHarris_demo(125, grayscaled)
    
    
    xmin = int(round(x-(resized.shape[0]*.06)))
    xmax = int(round(x+(resized.shape[0]*.06)))
    ymin = int(round(y-(resized.shape[0]*.06)))
    ymax = int(round(y+(resized.shape[0]*.06)))
    cropped = resized[xmin:xmax, ymin:ymax]
    gray_cropped = cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)
    
    pts = get_corners(gray_cropped, id)
    ordered = transform.order_points(pts)    
    warped = transform.four_point_transform(gray_cropped, ordered)
    return warped 
        
    
    
    
def get_corners(im, id): 
    #find edges near QR code
    edges = cv2.Canny(im,100,200)

    #get position of edges
    indices = np.where(edges != [0])
    by_x = list(zip(indices[1], indices[0]))
    by_y = list(by_x)
    
    by_x.sort(key = lambda x: x[0])
    by_y.sort(key = lambda x: x[1])
    
    points = np.empty(4, dtype=(int,2))
    points[0] = by_x[3]
    points[1] = by_x[len(by_x) - 1]
    points[2] = by_y[3]
    points[3] = by_y[len(by_y) - 1]
    
    
    for i in range(4):
        (a, b) = points[i]
        cv2.circle(edges, (a,b), 5, (150, 0, 0), 2)
    
    cv2.imwrite('./output/edge_image_{}.jpg'.format(id), edges)
    #cv2.imshow('edges for image {}'.format(id), edges)   
    return points
    


    
    


