import cv2
import numpy as np
import matplotlib.pylab as plt

# �̹����� �׷��� �����Ϸ� �б�
img = cv2.imread('./insightbook.opencv_project_python-master/img/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE) 

# ��� ���� 130���� ����
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)        

#������ �� �� ��� �� �� �ʿ� �����Ƿ� -1�� �ƿ� ��������ϴ�.
t, t_otsu = cv2.threshold(img, -1, 255,  cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
#t���� ��谪��, t_otsu���� �̹����� ���ϴ�

print('otsu threshold:', t) 
# Otsu �˰������� ���õ� ��� �� ���

imgs = {'Original': img, 't:130':t_130, 'otsu:%d'%t: t_otsu}
for i , (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()