import tkinter as tk
import cv2
import numpy as np

root=tk.Tk()

root.title("화면")
label=tk.Label(root,text="포토샵 기능을 선택하세요")
root.geometry("250x450+100+100")
label.pack()


cap=cv2.VideoCapture(0)
#노트북 기본 카메라 접근

if cap.isOpened():
    while True:
        ret,img=cap.read()    #카메라 객체를 받은 객체의 프레임 읽기
        if ret:
            cv2.imshow('camera',img)
            if cv2.waitKey(1) != -1:
            #무슨 키를 입력 받았다면 break
                break
        else:
            print('no frame')
            break
            
else:
    print("cant open camera")
    
cap.release()



pos=(-1,-1) #초기 좌표를 튜플로 설정

#각 사진들을 담을 수 있는 변수들을 전역 변수로 선언
rotateImg=()
grayImg=()
emphasizeImg=()
reverseImg=()
liquifyImg=()
clearImg=()
mosaicImg=()


def selectImg():
    global img
    x,y,w,h=cv2.selectROI('origin',img,False,False) 
    #selectROI함수를 사용해서 사진 영역 선택
    if w and h :
        img=img[y:y+h , x:x+w]
    

    
#zoom을 할때 마우스로 클릭을해서 점을 찍고
#해당 좌표를 기준으로 확대를 하기 위해 마우스이벤트 선언
def onMouse1(event,x,y,flags,param):
    global img,pos
    if event ==cv2.EVENT_LBUTTONDOWN:
        pos=(x,y)  
        img_copy=rotateImg.copy() 
        cv2.circle(img_copy,pos,3,(255,0,0),-1) 
        cv2.imshow('origin',img_copy)   
    

#사진 회전&확대 함수
def rotate():
    cv2.imshow('origin',img)
    cv2.setMouseCallback('origin',onMouse1)
    def onChange(x):
        global rotateImg
        angle=cv2.getTrackbarPos('time wise','origin')
        zoom=cv2.getTrackbarPos('size','origin')
        if(zoom>0): #zoom이 땡겨졌을 때는 마우스 이벤트로 받은
                    #좌표를 이용해서 회전+줌 둘다 적용
            m45 = cv2.getRotationMatrix2D((pos[0],pos[1]),-(angle),zoom+1) 
            rotateImg = cv2.warpAffine(img, m45,(cols, rows),None,None,cv2.BORDER_CONSTANT,(0,0,0))
            
        else: #zoom이 땡겨지지 않았을 때는 일반 회전만
            m45 = cv2.getRotationMatrix2D((cols/2,rows/2),-(angle),zoom+1) 
            rotateImg = cv2.warpAffine(img, m45,(cols, rows),None,None,cv2.BORDER_CONSTANT,(0,0,0))
            
        
        cv2.imshow('origin',rotateImg)
        

    
    rows,cols = img.shape[0:2]
    cv2.imshow('origin',img)

    cv2.createTrackbar( 'time wise', 'origin', 0, 360, onChange)  
    cv2.createTrackbar( 'size', 'origin', 0, 3, onChange)  

    
#스레시홀드를 이용해서 일종의 사진 강조 효과 필터를 적용하는 함수
def emphasize():
    global grayImg
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('origin2',grayImg)
    def onChange(x):
        global emphasizeImg
        C=cv2.getTrackbarPos('c','origin2') # 차감상수를 트랙바로 이용해서
                                        #값에 따라 다른 효과를 보여줍니다
        blk_size = 9        # 블럭 사이즈는 고정
        if(C==0):
            cv2.imshow('origin2',grayImg)
        else:
            emphasizeImg = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, blk_size, C)
            cv2.imshow('origin2',emphasizeImg)
    cv2.createTrackbar( 'c', 'origin2', 0, 10, onChange)  
    
    
#사진 반전효과 함수    
def reverse():  
    global reverseImg
    reverseImg=cv2.bitwise_not(img)
    cv2.imshow('origin3',reverseImg)

    

