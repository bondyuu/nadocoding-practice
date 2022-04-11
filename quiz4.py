#당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
#참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
#댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#추첨 프로그램을 작성하시오.

#조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
#조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
#조건3 : random 모듈의 shuffle과 smaple을 활용

from random import *

# lst = list(range(1,21))
# shuffle(lst)
# chicken = sample(lst,1)
# lst.pop(chicken)
# coffee = sample(lst, 3)

users = range(1,21)
users = list(users)

shuffle(users)

winners = sample(users,4)

# print("""
# -- 당첨자 발표 --
# 치킨 당첨자 : chicken
# 커피 당첨자 : coffee
# -- 축하합니다 --
# """)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다. --")