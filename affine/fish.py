import cv2
import numpy as np
import matplotlib.pylab as plt

img=cv2.imread("./insightbook.opencv_project_python-master/img/fish.jpg")


rows,cols=img.shape[:2]


x,y=100,50

mtrx=np.float32([[1,0,x],
                [0,1,y]])

dst=cv2.warpAffine(img,mtrx,(cols+x,rows+y))
dst2=cv2.warpAffine(img,mtrx,(cols+x,rows+y),None,cv2.INTER_LINEAR,cv2.BORDER_CONSTANT,(255,0,0))
dst3=cv2.warpAffine(img,mtrx,(cols+x,rows+y),None,cv2.INTER_LINEAR,cv2.BORDER_REFLECT)
#dst2,3이 추가되었습니다.

cv2.imshow('original',img)
cv2.imshow('trans1',dst)
cv2.imshow('trans2',dst2)
cv2.imshow('trans3',dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()