import cv2
import numpy as np 
import matplotlib.pyplot as plt 

blk_size = 9        # 블럭 사이즈
C = 5               # 차감 상수 
img = cv2.imread('./insightbook.opencv_project_python-master/img/sudoku.jpg', cv2.IMREAD_GRAYSCALE) # 그레이 스케일로  읽기

# 오츠의 알고리즘으로 단일 경계 값을 전체 이미지에 적용
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#이전에는 경계값 안받겠다고 -1을 넣었는데 
# 여기에 사실 무슨 값을 넣어도 cv2.THRESH_OTSU 옵션때문에
#반영이 안되는건가? 36같은 숫자 넣어도 그대로 똑같이 나온다.

# 적응형 스레스홀드를 평균과 가우시안 분포로 각각 적용
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
                                      cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                     cv2.THRESH_BINARY, blk_size, C)

# 결과를 Matplot으로 출력
imgs = {'Original': img, 'Global-Otsu:%d'%ret:th1, \
        'Adapted-Mean':th2, 'Adapted-Gaussian': th3}
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2,2,i+1)
    plt.title(k)
    plt.imshow(v,'gray')  #계속 cmap='gray' 해주는 것은 여전
    plt.xticks([]),plt.yticks([])

plt.show()