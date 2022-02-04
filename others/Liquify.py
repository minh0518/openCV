import cv2
import numpy as np

win_title = 'Liquify'   # â �̸�
half = 50               # ���� ���� ���� ũ��
isDragging = False      # �巡�� ���� �÷���

# �������� �Լ�
def liquify(img, cx1,cy1, cx2,cy2) :
    # ��� ���� ��ǥ�� ũ�� ����
    x, y, w, h = cx1-half, cy1-half, half*2, half*2
    # ���� ���� ����
    roi = img[y:y+h, x:x+w].copy()
    out = roi.copy()

    # ���ɿ��� �������� ��ǥ �� ����
    offset_cx1,offset_cy1 = cx1-x, cy1-y
    offset_cx2,offset_cy2 = cx2-x, cy2-y
    
    # ��ȯ ���� 4���� �ﰢ�� ��ǥ
    tri1 = [[ (0,0), (w, 0), (offset_cx1, offset_cy1)], # ��,top
            [ [0,0], [0, h], [offset_cx1, offset_cy1]], # ��,left
            [ [w, 0], [offset_cx1, offset_cy1], [w, h]], # ��, right
            [ [0, h], [offset_cx1, offset_cy1], [w, h]]] # ��, bottom

    # ��ȯ ���� 4���� �ﰢ�� ��ǥ
    tri2 = [[ [0,0], [w,0], [offset_cx2, offset_cy2]], # ��, top
            [ [0,0], [0, h], [offset_cx2, offset_cy2]], # ��, left
            [ [w,0], [offset_cx2, offset_cy2], [w, h]], # ��, right
            [ [0,h], [offset_cx2, offset_cy2], [w, h]]] # ��, bottom

    
    for i in range(4):
        # ������ �ﰢ�� ��ǥ�� ���� ���� ��ȯ ����
        matrix = cv2.getAffineTransform( np.float32(tri1[i]), \
                                         np.float32(tri2[i]))
        warped = cv2.warpAffine( roi.copy(), matrix, (w, h), \
            None, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)
        # �ﰢ�� ����� ����ũ ����
        mask = np.zeros((h, w), dtype = np.uint8)
        cv2.fillConvexPoly(mask, np.int32(tri2[i]), (255,255,255))
        
        # ����ŷ �� �ռ�
        warped = cv2.bitwise_and(warped, warped, mask=mask)
        out = cv2.bitwise_and(out, out, mask=cv2.bitwekise_not(mask))
        out = out + warped

    # ���� ������ ���� ���� �ռ�
    img[y:y+h, x:x+w] = out
    return img 

# ���콺 �̺�Ʈ �ڵ� �Լ�
def onMouse(event,x,y,flags,param):     
    global cx1, cy1, isDragging, img      # �������� ����
    # ���콺 �߽� ���� �������� ��� ���� ����ٴϱ�
    if event == cv2.EVENT_MOUSEMOVE:  
        if not isDragging :
            img_draw = img.copy()       
            # �巡�� ���� ǥ��
            cv2.rectangle(img_draw, (x-half, y-half), \
                    (x+half, y+half), (0,255,0)) 
            cv2.imshow(win_title, img_draw) # �簢�� ǥ�õ� �׸� ȭ�� ���
    elif event == cv2.EVENT_LBUTTONDOWN :   
        isDragging = True                   # �巡�� ����
        cx1, cy1 = x, y                     # �巡�� ���۵� ������ ��ġ ��ǥ ����
    elif event == cv2.EVENT_LBUTTONUP :
        if isDragging:
            isDragging = False              # �巡�� ��
            # �巡�� ���� ��ǥ�� ���� ��ǥ�� �������� ���� �Լ� ȣ��
            liquify(img, cx1, cy1, x, y)    
            cv2.imshow(win_title, img)

if __name__ == '__main__' :
    img = cv2.imread("./insightbook.opencv_project_python-master/img/man_face.jpg")
    h, w = img.shape[:2]

    cv2.namedWindow(win_title)
    cv2.setMouseCallback(win_title, onMouse) 
    cv2.imshow(win_title, img)
    while True:
        key = cv2.waitKey(1)
        if key & 0xFF == 27:
            break
    cv2.destroyAllWindows()