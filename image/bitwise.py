import numpy as np, cv2
import matplotlib.pylab as plt

#--① 이미지 읽기
img = cv2.imread('./insightbook.opencv_project_python-master/img/girl.jpg')

#--② 마스크 만들기
mask = np.full_like(img,255)
cv2.circle(mask, (150,140), 100, (0,0,0), -1)
#cv2.circle(대상이미지, (원점x, 원점y), 반지름, (색상), 채우기)

#--③ 마스킹
masked = cv2.bitwise_or(img, mask)

#--④ 결과 출력
cv2.imshow('original', img)
cv2.imshow('mask', mask)
cv2.imshow('masked', masked)
cv2.waitKey()
cv2.destroyAllWindows()



# xor연산하면 다른 값일때만 1이 나오는 것입니다.

# 그래서 색깔이 만약에 11110000이면
# 흰색인 11111111이랑 연산하면
# 00001111 이렇게 반전이 되는 것입니다.

# 검정인 00000000와 연산하면

# 그대로 11110000이 나옵니다