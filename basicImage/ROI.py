import cv2
import numpy as np

img=cv2.imread('./insightbook.opencv_project_python-master/img/sunset.jpg')
isDragging=False #드래그 상태를 나타냅니다. 드래그중에면 True.
pos=(-1,-1) #초기 좌표를 튜플로 설정합니다. -1이니까 없는것이죠.
w,h=(-1,-1)



def onMouse(event,x,y,flags,param):
    global isDragging,pos,w,h,img  
	 # 외부 변수를 여기서 사용하기 위해 global(파이썬 문법)
    
    if event ==cv2.EVENT_LBUTTONDOWN:  
		# 처음 누를땐 네모박스 그릴 필요없고
    # 그냥 그 좌표만 넘겨주면 됩니다.
        isDragging=True
        pos = (x,y)     
        #onMouse의 매개변수인 x,y는 기본적으로 마우스의 좌표를 
			#가지고 있습니다

    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging: 
				#마우스를 클릭한 상태에서 MOVE할 때
				
			
            img_draw=img.copy()
            cv2.rectangle(img_draw,pos,(x,y),(255,0,0),2) 
			#pos는 마우스를 클릭했을 때, 그 좌표값을 가지고 있습니다.
		#onMouse 함수의 인자로 있는 x,y는 드래그가 끝났을 때의 x,y좌표를
		#가지고 있습니다
			#마지막2는 두께  
				#x,y에 -1 안한 이유는 img전체에서 그리기 때문(위에 설명합니다)
	
            cv2.imshow('img',img_draw)
	#사각형을 보여줍니다
	#마우스를 드래그 -> cv2.EVENT_MOUSEMOVE 실행 ->
  # x,y가 계속 최신화 ->
 #그려집니다. 

    elif event==cv2.EVENT_LBUTTONUP:
        isDragging=False
        
        #마우스 up하는 순간 늘어난 x,y값과 초기값 pos값의 차이가
				# w,h가 됩니다.
        w=x-pos[0]
        h=y-pos[1]
        


        if w>0 and h>0:
#이 if문은 옆으로만 움직여서 사각형을 안 만들게 되는
#경우도 있는데 이 경우를 배제하는 것입니다

	#여기도 원본에다 안하고 원본을 복사해서 여기다가 사각형을
#그릴 것입니다
            img_draw=img.copy()
            cv2.rectangle(img_draw,pos,(x,y),(0,0,255),2)
					 # 다 그렸으니 색깔만 다르게
			#(드래그 해서 사각형을 그리고 버튼을 떼는 순간 이게 )
            cv2.imshow('img',img_draw) 
			# img_draw를 사용함으로써
		# img에다가 띄워서 또 다른 창이 띄워지는 것을 방지

				#드래그 된 부분을 roi로 설정
            roi=img[pos[1]:pos[1]+h,pos[0]:pos[0]+w]
            cv2.imshow('cropped',roi)
					#roi만 따로 보여줍니다

        else: #박스가 없을때 원본 보여주기
            cv2.imshow('img',img)
            
            
            

cv2.imshow('img',img)
cv2.setMouseCallback('img',onMouse) 
cv2.waitKey(0)
cv2.destroyAllWindows()