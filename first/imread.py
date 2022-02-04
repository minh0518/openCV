import cv2
#openCV라이브러리를 사용하기 위해 import


img=cv2.imread('./insightbook.opencv_project_python-master/img/girl.jpg')
#이미지가 있는 경로를 통해 이미지를 읽어옴

if img is not None:
    cv2.imshow('IMG',img) #읽은 이미지를 화면에 표시,
													# IMG는 창의 제목
    cv2.waitKey()     # 키가 입력될 때까지 대기. 

    cv2.destroyAllWindows() #모든 창 닫기
#   cv2.destroywindow('IMG') #'IMG'라는 창의 제목이 있는 것만 닫음
		
    
else:
    print('No image in file')