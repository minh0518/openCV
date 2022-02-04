import cv2
import numpy as np

win_name = "scanning"
img = cv2.imread("./insightbook.opencv_project_python-master/img/paper.jpg")
rows, cols = img.shape[:2]
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4,2), dtype=np.float32)

def onMouse(event, x, y, flags, param):  #���콺 �̺�Ʈ �ݹ� �Լ� ���� ---�� 
    global  pts_cnt                     # ���콺�� ���� ��ǥ�� ���� ����
    if event == cv2.EVENT_LBUTTONDOWN:  
        cv2.circle(draw, (x,y), 10, (0,255,0), -1) # ��ǥ�� �ʷϻ� ���׶�� ǥ��
        cv2.imshow(win_name, draw)

        pts[pts_cnt] = [x,y]            # ���콺 ��ǥ ����
        pts_cnt+=1
        if pts_cnt == 4:                       # ��ǥ�� 4�� ������ 
            # ��ǥ 4�� �� �����¿� ã�� ---�� 
            sm = pts.sum(axis=1)                 # 4���� ��ǥ ���� x+y ���
            diff = np.diff(pts, axis = 1)       # 4���� ��ǥ ���� x-y ���

            topLeft = pts[np.argmin(sm)]         # x+y�� ���� ���� ���� �»�� ��ǥ
            bottomRight = pts[np.argmax(sm)]     # x+y�� ���� ū ���� ���ϴ� ��ǥ
            topRight = pts[np.argmin(diff)]     # x-y�� ���� ���� ���� ���� ��ǥ
            bottomLeft = pts[np.argmax(diff)]   # x-y�� ���� ū ���� ���ϴ� ��ǥ

            # ��ȯ �� 4�� ��ǥ 
            pts1 = np.float32([topLeft, topRight, bottomRight , bottomLeft])

            # ��ȯ �� ���� ����� ������ ���� ���� ��� ---�� 
            w1 = abs(bottomRight[0] - bottomLeft[0])    # ��� �¿� ��ǥ���� �Ÿ�
            w2 = abs(topRight[0] - topLeft[0])          # �ϴ� �¿� ��ǥ���� �Ÿ�
            h1 = abs(topRight[1] - bottomRight[1])      # ���� ���� ��ǥ���� �Ÿ�
            h2 = abs(topLeft[1] - bottomLeft[1])        # ���� ���� ��ǥ���� �Ÿ�
            width = max([w1, w2])                       # �� �¿� �Ÿ����� �ִ밪�� ������ ��
            height = max([h1, h2])                      # �� ���� �Ÿ����� �ִ밪�� ������ ����
            
            # ��ȯ �� 4�� ��ǥ
            pts2 = np.float32([[0,0], [width-1,0], 
                                [width-1,height-1], [0,height-1]])

            # ��ȯ ��� ��� 
            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            # ���� ��ȯ ����
            result = cv2.warpPerspective(img, mtrx, (width, height))
            cv2.imshow('scanned', result)
cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)    # ���콺 �ݹ� �Լ��� GUI �����쿡 ��� ---��
cv2.waitKey(0)
cv2.destroyAllWindows()