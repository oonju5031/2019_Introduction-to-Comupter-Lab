# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54] #리스트의 정수값들을 바꾸세요.
odd = 0
even = 0

for i in A:
    if i % 2 == 0: 
        even = even + 1 
    elif i % 2 == 1: 
        odd = odd + 1 
print (odd, even)
