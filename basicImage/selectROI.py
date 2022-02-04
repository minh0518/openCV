import cv2
import numpy as np

img=cv2.imread('./insightbook.opencv_project_python-master/img/sunset.jpg')
x,y,w,h=cv2.selectROI('img',img,False,False) #ù��° False�� ũ�ν���� ���ִ°�
                                        #�ι�° False�� ���콺 ���� ������ ������
			                                #�߽����� ����. �̰� True�� ũ�ν����� False�� ���ݴϴ�.
#x,y,w,h�� �����ݴϴ�.
#selectROI�����ε� imshow���� �巡�� �� �� �簢����
#�����ְ� �巡�װ� ������ ������ show�˴ϴ�.


if w and h :
 #selectROI�� 0���� ���� ��쵵(�����θ� �������� �簢�� ����� �ƴҶ�)
 #�˾Ƽ� ��������� true������ �˸� �˴ϴ�

    roi=img[y:y+h , x:x+w]
    cv2.imshow('cropped',roi) 

cv2.imshow('img',img)  # �̰� ������ �� �ϴ��� �𸣰ڴ�
									#���ص� ��ȭ�� ���µ�..
cv2.waitKey(0)
cv2.destroyAllWindows()