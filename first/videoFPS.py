import cv2

cap=cv2.VideoCapture('./insightbook.opencv_project_python-master/img/big_buck.avi')


if cap.isOpened():

    fps=cap.get(cv2.CAP_PROP_FPS)
	#게터를 이용해 동영상 파일의 고유 fps를 읽어옵니다
    delay=int(1000/fps)
  # 읽어온 fps를 토대로 지연시간을 읽어옵니다.
    print("FPS : %f Delay : %d ms"%(fps,delay))
    

#이전에 배운 동영상 재생
    while True:
        ret,img=cap.read()
        if ret:           
            cv2.imshow('videofile',img)
            
            cv2.waitKey(delay)
						#위에서 구한 delay를 넣어줍니다
            
        else:           
            break       
else:
    printf("can't open video")

cap.release()   
cv2.destroyAllWindows()