import cv2

cap=cv2.VideoCapture(0)
if cap.isOpened:
    fps=cap.get(cv2.CAP_PROP_FPS)
    width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
																#편의를 위해fps와 width,height는
											           #변수형태로 만든 다음에 사용했습니다

    size=(int(width),int(height)) #VideoWriter의 size는 튜플형태여야 합니다
    out=cv2.VideoWriter('./record.avi',cv2.VideoWriter_fourcc(*'DIVX'),fps,size)
    while True:
        ret,frame=cap.read() #img대신 frame이라는 이름으로 사용합니다
        if ret: #read가 성공했다면
            cv2.imshow('camera-recording',frame) #영상을 보여줍니다
            out.write(frame)  #위에 VideoWriter를 통해 만들어진
												   #cap객체의 write()메소드를 이용해서 저장
            if cv2.waitKey(int(1000/fps)) !=-1:
											#딜레이를 계산해서 바로 집어넣습니다
											#키보드 입력이 들어오면 바로 break하게 됩니다
                break
        else:
            print("No frame")
            break
        out.release()

else:
    print("can't open camera")
    
cap.release()
cv2.destroyAllWindows()