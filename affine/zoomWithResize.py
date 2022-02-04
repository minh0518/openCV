import cv2
import numpy as np

img=cv2.imread("./insightbook.opencv_project_python-master/img/fish.jpg")
h,w=img.shape[:2]

#ũ�⸦ ���� ������ �༭ ���
dst1=cv2.resize(img,(int(w*0.5),int(h*0.5)),interpolation=cv2.INTER_AREA)

#������ �����ؼ� Ȯ��
dst2=cv2.resize(img,None,None,2,2,cv2.INTER_CUBIC)

cv2.imshow('original',img)
cv2.imshow('small',dst1)
cv2.imshow('big',dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()