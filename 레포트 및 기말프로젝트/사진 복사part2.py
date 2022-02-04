import cv2
import numpy as np

img = cv2.imread('./insightbook.opencv_project_python-master/img/sunset.jpg')
a,b,w,h=cv2.selectROI('img',img,False,False)
pos = (0, 0)

if w and h :
    roi=img[b:b+h , a:a+w]


roi2=roi.copy()

rows,cols ,_=img.shape 

def onMouse(event,x,y,flags,param):
    global pos
    
    if event == cv2.EVENT_LBUTTONDOWN :
        pos=(x,y) 

        if pos[0]+w >= cols:
            cv2.line(img,(50,50),(150,150),(255,0,0))
            cv2.imshow('img', img) 
			#여기에 cv2.imshow('img', img)를 해줘야 클릭하고 바로
			#대각선이 생기게 됩니다. 
            
        if pos[1]+h >= rows:
            cv2.line(img,(50,50),(150,150),(255,0,0))
            cv2.imshow('img', img) 
    
        else: #아니 이건 왜 실행이 자꾸 되는거야
            img[pos[1]:pos[1]+h,pos[0]:pos[0]+w]=roi2
            cv2.imshow('img', img) 
        
        
    
cv2.setMouseCallback('img',onMouse)   


cv2.waitKey(0)
cv2.destroyAllWindows()