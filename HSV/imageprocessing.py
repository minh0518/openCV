import cv2
import numpy as np
import matplotlib.pylab as plt


img=cv2.imread('./insightbook.opencv_project_python-master/img/pump_horse.jpg')
cv2.imshow('img',img)

hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


draw=img.copy()

x,y,w,h=cv2.selectROI('img',img,False)

if w>0 and h>0: 
    roi=draw[y:y+h,x:x+w]
    cv2.rectangle(draw,(x-2,y-2),(x+w+2,y+h+2),(0,0,255),2)
    hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    hist_roi=cv2.calcHist([hsv_roi],[0,1],None,[180,256],[0,180,0,256])
    hist_img=cv2.calcHist([hsv_img],[0,1],None,[180,256],[0,180,0,256])
    
    p1=plt.imshow(hist_roi)
    plt.colorbar(p1)
    plt.show()
    
    p2=plt.imshow(hist_img)
    plt.colorbar(p2)
    plt.show()
    
    
    
    hist_rate=hist_roi/hist_img
    
    h,s,v=cv2.split(hsv_img)
    bp=hist_rate[h.ravel(),s.ravel()]
    bp=bp.reshape(img.shape[:2])
    cv2.normalize(bp,bp,0,255,cv2.NORM_MINMAX)
    bp=bp.astype(np.uint8)
    cv2.imshow('bp',bp)
    
	#¸¶½ºÅ©
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    cv2.filter2D(bp,-1,disc,bp)
    _, mask = cv2.threshold(bp, 1, 255, cv2.THRESH_BINARY)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('result', result)
    
     
cv2.imshow('img',draw)
cv2.waitKey()
cv2.destroyAllWindows()