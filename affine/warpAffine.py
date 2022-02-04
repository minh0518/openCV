import cv2
import numpy as np
from matplotlib import pyplot as plt

file_name = "./insightbook.opencv_project_python-master/img/fish.jpg"
img = cv2.imread(file_name)
rows, cols = img.shape[:2]


# ---① 변환 전, 후 각 3개의 좌표 생성
pt1=(100,50)
pt2=(200,50)
pt3=(100,200)
pts1 = np.float32([pt1,pt2,pt3])
pts2 = np.float32([[80, 70], [210, 60], [250, 120]])

# ---② 변환 전 좌표를 이미지에 표시
cv2.circle(img, pt1, 5, (255,0), -1)
cv2.circle(img, pt2, 5, (0,255,0), -1)
cv2.circle(img, pt3, 5, (0,0,255), -1)

#---③ 짝지은 3개의 좌표로 변환 행렬 계산
mtrx = cv2.getAffineTransform(pts1, pts2)
print(mtrx)
#---④ 어핀 변환 적용
dst = cv2.warpAffine(img, mtrx, (int(cols*1.5), rows))

#---⑤ 결과 출력
cv2.imshow('origin',img)
cv2.imshow('affin', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()