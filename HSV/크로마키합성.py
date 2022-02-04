import cv2
import numpy as np
import matplotlib.pylab as plt

#--① 크로마키 배경 영상과 합성할 배경 영상 읽기
img1 = cv2.imread('./insightbook.opencv_project_python-master/img/man_chromakey.jpg')
#사람과 크로마키 배경이미지
img2 = cv2.imread('./insightbook.opencv_project_python-master/img/street.jpg')
#길거리 배경 이미지

#--② ROI 선택을 위한 좌표 계산
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]
#이렇게 하면 앞에 2개만 가져오는 것입니다
#shape의 앞에 2개의 값, 즉 width와 height죠.
#img3차원배열에서 :2 한게 아니라 shape로 가져온 1차원배열에서 :2

x = (w2 - w1)//2
y = h2- h1


#--③ 크로마키 배경 영상에서 크로마키 영역을 10픽셀 정도로 지정
chromakey = img1[:10, :10, :]
offset = 20

#--④ 크로마키부분과 사람과크로마키가 있는 사진 둘 다 HSV로 변경
##거리이미지는 냅둠
hsv_chroma = cv2.cvtColor(chromakey, cv2.COLOR_BGR2HSV)
hsv_img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)



#--⑤ 크로마키 영역의 H값에서 offset 만큼 여유를 두어서 범위 지정
# offset 값은 여러차례 시도 후 결정
#chroma_h = hsv_chroma[0]
chroma_h = hsv_chroma[:,:,0]
lower = np.array([chroma_h.min()-offset, 100, 100])
upper = np.array([chroma_h.max()+offset, 255, 255])

#--⑥ 마스크 생성 및 마스킹 후 합성
mask = cv2.inRange(hsv_img, lower, upper)
mask_inv = cv2.bitwise_not(mask)
roi = img2[y:y+h1, x:x+w1]
fg = cv2.bitwise_and(img1, img1, mask=mask_inv)
bg = cv2.bitwise_and(roi, roi, mask=mask)
img2[y:y+h1, x:x+w1] = fg + bg

#--⑦ 결과 출력
cv2.imshow('chromakey', img1)
cv2.imshow('added', img2)
cv2.waitKey()
cv2.destroyAllWindows()