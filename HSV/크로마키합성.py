import cv2
import numpy as np
import matplotlib.pylab as plt

#--�� ũ�θ�Ű ��� ����� �ռ��� ��� ���� �б�
img1 = cv2.imread('./insightbook.opencv_project_python-master/img/man_chromakey.jpg')
#����� ũ�θ�Ű ����̹���
img2 = cv2.imread('./insightbook.opencv_project_python-master/img/street.jpg')
#��Ÿ� ��� �̹���

#--�� ROI ������ ���� ��ǥ ���
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]
#�̷��� �ϸ� �տ� 2���� �������� ���Դϴ�
#shape�� �տ� 2���� ��, �� width�� height��.
#img3�����迭���� :2 �Ѱ� �ƴ϶� shape�� ������ 1�����迭���� :2

x = (w2 - w1)//2
y = h2- h1


#--�� ũ�θ�Ű ��� ���󿡼� ũ�θ�Ű ������ 10�ȼ� ������ ����
chromakey = img1[:10, :10, :]
offset = 20

#--�� ũ�θ�Ű�κа� �����ũ�θ�Ű�� �ִ� ���� �� �� HSV�� ����
##�Ÿ��̹����� ����
hsv_chroma = cv2.cvtColor(chromakey, cv2.COLOR_BGR2HSV)
hsv_img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)



#--�� ũ�θ�Ű ������ H������ offset ��ŭ ������ �ξ ���� ����
# offset ���� �������� �õ� �� ����
#chroma_h = hsv_chroma[0]
chroma_h = hsv_chroma[:,:,0]
lower = np.array([chroma_h.min()-offset, 100, 100])
upper = np.array([chroma_h.max()+offset, 255, 255])

#--�� ����ũ ���� �� ����ŷ �� �ռ�
mask = cv2.inRange(hsv_img, lower, upper)
mask_inv = cv2.bitwise_not(mask)
roi = img2[y:y+h1, x:x+w1]
fg = cv2.bitwise_and(img1, img1, mask=mask_inv)
bg = cv2.bitwise_and(roi, roi, mask=mask)
img2[y:y+h1, x:x+w1] = fg + bg

#--�� ��� ���
cv2.imshow('chromakey', img1)
cv2.imshow('added', img2)
cv2.waitKey()
cv2.destroyAllWindows()