import cv2

cap=cv2.VideoCapture(0)
#0����ġ�� ��Ʈ�� �⺻ ī�޶��Դϴ�

if cap.isOpened():
    while True:
        ret,img=cap.read()    #ī�޶� ��ü�� ���� ��ü�� ������ �б�
        if ret:
            cv2.imshow('camera',img)
            if cv2.waitKey(1) != -1:
              #�ƹ� Ű�� �Է¹��� �ʴ� ��Ȳ(-1) �� �ƴ϶�� 
							#�� ,���� Ű�� �Է� �޾Ҵٸ� break
                break
        else:
            print('no frame')
            break
            
else:
    print("cant open camera")
    
cap.release()
cv2.destroyAllWindows()