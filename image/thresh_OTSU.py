import cv2
import numpy as np
import matplotlib.pylab as plt

# 이미지를 그레이 스케일로 읽기
img = cv2.imread('./insightbook.opencv_project_python-master/img/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE) 

# 경계 값을 130으로 지정
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)        

#오츠로 할 때 경계 값 은 필요 없으므로 -1로 아예 비워버립니다.
t, t_otsu = cv2.threshold(img, -1, 255,  cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
#t에는 경계값이, t_otsu에는 이미지가 들어갑니다

print('otsu threshold:', t) 
# Otsu 알고리즘으로 선택된 경계 값 출력

imgs = {'Original': img, 't:130':t_130, 'otsu:%d'%t: t_otsu}
for i , (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()