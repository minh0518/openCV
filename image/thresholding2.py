import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('./insightbook.opencv_project_python-master/img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

_, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

#t_truc.shape[1]은 (a,b)가 있으면 b를 말하는 것
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


# 이전의 예제에서 사용 된 `imshow의 cmap='gray'`는 그 이미지의 모든 값들을 보고 그걸 확장시킵니다.

# 그니까 한 그레이스케일의 밝기값 중 제일 어두운 것이 87이라 치면 그걸 억지로 0까지 늘려서 0~255의 상태로 무조건 만든 다음에 출력하는 것입니다.

# 여기서도 4번째 THRESH_TRUNC(경계값을 넘으면 유지, 못 넘으면 0)

# 를 보면 원본 이미지의 밝기 값을 0~255로 늘린 다음에 127기준값을 기준으로 사진을 변환하기 때문에

# 사진을 보면 흰색부분이 많이 나오게 되는 것입니다.

# 그래서 shape[1]의 끝깞을 255로 바꿔버립니다. 그러면 0~255이므로 값을 늘이는 일이 없습니다.