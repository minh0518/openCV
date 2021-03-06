import cv2
import numpy as np



w=int(input('가로 길이'))
h=int(input('세로 길이'))

#사실 x,y가 바뀌는 것은 여긴 의미가 없다. 
#그냥 여기엔 값만 넣어주는 것이기 때문
#다만 아래에 img에 슬라이싱 할때 바뀌는 것은 굉장히 중요하다.
img=np.full((h,w,3),255,dtype=np.uint8) 
# 255만 들가도 되는데 3차원이어서
# 255 255 255 일케 들가는 것. 전혀 상관없음

#3차원 배열 설명을 보면 (a,b,c)가 있으면 bxc로 된 배열이 a개 있는 것입니다
#그러므로 b가 가로이고 a가 세로, 그리고 각각의 픽셀에 3개의 bgr값이 있는 
#것입니다. 그래서 full의 인자로 세로 가로 순으로 넣어 줬습니다
    
h2=int((h*0.83))
# 가로 세로 6:5 이므로
# 가로가 1이라면 세로는 0.83


for i in range(h2):
    img[int((h-h2)/2):h-int((h-h2)/2),:]=(125,36,0)

#가로를 받아서 세로의 길이를 수정합니다.
#슬라이싱으로 y값을 조정해주면 세로의 길이가 수정됩니다.
# >> 가로 세로 6:5비울로 남색 배경이 생성됩니다.

#이전에도 했듯이 슬리이싱을 하는 곳은 가로선(y좌표)가 행이 되므로
# y,x순 입니다

#근데 가로와 세로를 동일하게 입력하지 않으면 애초에 6:5 비율이 생길수가
# 없습니다. 

rows,cols ,_=img.shape 

# int((h-h2)/2는 파란색 남색 배경이 찍히는 첫번째 y좌표입니다
#(사각형에서 세로의 위치)
#(전체높이 - 0.83곱한 높이)/2 하면 위아래 흰색 좌표의 시작점이 나옵니다.
#그걸 i로 돌립니다
for i in range(int((h-h2)/2),h-int((h-h2)/2)):
      img[i,i-(int((h-h2)/2)):(i-(int((h-h2)/2))+int(h2*0.2))]=(255,255,255)
        #이걸 보면 열 부분만 수정을 합니다
        #왜냐하면 행은 range로 값을 다 잡아줬지만
        #(흰,빨 줄을 긋기 위한)열은 range를 따라가면 안됩니다.
        #영국 국기를 보면 빨간줄이 그이는 곳의 열 좌표는 남색부분이 아니라
        #0부터 시작해야 합니다(열좌표가 그렇다는 것입니다!!)
        #그러므로 0부터 시작해야 합니다 그래서 i가 아니라 i-(int((h-h2)/2))로 0부터
        #시작하도록 잡아줍니다
        
#         또한 굵기를 설정하는데 있어서, i값이 열을 가지고 있는데
#         이미 가로를 설정하는것 때문에i가 i-(int((h-h2)/2)) 부터 시작하므로
#         굵기를 설정할 때 역시 i가 아닌 (i-(int((h-h2)/2)) + 굵기
#         를 해줘야 합니다. (i+ a : i+10 ) 가 아닌 (i :i+10 ) 을 해야 초기값이
#         같으므로 우리가 원하는 두께를 얻을 수 있습니다
# >>반드시 (i :i+10 )  가 있으면 처음에 i는 서로 같아야 합니다!
        

#그리고 책의 예제에서도 그렇고 정사각형이 아닌 모형에서는
#x표가 제대로 그려지지 않습니다. 당연하죠. i값이 세로를 기준으로 사선을 그려가는데
#직사각형이면 i인 세로가 끝났는데도 아직 가로가 많이 남은 경우도 있기 때문입니다.

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()