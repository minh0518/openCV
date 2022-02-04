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
            img[pos[1]:pos[1]+h,pos[0]:cols]=(0,0,0)
									#어차피 우리는 화면이 표시된 곳까지만 보여주면
				#되니까 슬라이싱으로 cols를 잡아줬습니다
           #근데 엄밀히 말하면 슬라이싱은 마지막 포함x니까
			# cols+1을 해줘야 하나?
        if pos[1]+h >= rows:
            img[pos[1]:rows,pos[0]:pos[0]+w]=(0,0,0)
        
        elif pos[0]+w <= cols and pos[1]+h <= rows:
                img[pos[1]:pos[1]+h,pos[0]:pos[0]+w]=roi2
        
        cv2.imshow('img', img)  
    
cv2.setMouseCallback('img',onMouse)   


cv2.waitKey(0)
cv2.destroyAllWindows()