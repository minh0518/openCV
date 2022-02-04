import cv2

cap=cv2.VideoCapture('./insightbook.opencv_project_python-master/img/big_buck.avi')
#동영상 캡처 객체 생성

if cap.isOpened(): #캡처 객체 초기화 확인. 제대로 됐으면 true를 반환
    while True:
        ret,img=cap.read() # 다음 프레임 읽기
        if ret:           #프레임이 정상적으로 읽혔다면 아래 실행
            cv2.imshow('videofile',img)
            #화면에 출력 ( imshow는 이미자나 동영상을 화면에 보여주는 역할을 합니다 )
            cv2.waitKey(25)
            #25ms 지연시킴 (=40fps)
        else:           #다음 프레이미이 더이상 없어서 못 읽을 때
            break       #반복문 탈출
else:
    printf("can't open video")

cap.release()   #캡처 자원 반납
cv2.destroyAllWindows()