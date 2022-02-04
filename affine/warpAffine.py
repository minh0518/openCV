import cv2
import numpy as np
from matplotlib import pyplot as plt

file_name = "./insightbook.opencv_project_python-master/img/fish.jpg"
img = cv2.imread(file_name)
rows, cols = img.shape[:2]


# ---�� ��ȯ ��, �� �� 3���� ��ǥ ����
pt1=(100,50)
pt2=(200,50)
pt3=(100,200)
pts1 = np.float32([pt1,pt2,pt3])
pts2 = np.float32([[80, 70], [210, 60], [250, 120]])

# ---�� ��ȯ �� ��ǥ�� �̹����� ǥ��
cv2.circle(img, pt1, 5, (255,0), -1)
cv2.circle(img, pt2, 5, (0,255,0), -1)
cv2.circle(img, pt3, 5, (0,0,255), -1)

#---�� ¦���� 3���� ��ǥ�� ��ȯ ��� ���
mtrx = cv2.getAffineTransform(pts1, pts2)
print(mtrx)
#---�� ���� ��ȯ ����
dst = cv2.warpAffine(img, mtrx, (int(cols*1.5), rows))

#---�� ��� ���
cv2.imshow('origin',img)
cv2.imshow('affin', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()