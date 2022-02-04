import cv2
import numpy as np

img=cv2.imread('./insightbook.opencv_project_python-master/img/sunset.jpg')
x,y,w,h=cv2.selectROI('img',img,False,False) #첫번째 False는 크로스헤어 없애는거
                                        #두번째 False는 마우스 시작 시점을 영역의
			                                #중심으로 지정. 이게 True면 크로스헤어는 False로 해줍니다.
#x,y,w,h를 돌려줍니다.
#selectROI만으로도 imshow없이 드래그 할 때 사각형을
#보여주고 드래그가 끝나면 사진이 show됩니다.


if w and h :
 #selectROI가 0보다 작은 경우도(옆으로만 움직여서 사각형 모양이 아닐때)
 #알아서 잡아줌으로 true인지만 알면 됩니다

    roi=img[y:y+h , x:x+w]
    cv2.imshow('cropped',roi) 

cv2.imshow('img',img)  # 이건 솔직히 왜 하는지 모르겠다
									#안해도 변화가 없는데..
cv2.waitKey(0)
cv2.destroyAllWindows()