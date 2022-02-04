import cv2
import numpy as np
import matplotlib.pylab as plt

img=cv2.imread('./insightbook.opencv_project_python-master/img/gray_gradient.jpg',cv2.IMREAD_GRAYSCALE)

thresh_np=np.zeros_like(img)
thresh_np[img>127]=255
#여기는 numpy로 한 것. 경계값 127을 넘으면 255를 넣습니다


#경계값 127을 넘으면 value인 255를 넣고
#넘지 못하면 다 0을 넣습니다
_,thresh_cv=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#이건 threshold함수를 사용한 것
#리턴값에서 경계값은 안받고 그냥 이미지만 받습니다.

imgs={'Original':img , 'Numpy API':thresh_np, 'cv2.threshold':thresh_cv}
#원본이미지 (img) , 
#numpy로 변환한 이미지(thresh_np) ,
#threshold로 변환한 이미지 (thresh_cv) 를 
# imgs객체의 값으로 넣어줌


# imgs객체 안에 있는 것들을 출력
for i,(k,v) in enumerate(imgs.items(),1): 
			#아래 subplot을 출력할 때 들어가는 숫자는 1부터여야 합니다.
				#그래서 subplot을 i+1부터 하는게 귀찮아서 여기서
				#인수로 1을 추가로 넣어줌
		#( 1을 넣으면 인덱스를 0이 아니라 1부터 잡습니다  
		# https://www.daleseo.com/python-enumerate/)

    plt.subplot(1,3,i)
    plt.title(k)
    plt.imshow(v,cmap='gray')
    plt.xticks([]);
    plt.yticks([]);
    
plt.show()