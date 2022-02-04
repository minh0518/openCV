import cv2

cap=cv2.VideoCapture('./insightbook.opencv_project_python-master/img/big_buck.avi')


if cap.isOpened():

    fps=cap.get(cv2.CAP_PROP_FPS)
	#���͸� �̿��� ������ ������ ���� fps�� �о�ɴϴ�
    delay=int(1000/fps)
  # �о�� fps�� ���� �����ð��� �о�ɴϴ�.
    print("FPS : %f Delay : %d ms"%(fps,delay))
    

#������ ��� ������ ���
    while True:
        ret,img=cap.read()
        if ret:           
            cv2.imshow('videofile',img)
            
            cv2.waitKey(delay)
						#������ ���� delay�� �־��ݴϴ�
            
        else:           
            break       
else:
    printf("can't open video")

cap.release()   
cv2.destroyAllWindows()