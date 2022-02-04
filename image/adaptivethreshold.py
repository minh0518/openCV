import cv2
import numpy as np 
import matplotlib.pyplot as plt 

blk_size = 9        # �� ������
C = 5               # ���� ��� 
img = cv2.imread('./insightbook.opencv_project_python-master/img/sudoku.jpg', cv2.IMREAD_GRAYSCALE) # �׷��� �����Ϸ�  �б�

# ������ �˰������� ���� ��� ���� ��ü �̹����� ����
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#�������� ��谪 �ȹްڴٰ� -1�� �־��µ� 
# ���⿡ ��� ���� ���� �־ cv2.THRESH_OTSU �ɼǶ�����
#�ݿ��� �ȵǴ°ǰ�? 36���� ���� �־ �״�� �Ȱ��� ���´�.

# ������ ������Ȧ�带 ��հ� ����þ� ������ ���� ����
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
                                      cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                     cv2.THRESH_BINARY, blk_size, C)

# ����� Matplot���� ���
imgs = {'Original': img, 'Global-Otsu:%d'%ret:th1, \
        'Adapted-Mean':th2, 'Adapted-Gaussian': th3}
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2,2,i+1)
    plt.title(k)
    plt.imshow(v,'gray')  #��� cmap='gray' ���ִ� ���� ����
    plt.xticks([]),plt.yticks([])

plt.show()