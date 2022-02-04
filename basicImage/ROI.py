import cv2
import numpy as np

img=cv2.imread('./insightbook.opencv_project_python-master/img/sunset.jpg')
isDragging=False #�巡�� ���¸� ��Ÿ���ϴ�. �巡���߿��� True.
pos=(-1,-1) #�ʱ� ��ǥ�� Ʃ�÷� �����մϴ�. -1�̴ϱ� ���°�����.
w,h=(-1,-1)



def onMouse(event,x,y,flags,param):
    global isDragging,pos,w,h,img  
	 # �ܺ� ������ ���⼭ ����ϱ� ���� global(���̽� ����)
    
    if event ==cv2.EVENT_LBUTTONDOWN:  
		# ó�� ������ �׸�ڽ� �׸� �ʿ����
    # �׳� �� ��ǥ�� �Ѱ��ָ� �˴ϴ�.
        isDragging=True
        pos = (x,y)     
        #onMouse�� �Ű������� x,y�� �⺻������ ���콺�� ��ǥ�� 
			#������ �ֽ��ϴ�

    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging: 
				#���콺�� Ŭ���� ���¿��� MOVE�� ��
				
			
            img_draw=img.copy()
            cv2.rectangle(img_draw,pos,(x,y),(255,0,0),2) 
			#pos�� ���콺�� Ŭ������ ��, �� ��ǥ���� ������ �ֽ��ϴ�.
		#onMouse �Լ��� ���ڷ� �ִ� x,y�� �巡�װ� ������ ���� x,y��ǥ��
		#������ �ֽ��ϴ�
			#������2�� �β�  
				#x,y�� -1 ���� ������ img��ü���� �׸��� ����(���� �����մϴ�)
	
            cv2.imshow('img',img_draw)
	#�簢���� �����ݴϴ�
	#���콺�� �巡�� -> cv2.EVENT_MOUSEMOVE ���� ->
  # x,y�� ��� �ֽ�ȭ ->
 #�׷����ϴ�. 

    elif event==cv2.EVENT_LBUTTONUP:
        isDragging=False
        
        #���콺 up�ϴ� ���� �þ x,y���� �ʱⰪ pos���� ���̰�
				# w,h�� �˴ϴ�.
        w=x-pos[0]
        h=y-pos[1]
        


        if w>0 and h>0:
#�� if���� �����θ� �������� �簢���� �� ����� �Ǵ�
#��쵵 �ִµ� �� ��츦 �����ϴ� ���Դϴ�

	#���⵵ �������� ���ϰ� ������ �����ؼ� ����ٰ� �簢����
#�׸� ���Դϴ�
            img_draw=img.copy()
            cv2.rectangle(img_draw,pos,(x,y),(0,0,255),2)
					 # �� �׷����� ���� �ٸ���
			#(�巡�� �ؼ� �簢���� �׸��� ��ư�� ���� ���� �̰� )
            cv2.imshow('img',img_draw) 
			# img_draw�� ��������ν�
		# img���ٰ� ����� �� �ٸ� â�� ������� ���� ����

				#�巡�� �� �κ��� roi�� ����
            roi=img[pos[1]:pos[1]+h,pos[0]:pos[0]+w]
            cv2.imshow('cropped',roi)
					#roi�� ���� �����ݴϴ�

        else: #�ڽ��� ������ ���� �����ֱ�
            cv2.imshow('img',img)
            
            
            

cv2.imshow('img',img)
cv2.setMouseCallback('img',onMouse) 
cv2.waitKey(0)
cv2.destroyAllWindows()