# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 리스트 A
A = [1, 2, 3, 'a', 'b', 'c', 'd', [7, 8, 9]]

# 리스트 A의 4번째 값
print A[3]

# 리스트 A의 5번째 값을 'python'으로 변경
A[4] = 'python'
print A

# 리스트 A의 1번째부터 4번째 값을 'f', 'o', 'o', 'd'로 변경
A[0:4] = ['f','o','o','d']
print A
