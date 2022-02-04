import cv2
import numpy as np

img = cv2.imread('./insightbook.opencv_project_python-master/img/sunset.jpg')
a,b,w,h=cv2.selectROI('img',img,False,False)
pos = (0, 0)

if w and h :
    roi=img[b:b+h , a:a+w]
    print(roi.shape) # 드래그한 roi부분의 shape 확인

roi2=roi.copy()
    #roi로 선택된 영역이  b:b+h , a:a+w 가 있는데
    #여기서 클릭해서 복사된 이미지가 b:b+h , a:a+w를 침범하게 되면
    #roi가 다시 바뀌게 됩니다.
	  #아마 selectROI로 설정된 이 b:b+h , a:a+w 범위는
    #한번 roi에 들어가고 끝이 아니라, 계속해서 
		#b:b+h , a:a+w 여기가 선택이 되어 있게 상태인 것입니다.
    #그래서 b:b+h , a:a+w 여기에 새로운 이미지가 들어가게 된다면 그 순간부턴
    #roi에 새로운 이미지가 또 들어가게 되는 것이죠
    #그래서 roi를 처음에 하나 찍고나서 그걸 roi2로 copy해서 이 고정된 이미지만
    #아래 마우스이벤트에다가 클릭하면 나오게 하는 것입니다.
    #그러면 b:b+h , a:a+w  안에 뭐가 들어가서 roi가 바뀌어도 
		#어차피 바뀌게 된 roi가 아닌 roi2를 출력하기 때문에 문제가 없죠.
    
    #대신! roi2=roi가 아니라 copy로 해야 합니다
    # =로 넘기면 이미지가 넘어가는 것이 아니라 roi에 넘겨줬던 해당 범위
    #[b:b+h , a:a+w]가 넘어가는 것입니다. 그래서 똑같이 이미지가 겹치죠
    #그래서 copy로 이미지(말 그대로 [b:b+h , a:a+w] 가 아니라 
    # [b:b+h , a:a+w]에 해당하는 사진)를 넘겨줘야 합니다.
    
    
def onMouse(event,x,y,flags,param):
    global pos
    
    if event == cv2.EVENT_LBUTTONDOWN :
        pos=(x,y) 
        img[pos[1]:pos[1]+h,pos[0]:pos[0]+w]=roi2
        
        cv2.imshow('img', img)  
        #이렇게 roi를 복사한 다음 inshow로 보여줘야 합니다

        
#여기다가 
#img[pos[1]:pos[1]+h,pos[0]:pos[0]+w]=roi 를 넣어주면 오류가 발생합니다
#pos값이 초기에 선언한 0,0에서 바뀌지 않기 때문입니다.
cv2.setMouseCallback('img',onMouse)   


cv2.waitKey(0)
cv2.destroyAllWindows()