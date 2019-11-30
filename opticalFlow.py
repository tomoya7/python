# -*- coding: utf-8 -*-
import numpy as np
import cv2
 
 
cap = cv2.VideoCapture("../fight007/video/1.mp4")
 
#获取第一帧
ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
#遍历每一行的第1列
hsv[...,1] = 255
ret,frame2=cap.read()
next=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
flow=cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
print flow.shape
 
# while(1):
#     ret, frame2 = cap.read()
#     next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
 
#     #返回一个两通道的光流向量，实际上是每个点的像素位移值
#     flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
 
#     #print(flow.shape)
#     print(flow)
 
#     #笛卡尔坐标转换为极坐标，获得极轴和极角
#     mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
#     hsv[...,0] = ang*180/np.pi/2
#     hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
#     rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
 
#     cv2.imshow('frame2',rgb)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
#     elif k == ord('s'):
#         cv2.imwrite('opticalfb.png',frame2)
#         cv2.imwrite('opticalhsv.png',rgb)
#     prvs = next
 
cap.release()
cv2.destroyAllWindows()