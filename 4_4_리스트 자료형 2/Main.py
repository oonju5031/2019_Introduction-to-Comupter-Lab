# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a = [1, 9, 2, 3, 4, 5, 7]

#a를 오름차순으로 변경 한 뒤 출력
a.sort()     #알맞은 함수를 입력해 주세요.
print a

#a에서 9를 꺼낸 뒤 출력
a.pop()
print a

#a의 5 뒤에 6을 추가한 뒤 출력
a.insert(5, 6)
print a

#a의 맨 마지막에 8을 추가하고 출력
a.append(8)
print a

#a를 내림차순 한 뒤 출력
a.sort()
a.reverse()
print a
