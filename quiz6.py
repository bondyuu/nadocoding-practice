# 표준 체중을 구하는 프로그램을 작성하시오
# 표준체중 : 각 개인의 키에 적당한 체중

# 남자 : 키 * 키 * 22
# 여자 : 키 * 키 * 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         함수명 : std_weight
#         전달값 : 키, 성별
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

def std_weight(height, gender):
    if gender == "남":
        weight = round(height * height * 22 / 10000,2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height,weight))
    else:
        weight = round(height * height * 21 / 10000,2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg입니다.".format(height,weight))
        
std_weight(160,"여")