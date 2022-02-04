import cv2
import numpy as np


img=np.zeros((120,120,3),dtype=np.uint8)

rows,cols ,_=img.shape 

for i in range(rows-10): 
    img[i,i:(i+10)]=(0,0,255)
    img[i,(cols-10)-i:cols-i]=(0,255,0)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()