import cv2
import numpy as np



w=int(input('가로 길이'))
h=int(input('세로 길이'))


img=np.full((h,w,3),255,dtype=np.uint8) 

    
h2=int((h*0.83))

x=(int((h-h2)/2))
# x는 위 아래 흰색부분들의 각 높이값입니다
# 원래 그대로 썼었는데 코드가 너무 길어져서 변수형태로 바꿨습니다

#세부 비율을 모르면 전체 비율로
#빨간색 줄은 흰색 줄의 절반이라는데 만약 흰색줄의 두께를 모르겠다면
#(여기선 슬라이싱으로 쓰는데 : 가 난무하는 곳에서 또 :로 작성된 것의 길이를
#알아오기 너무 까다롭다)
#전체의 10%로 계산하면 된다.
for i in range(h2):
    img[int((h-h2)/2):h-int((h-h2)/2),:]=(125,36,0)


rows,cols ,_=img.shape 

for i in range(x,h-x):
      img[i,i-x:(i-x+int(h2*0.2))]=(255,255,255)
      img[i,i-x+int((h2*0.2)/4):i-x+int((h2*0.2)/4)+int(h2*0.1)]=(0,0,255)
            #빨간색이 다 그려졌을때 흰색 줄의 50%를 차지해야 하므로
            #1/4지점에서 3/4지점까지 끝나야 한다
            #그럼 양 옆에 1/4지점이 있게 되어서 딱 중앙에 들어오게 된다.
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()