import cv2

cap=cv2.VideoCapture(0)
if cap.isOpened:
    fps=cap.get(cv2.CAP_PROP_FPS)
    width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
																#���Ǹ� ����fps�� width,height��
											           #�������·� ���� ������ ����߽��ϴ�

    size=(int(width),int(height)) #VideoWriter�� size�� Ʃ�����¿��� �մϴ�
    out=cv2.VideoWriter('./record.avi',cv2.VideoWriter_fourcc(*'DIVX'),fps,size)
    while True:
        ret,frame=cap.read() #img��� frame�̶�� �̸����� ����մϴ�
        if ret: #read�� �����ߴٸ�
            cv2.imshow('camera-recording',frame) #������ �����ݴϴ�
            out.write(frame)  #���� VideoWriter�� ���� �������
												   #cap��ü�� write()�޼ҵ带 �̿��ؼ� ����
            if cv2.waitKey(int(1000/fps)) !=-1:
											#�����̸� ����ؼ� �ٷ� ����ֽ��ϴ�
											#Ű���� �Է��� ������ �ٷ� break�ϰ� �˴ϴ�
                break
        else:
            print("No frame")
            break
        out.release()

else:
    print("can't open camera")
    
cap.release()
cv2.destroyAllWindows()