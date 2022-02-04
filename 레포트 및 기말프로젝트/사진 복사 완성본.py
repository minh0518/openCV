import cv2
import numpy as np

img = cv2.imread('./insightbook.opencv_project_python-master/img/sunset.jpg')
a,b,w,h=cv2.selectROI('img',img,False,False)
pos = (0, 0)

if w and h :
    roi=img[b:b+h , a:a+w]


roi2=roi.copy()

rows,cols ,_=img.shape 
#화면 전체의 크기를 받아오는데 색상을 표시한 마지막 3은
#필요가 없으므로 _로 넘깁니다
#값이 아니라 shape이므로 색상값이 [ , , ]이렇게 표현되지 않고
# 그냥 3으로 표기가 됩니다

def onMouse(event,x,y,flags,param):
    global pos

    if event == cv2.EVENT_LBUTTONDOWN :
        pos=(x,y) 

        if pos[0]+w >= cols:
            img[pos[1]:pos[1]+h,pos[0]:cols]=roi2[:,:(cols-pos[0])]
                                            #img하면 안됨 또 사진 겹침
                            
        if pos[1]+h >= rows:
            img[pos[1]:rows,pos[0]:pos[0]+w]=roi2[:(rows-pos[1]),:]
       
		 #화면을 벗어나지 않는다면 그냥 클릭한 부분을 기준으로
        #바로 roi2를 넣어줍니다
        elif pos[0]+w <= cols and pos[1]+h <= rows:
                img[pos[1]:pos[1]+h,pos[0]:pos[0]+w]=roi2
        
        cv2.imshow('img', img)  
    
cv2.setMouseCallback('img',onMouse)   


cv2.waitKey(0)
cv2.destroyAllWindows()