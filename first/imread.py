import cv2
#openCV���̺귯���� ����ϱ� ���� import


img=cv2.imread('./insightbook.opencv_project_python-master/img/girl.jpg')
#�̹����� �ִ� ��θ� ���� �̹����� �о��

if img is not None:
    cv2.imshow('IMG',img) #���� �̹����� ȭ�鿡 ǥ��,
													# IMG�� â�� ����
    cv2.waitKey()     # Ű�� �Էµ� ������ ���. 

    cv2.destroyAllWindows() #��� â �ݱ�
#   cv2.destroywindow('IMG') #'IMG'��� â�� ������ �ִ� �͸� ����
		
    
else:
    print('No image in file')