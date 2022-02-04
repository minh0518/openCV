import numpy as np
a=np.arange(12).reshape(3,4)
print(a[0][2] ) #2
print(a[1]) # [4 5 6 7]


b=np.arange(12).reshape(3,4)
print(b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(b[0:2 , 1:3] )
# [[1 2]
#  [5 6]]



c=np.arange(12).reshape(3,4)
d=a[0:2 , 1:3]   #인덱싱 사용
#파이썬이라면 그냥 복사본이 넘어가지만, 
#`Numpy는 원본 ( 레퍼런스값)이 넘어가므로` 저렇게 b의 값을 수정하면 원본  a의 값도 같이 바뀝니다.

print(d)
# [[1 2]
#  [5 6]]

d[0,0]=100

print(d)
# [[100   2]
#  [  5   6]]

print(c)
# [[  0 100   2   3]     100으로 바뀌었습니다
#  [  4   5   6   7]
#  [  8   9  10  11]]