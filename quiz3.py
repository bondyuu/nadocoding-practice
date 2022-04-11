# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# http://naver.com
# 규칙1 : http:// 부분은 제외 
# 규칙2 : 처음 만나는 점 (.) 이후 부분은 제외
# 규칙3 : 남은글자 중 처음 세자리 + 글자 갯수 + 글자 내 "e" 갯수 + "!"로 구성

adr = "http://naver.com"

#newadr = adr[7:12] 예제의 답은 똑같이 나오나 주소가 달라지면 답이 틀리게 나옴
newadr = adr.replace("http://","")
newadr = newadr[:newadr.index(".")]

pw = (newadr[0:3] + str(len(newadr)) + str(newadr.count("e")) + "!")

print("{0}의 비밀번호는 {1}입니다.".format(adr, pw))