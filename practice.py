# print("Hello World!")

# if----------------------------------------------------

# weather ="비" #input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")




#for----------------------------------------------------

# for waiting_no in [0, 1, 2, 3, 4]:    0 1 2 3 4
#     print("대기번호 :{0}".format(waiting_no))
    
# for wait_no in range(1,6):       1 2 3 4 5
#     print("대기번호 : {0}".format(wait_no))





#while -----------------------------------------------

# customer = "토르"
# index = 5
# while index >=1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer,index))
#     index -= 1
#     if index==0:
#         print("커피는 폐기처분되었습니다")
 
# customer = "아이언맨"
# while True:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))




#continue, break --------------------------------------------

# absent =[2, 5]
# no_book =[7]
# for student in range(1, 11):
#     if student in absent:
#         continue   #조건에 맞으면 다음 반복문으로 넘어감
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(no_book))
#         break      #조건에 맞으면 반복문 멈춤
#     print("{0}아 책을 읽어봐".format(student))




#한줄for ---------------------------------------------------

# students = [1, 2, 3, 4, 5,]

# students = [i+100 for i in students]

# print(students) 