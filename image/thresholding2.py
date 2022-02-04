import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('./insightbook.opencv_project_python-master/img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

_, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

#t_truc.shape[1]�� (a,b)�� ������ b�� ���ϴ� ��
t_truc[:,t_truc.shape[1]-1]=255
t_2zrinv[:,t_2zrinv.shape[1]-1]=255

imgs = {'origin':img, 'BINARY':t_bin, 'BINARY_INV':t_bininv, \
        'TRUNC':t_truc, 'TOZERO':t_2zr, 'TOZERO_INV':t_2zrinv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2,3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]);    plt.yticks([])
    
plt.show()


# ������ �������� ��� �� `imshow�� cmap='gray'`�� �� �̹����� ��� ������ ���� �װ� Ȯ���ŵ�ϴ�.

# �״ϱ� �� �׷��̽������� ��Ⱚ �� ���� ��ο� ���� 87�̶� ġ�� �װ� ������ 0���� �÷��� 0~255�� ���·� ������ ���� ������ ����ϴ� ���Դϴ�.

# ���⼭�� 4��° THRESH_TRUNC(��谪�� ������ ����, �� ������ 0)

# �� ���� ���� �̹����� ��� ���� 0~255�� �ø� ������ 127���ذ��� �������� ������ ��ȯ�ϱ� ������

# ������ ���� ����κ��� ���� ������ �Ǵ� ���Դϴ�.

# �׷��� shape[1]�� ������ 255�� �ٲ�����ϴ�. �׷��� 0~255�̹Ƿ� ���� ���̴� ���� �����ϴ�.