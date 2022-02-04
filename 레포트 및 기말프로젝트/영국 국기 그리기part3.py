import cv2
import numpy as np



w=int(input('가로 길이'))
h=int(input('세로 길이'))


img=np.full((h,w,3),255,dtype=np.uint8) 

    
h2=int((h*0.83))

x=(int((h-h2)/2))

for i in range(h2):
    img[int((h-h2)/2):h-int((h-h2)/2),:]=(125,36,0)


rows,cols ,_=img.shape 

for i in range(x,h-x):
      img[i,i-x:(i-x+int(h2*0.2))]=(255,255,255)
      img[i,i-x+int((h2*0.2)/4):i-x+int((h2*0.2)/4)+int(h2*0.1)]=(0,0,255)
         
                        # -i대신 -(i-x)를 해 줌으로써 오른쪽 위에 있는
                        #흰색부분의 왼쪾 시작 부분이 더 왼쪽으로 가버릴 수 있었
                        #지만 (i가 x부터 시작하니까 -되는 부분이 더 커서)
                        # 위와 마찬가지로 i에 x를 빼줘서i가 정확히 열의 개념에선
                        #0부터 들어갈 수 있도록 함.
      img[i,cols-(int(h2*0.2))-(i-x) : cols-(i-x)]=(255,255,255)
      img[i,cols-(int((h2*0.2)/4))-(i-x)-int(h2*0.1) :cols-(int((h2*0.2)/4))-(i-x)]=(0,0,255)
        #항상 반대편 십자가는 cols(오른쪽 끝 좌표)에서 i를 계쏙 빼주는 식이다.
        #그리고 두께표현은 논리상 항상 : 가 있으면 왼쪽에다가 빼줘서 두께를 표현한다.
        
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()