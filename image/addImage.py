import cv2
import numpy as np
import matplotlib.pylab as plt

# ---�� ���꿡 ����� �̹��� �б�
img1 = cv2.imread('./insightbook.opencv_project_python-master/img/wing_wall.jpg')
img2 = cv2.imread('./insightbook.opencv_project_python-master/img/yate.jpg')

# ---�� �̹��� ����
img3 = img1 + img2  # ���ϱ� ����
img4 = cv2.add(img1, img2) # OpenCV �Լ�

imgs = {'img1':img1, 'img2':img2, 'img1+img2': img3, 'cv.add(img1, img2)': img4}

# ---�� �̹��� ���
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2,2, i + 1)
    plt.imshow(v[:,:,::-1])
    plt.title(k)
    plt.xticks([]); plt.yticks([])

plt.show()