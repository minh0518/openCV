import cv2
import numpy as np

win_name = 'Alpha blending'     # 창 이름
trackbar_name = 'fade'          # 트렉바 이름

# ---① 트렉바 이벤트 핸들러 함수
def onChange(x):
    alpha = x/100
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0) 
    cv2.imshow(win_name, dst)


# ---② 합성 영상 읽기
img1 = cv2.imread('./insightbook.opencv_project_python-master/img/man_face.jpg')
img2 = cv2.imread('./insightbook.opencv_project_python-master/img/lion_face.jpg')

# ---③ 이미지 표시 및 트렉바 붙이기
cv2.imshow(win_name, img1)
cv2.createTrackbar(trackbar_name, win_name, 0, 100, onChange)
#트랙바가 0~100까지 움직이면서 onChange의 x로 값이 들어갑니다.


cv2.waitKey()
cv2.destroyAllWindows()