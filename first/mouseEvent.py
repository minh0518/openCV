import cv2

title = 'mouse event'                   # â ����
img = cv2.imread('./insightbook.opencv_project_python-master/img/blank_500.jpg') # ��� �̹��� �б�
cv2.imshow(title, img)                  # ��� �̹��� ǥ��

colors = {'black':(0,0,0),
         'red' : (0,0,255),
         'blue':(255,0,0),
         'green': (0,255,0) } # ���� �̸� ����
#jsó�� Ű : �� ���·� �����ϱ� ����  { } �� ���


def onMouse(event, x, y, flags, param): # ���콺 �ݹ� �Լ� ���� 
    print(event, x, y, flags)                # �Ķ���� ���
    color = colors['black']
    if event == cv2.EVENT_LBUTTONDOWN:  # ���� ��ư ������ ��� 
        # ��Ʈ��Ű�� ����Ʈ Ű�� ��� ���� ���
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY : 
            color = colors['green'] #jsó�� ���ȣ ǥ������� ����
        elif flags & cv2.EVENT_FLAG_SHIFTKEY : # ����Ʈ Ű�� ���� ���
            color = colors['blue']
        elif flags & cv2.EVENT_FLAG_CTRLKEY : # ��Ʈ�� Ű�� ���� ���
            color = colors['red']

        cv2.circle(img, (x,y), 30, color, -1) 
        # ���� 30 ũ���� ������ ���� �ش� ��ǥ�� �׸�
        cv2.imshow(title, img)          
				# �׷��� �̹����� �ٽ� ǥ�� 
		#��� ��濡�ٰ� �� �̺�Ʈ�� ǥ���ؾ��ϱ� ������ �ݵ��
#�̹���â�� �̸��� ���ƾ� �մϴ�!

cv2.setMouseCallback(title, onMouse)    
# ���콺 �ݹ� �Լ��� GUI �����쿡 ��� 

while True:
    if cv2.waitKey(0) & 0xFF == 27:     # esc�� ����
        break
cv2.destroyAllWindows()