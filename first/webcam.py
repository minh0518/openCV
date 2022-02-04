import cv2

cap=cv2.VideoCapture(0)
#0번장치가 노트북 기본 카메라입니다

if cap.isOpened():
    while True:
        ret,img=cap.read()    #카메라 객체를 받은 객체의 프레임 읽기
        if ret:
            cv2.imshow('camera',img)
            if cv2.waitKey(1) != -1:
              #아무 키를 입력받지 않는 상황(-1) 이 아니라면 
							#즉 ,무슨 키를 입력 받았다면 break
                break
        else:
            print('no frame')
            break
            
else:
    print("cant open camera")
    
cap.release()
cv2.destroyAllWindows()