isDragging = False      # 드래그 여부 플래그
#리퀴파이 함수로 직접 마우스로 사진을 수정하는 함수
def liquify():
    global liquifyImg,img
    liquifyImg=img.copy()
    half = 20               # 관심 영역 절반 크기
    win_title='liquifyImg'

    def onMouse(event,x,y,flags,param):     
        global cx1, cy1, isDragging, img,liquifyImg      # 전역변수 참조
        # 마우스 중심 점을 기준으로 대상 영역 따라다니기
        if event == cv2.EVENT_MOUSEMOVE:  
            if not isDragging :
                img_draw = liquifyImg.copy()       
                # 드래그 영역 표시
                cv2.rectangle(img_draw, (x-half, y-half),(x+half, y+half), (255,0,0)) 
                cv2.imshow(win_title, img_draw) # 사각형 표시된 그림 화면 출력
        elif event == cv2.EVENT_LBUTTONDOWN :   
            isDragging = True                   # 드래그 시작
            cx1, cy1 = x, y                     # 드래그 시작된 원래의 위치 좌표 저장
        elif event == cv2.EVENT_LBUTTONUP :
            if isDragging:
                isDragging = False              # 드래그 끝
      
            
    
                # 드래그 시작 좌표와 끝난 좌표로 리퀴파이 적용 함수 호출
                  # 대상 영역 좌표와 크기 설정
                x2, y2, w, h = cx1-half, cy1-half, half*2, half*2
                # 관심 영역 설정
                roi = liquifyImg[y2:y2+h, x2:x2+w].copy()
                out = roi.copy()

                # 관심영역 기준으로 좌표 재 설정
                offset_cx1,offset_cy1 = cx1-x2, cy1-y2
                offset_cx2,offset_cy2 = x-x2, y-y2
    
                # 변환 이전 4개의 삼각형 좌표
                tri1 = [[ (0,0), (w, 0), (offset_cx1, offset_cy1)], # 상,top
                        [ [0,0], [0, h], [offset_cx1, offset_cy1]], # 좌,left
                        [ [w, 0], [offset_cx1, offset_cy1], [w, h]], # 우, right
                        [ [0, h], [offset_cx1, offset_cy1], [w, h]]] # 하, bottom

                # 변환 이후 4개의 삼각형 좌표
                tri2 = [[ [0,0], [w,0], [offset_cx2, offset_cy2]], # 상, top
                        [ [0,0], [0, h], [offset_cx2, offset_cy2]], # 좌, left
                        [ [w,0], [offset_cx2, offset_cy2], [w, h]], # 우, right
                        [ [0,h], [offset_cx2, offset_cy2], [w, h]]] # 하, bottom

    
                for i in range(4):
                    # 각각의 삼각형 좌표에 대해 어핀 변환 적용
                    matrix = cv2.getAffineTransform( np.float32(tri1[i]), np.float32(tri2[i]))
                    warped = cv2.warpAffine( roi.copy(), matrix, (w, h),None, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)
                    # 삼각형 모양의 마스크 생성
                    mask = np.zeros((h, w), dtype = np.uint8)
                    cv2.fillConvexPoly(mask, np.int32(tri2[i]), (255,255,255))
        
                    # 마스킹 후 합성
                    warped = cv2.bitwise_and(warped, warped, mask=mask)
                    out = cv2.bitwise_and(out, out, mask=cv2.bitwise_not(mask))
                    out = out + warped

                # 관심 영역을 원본 영상에 합성
                
                liquifyImg[y2:y2+h, x2:x2+w] = out
                
    
    
    
    cv2.namedWindow(win_title)
    cv2.setMouseCallback(win_title, onMouse) 
    cv2.imshow(win_title, liquifyImg)

# 균등화를 하면 너무 어두워지거나 밝아지므로 균등화 하는 적절한 범위를
#지정해주는 clahe함수를 이용해서 사진의 선명도를 조절하는 필터가 있는 함수
def clear():
    cv2.imshow('CLAHE',img) # 기존의 창을 띄워놓아야 createTrackbar등록이 가능
                        #하므로 미리 창을 띄워줌
    def onChange(x):
        global img,clearImg
        
        d=cv2.getTrackbarPos('depth','CLAHE')
        if(d==0):
            cv2.imshow('CLAHE',img)
        else:
            img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

            #--③ 밝기 채널에 대해서 CLAHE 적용
            clearImg = img_yuv.copy()
            clahe = cv2.createCLAHE(clipLimit=(d), tileGridSize=(8,8)) #CLAHE 생성
            clearImg[:,:,0] = clahe.apply(clearImg[:,:,0])           #CLAHE 적용
            clearImg = cv2.cvtColor(clearImg, cv2.COLOR_YUV2BGR)
            cv2.imshow('CLAHE',clearImg)
        

    cv2.createTrackbar( 'depth', 'CLAHE', 0, 7, onChange)  


