import numpy as np, cv2
import matplotlib.pylab as plt

#--�� �̹��� �б�
img = cv2.imread('./insightbook.opencv_project_python-master/img/girl.jpg')

#--�� ����ũ �����
mask = np.full_like(img,255)
cv2.circle(mask, (150,140), 100, (0,0,0), -1)
#cv2.circle(����̹���, (����x, ����y), ������, (����), ä���)

#--�� ����ŷ
masked = cv2.bitwise_or(img, mask)

#--�� ��� ���
cv2.imshow('original', img)
cv2.imshow('mask', mask)
cv2.imshow('masked', masked)
cv2.waitKey()
cv2.destroyAllWindows()



# xor�����ϸ� �ٸ� ���϶��� 1�� ������ ���Դϴ�.

# �׷��� ������ ���࿡ 11110000�̸�
# ����� 11111111�̶� �����ϸ�
# 00001111 �̷��� ������ �Ǵ� ���Դϴ�.

# ������ 00000000�� �����ϸ�

# �״�� 11110000�� ���ɴϴ