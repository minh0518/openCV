import numpy as np

a=np.array([1,2,3,4])
# �̷��� ����Ʈ�� �־��ָ� �� ����Ʈ�� ���ҷ� ������ 
# �迭�� ������ݴϴ�
print(a) # [1 2 3 4]
print(a.dtype)  # int 32
#�տ� �̹����� �д� �������� uint8�� ���� ���� openCVȯ���̶� �׷��� �� ���̰� 
#���� �̷��� dtype�� �Ϲ����� �������� ���ɴϴ�
print(type(a))
#<class 'numpy.ndarray'>
print(a.shape)
#(4,)    1���� �迭�̹Ƿ� ���� �ϳ��� ������ �˴ϴ�


b=np.array([[1,2,3,4],[5,6,7,8]])

print(b) 
#  [[1 2 3 4]
#   [5 6 7 8]]
print(b.dtype)
#int32
print(type(b))
#<class 'numpy.ndarray'>
print(b.shape)
#(2,4)





c=np.array([[1],[2],[3],[4]])
print(c)
# [[1]
# [2]
# [3]
# [4]]

print(c.shape) #(4,1)



d=np.array([[1],[2],[3],[4]])
print(d)
# [[1]
# [2]
# [3]
# [4]]

print(d.shape) #(4,1)