#모자이크
def mosaic():
    rate = 15               # 모자이크에 사용할 축소 비율 (1/rate)
    global mosaicImg
    mosaicImg=img.copy()
  
    x,y,w,h = cv2.selectROI('mosaic', mosaicImg, False) # 모자이크를 하고자하는 영역 선택
      
    roi = mosaicImg[y:y+h, x:x+w]   # 관심영역 지정
    roi = cv2.resize(roi, (w//rate, h//rate)) # 1/rate 비율로 축소
    # 원래 크기로 확대
    roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)  
    mosaicImg[y:y+h, x:x+w] = roi   # 원본 이미지에 적용
    cv2.imshow('mosaic', mosaicImg)
    
            

            
#각 단계별로 저장하는 함수들

def saveRotate():
    cv2.imwrite('./rotateImg.jpg',rotateImg)
    print('회전or확대 이미지가 현재 디렉토리에 저장되었습니다!')
def saveGray():
    cv2.imwrite('./grayImg.jpg',grayImg)
    print('흑백 이미지가 현재 디렉토리에 저장되었습니다!')
def saveEmphasize():
    cv2.imwrite('./emphasizeImg.jpg',emphasizeImg)
    print('사진 강조 효과 이미지가 현재 디렉토리에 저장되었습니다!')
def saveReverse():
    cv2.imwrite('./reverseImg.jpg',reverseImg)
    print('반전 이미지가 현재 디렉토리에 저장되었습니다!')
def saveLiquify():
    cv2.imwrite('./liquifyImg.jpg',liquifyImg)
    print('얼굴 수정 이미지가 현재 디렉토리에 저장되었습니다!')
def saveClear():
    cv2.imwrite('./clearImg.jpg',clearImg)
    print('선명도 조절 이미지가 현재 디렉토리에 저장되었습니다!')
def saveMosaic():
    cv2.imwrite('./mosaicImg.jpg',mosaicImg)
    print('모자이크 이미지가 현재 디렉토리에 저장되었습니다!')

    
    
# GUI버튼 등록


button1=tk.Button(root,width=15,text="Select",overrelief="solid",command=selectImg)
button1.pack()


button2=tk.Button(root,width=15,text="Rotate&Zoom-in",overrelief="solid",command=rotate)
button2.pack()
savebutton=tk.Button(root,width=7,text="save",overrelief="solid",command=saveRotate)
savebutton.pack()


button4=tk.Button(root,width=15,text="Emphasize",overrelief="solid",command=emphasize)
button4.pack()
savebutton3=tk.Button(root,width=7,text="save",overrelief="solid",command=saveEmphasize)
savebutton3.pack()



button5=tk.Button(root,width=15,text="Reverse",overrelief="solid",command=reverse)
button5.pack()
savebutton4=tk.Button(root,width=7,text="save",overrelief="solid",command=saveReverse)
savebutton4.pack()




button6=tk.Button(root,width=15,text="Liquify",overrelief="solid",command=liquify)
button6.pack()
savebutton5=tk.Button(root,width=7,text="save",overrelief="solid",command=saveLiquify)
savebutton5.pack()



button7=tk.Button(root,width=15,text="Clear",overrelief="solid",command=clear)
button7.pack()
savebutton6=tk.Button(root,width=7,text="save",overrelief="solid",command=saveClear)
savebutton6.pack()


button7=tk.Button(root,width=15,text="Mosaic",overrelief="solid",command=mosaic)
button7.pack()
savebutton7=tk.Button(root,width=7,text="save",overrelief="solid",command=saveMosaic)
savebutton7.pack()


root.mainloop()



cv2.waitKey(0)
cv2.destroyAllWindows()