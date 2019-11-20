import cv2
img=cv2.imread('./tomoya.jpg')
rigion=[0,0,200,200]
img=img[rigion[0]:rigion[2],rigion[1]:rigion[3]]
cv2.imshow("img",img)
cv2.waitKey(0)
