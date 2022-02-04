import cv2

cap=cv2.VideoCapture('./insightbook.opencv_project_python-master/img/big_buck.avi')
#������ ĸó ��ü ����

if cap.isOpened(): #ĸó ��ü �ʱ�ȭ Ȯ��. ����� ������ true�� ��ȯ
    while True:
        ret,img=cap.read() # ���� ������ �б�
        if ret:           #�������� ���������� �����ٸ� �Ʒ� ����
            cv2.imshow('videofile',img)
            #ȭ�鿡 ��� ( imshow�� �̹��ڳ� �������� ȭ�鿡 �����ִ� ������ �մϴ� )
            cv2.waitKey(25)
            #25ms ������Ŵ (=40fps)
        else:           #���� �����̹��� ���̻� ��� �� ���� ��
            break       #�ݺ��� Ż��
else:
    printf("can't open video")

cap.release()   #ĸó �ڿ� �ݳ�
cv2.destroyAllWindows()