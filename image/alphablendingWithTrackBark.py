import cv2
import numpy as np

win_name = 'Alpha blending'     # â �̸�
trackbar_name = 'fade'          # Ʈ���� �̸�

# ---�� Ʈ���� �̺�Ʈ �ڵ鷯 �Լ�
def onChange(x):
    alpha = x/100
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0) 
    cv2.imshow(win_name, dst)


# ---�� �ռ� ���� �б�
img1 = cv2.imread('./insightbook.opencv_project_python-master/img/man_face.jpg')
img2 = cv2.imread('./insightbook.opencv_project_python-master/img/lion_face.jpg')

# ---�� �̹��� ǥ�� �� Ʈ���� ���̱�
cv2.imshow(win_name, img1)
cv2.createTrackbar(trackbar_name, win_name, 0, 100, onChange)
#Ʈ���ٰ� 0~100���� �����̸鼭 onChange�� x�� ���� ���ϴ�.


cv2.waitKey()
cv2.destroyAllWindows()