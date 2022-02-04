import cv2
import numpy as np

alpha = 0.5 # �ռ��� ����� ���� ��

#---�� �ռ��� ����� ���� �б�
img1 = cv2.imread('./insightbook.opencv_project_python-master/img/wing_wall.jpg')
img2 = cv2.imread('./insightbook.opencv_project_python-master/img/yate.jpg')

# ---�� NumPy �迭�� ������ ���� �����ؼ� ���� ���� ����
blended = img1 * alpha + img2 * (1-alpha)
blended = blended.astype(np.uint8) # �Ҽ��� �߻��� �����ϱ� ����
cv2.imshow('img1 * alpha + img2 * (1-alpha)', blended)

# ---�� addWeighted() �Լ��� ���� ���� ����
dst = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0) 
cv2.imshow('cv2.addWeighted', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()