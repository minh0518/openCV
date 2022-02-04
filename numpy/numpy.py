import numpy as np

a=np.array([1,2,3,4])
# 이렇게 리스트를 넣어주면 이 리스트를 원소로 가지는 
# 배열을 만들어줍니다
print(a) # [1 2 3 4]
print(a.dtype)  # int 32
#앞에 이미지를 읽는 예제에서 uint8이 나온 것은 openCV환경이라 그렇게 뜬 것이고 
#보통 이렇게 dtype은 일반적인 정수형이 나옵니다
print(type(a))
#<class 'numpy.ndarray'>
print(a.shape)
#(4,)    1차원 배열이므로 값이 하나만 나오게 됩니다


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