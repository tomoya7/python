#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:38:37 2019

@author: tomoya
"""
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
img=Image.open('./tomoya_server.jpg')
print(type(img))
print(img.mode)
img=np.array(img)
print(img[0,0,:])
img=cv2.imread('./tomoya_server.jpg')
print(type(img))
print(img[0,0,:])
img=plt.imread('./tomoya_server.jpg')
print(type(img))
print(img[0,0,:])
