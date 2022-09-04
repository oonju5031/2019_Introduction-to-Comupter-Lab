# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 4번, 5번의 경우 x = y.함수(z)를 이용하면 됩니다.

a = "aBCdefGhijklmnopqRstuvWxyz"
b = ','

# e의 위치를 찾습니다
print a.find('e')

# a를 대문자로 바꿉니다
print a.upper()

# a를 소문자로 바꿉니다
print a.lower()

# a의 모든 문자 사이에 콤마를 삽입합니다
print ','.join(a)

# b에 저장합니다
b = ','.join(a)

# 저장된 문자열을 콤마로 나눕니다
print b.split(',')
