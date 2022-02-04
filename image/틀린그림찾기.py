import cv2
import numpy as np

#--① 합성에 사용할 영상 읽기, 전경 영상은 4채널 png 파일
img_fg = cv2.imread('./insightbook.opencv_project_python-master/img/opencv_logo.png', cv2.IMREAD_UNCHANGED)
img_bg = cv2.imread('./insightbook.opencv_project_python-master/img/girl.jpg')

#--② 알파채널을 이용해서 마스크와 역마스크 생성
_, mask = cv2.threshold(img_fg[:,:,3], 1, 255, cv2.THRESH_BINARY)
											# 3 은 0,1,2까지가 아니라 [3]이어서
										#알파채널만 가져오게 됨.
#mask는 그러면 결국 흰,검만 들어간 2차원 배열이 된다

mask_inv = cv2.bitwise_not(mask)

#--③ 전경 영상 크기로 배경 영상에서 ROI 잘라내기
img_fg = cv2.cvtColor(img_fg, cv2.COLOR_BGRA2BGR)
h, w = img_fg.shape[:2]
roi = img_bg[10:10+h, 10:10+w ]

#--④ 마스크 이용해서 오려내기
masked_fg = cv2.bitwise_and(img_fg, img_fg, mask=mask)
#2개를 and하면 똑같아지는데 여기에 mask를 넣는다
#mask는위에서 알파채널을 통해 전경의 255부분을
#제외하곤 다 0이다. 
#그러므로 masked_fg 에도 이제 255인 부분인 글자와 로고 부분만 남고
#여기서 나머지 배경 부분은 0이 되어서 검정이 된다.


#여기서 사용하는 roi는 실제 배경으로 사용될 girl이미지의 roi입니다.
masked_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
#반대로 아까 합성할 영역을 지정해 준 roi부분에
# mask_inv한 배경부분만 mask를 통한 and를 해줘서 배경이 255가 되고
#전경이 0이 된다.
#그러면 배경부분은 원래 girl이미지의 배경에 
#opencv_logo부분만큼 검정색으로 된다

#--⑥ 이미지 합성
#로고부분만 있는 것과 로고부분과 동일한 크기의 배경부분을 합친다
added = masked_fg + masked_bg
# 브로드캐스팅해도 한쪾에 0이어서 클리핑이 일어나지 않는다.

img_bg[10:10+h, 10:10+w] = added

cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('masked_fg', masked_fg)
cv2.imshow('masked_bg', masked_bg)
cv2.imshow('added', added)
cv2.imshow('result', img_bg)
cv2.waitKey()
cv2.destroyAllWindows()