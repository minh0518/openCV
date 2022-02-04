import cv2
import numpy as np
import matplotlib.pylab as plt

img=cv2.imread("./insightbook.opencv_project_python-master/img/fish.jpg")

h,w=img.shape[:2]

m_small=np.float32([[0.5,0,0],
                    [0,0.5,0]])
m_big=np.float32([[2,0,0],
                [0,2,0]])

dst1=cv2.warpAffine(img,m_small,( int(h*0.5),int(w*0.5) ) )
dst2=cv2.warpAffine(img,m_big,( int(h*2),int(w*2) ) )


dst3=cv2.warpAffine(img,m_small,( int(h*0.5),int(w*0.5) ) , None , cv2.INTER_AREA)
dst4=cv2.warpAffine(img,m_big,( int(h*2),int(w*2) ) , None , cv2.INTER_CUBIC)

cv2.imshow('original',img)
cv2.imshow('small',dst1)
cv2.imshow('big',dst2)
cv2.imshow('small INTER_AREA',dst3)
cv2.imshow('big INTER_AREA',dst4)

cv2.waitKey(0)
cv2.destroyAllWindows()