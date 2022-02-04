import cv2
import numpy as np
import matplotlib.pylab as plt

img=cv2.imread('./insightbook.opencv_project_python-master/img/gray_gradient.jpg',cv2.IMREAD_GRAYSCALE)

thresh_np=np.zeros_like(img)
thresh_np[img>127]=255
#����� numpy�� �� ��. ��谪 127�� ������ 255�� �ֽ��ϴ�


#��谪 127�� ������ value�� 255�� �ְ�
#���� ���ϸ� �� 0�� �ֽ��ϴ�
_,thresh_cv=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#�̰� threshold�Լ��� ����� ��
#���ϰ����� ��谪�� �ȹް� �׳� �̹����� �޽��ϴ�.

imgs={'Original':img , 'Numpy API':thresh_np, 'cv2.threshold':thresh_cv}
#�����̹��� (img) , 
#numpy�� ��ȯ�� �̹���(thresh_np) ,
#threshold�� ��ȯ�� �̹��� (thresh_cv) �� 
# imgs��ü�� ������ �־���


# imgs��ü �ȿ� �ִ� �͵��� ���
for i,(k,v) in enumerate(imgs.items(),1): 
			#�Ʒ� subplot�� ����� �� ���� ���ڴ� 1���Ϳ��� �մϴ�.
				#�׷��� subplot�� i+1���� �ϴ°� �����Ƽ� ���⼭
				#�μ��� 1�� �߰��� �־���
		#( 1�� ������ �ε����� 0�� �ƴ϶� 1���� ����ϴ�  
		# https://www.daleseo.com/python-enumerate/)

    plt.subplot(1,3,i)
    plt.title(k)
    plt.imshow(v,cmap='gray')
    plt.xticks([]);
    plt.yticks([]);
    
plt.show()