#train_num = 1
#train_set = 0

#if train_num == 1:
    #print(f"기차 {train_num}번은 여수로 간다")
#else:
    #print(f"기차 {train_num}번은 부산으로 간다")
    
#num = 1
#if num == 1:
    #print("숫자가 1입니다")
#print("프로그램 종료")

#num = 2

#if num == 1:
    #print("숫자의 내용은 1입니다.")
    
    #print("숫자가 출력되었습니다.")
    #print("프로그램을 종료 하시겠습니까?")
    
    #switch = True
    
    #if switch == True:
        #print("프로그램을 정상종료합니다.")
        
#money = 2100

#if money > 2000:
    #print("택시를 타고 집에 간다")
#else:
    #print("걸어간다")

#print("집에 도착했다")

#score = 80

#if 100 >= score > 90:
    #print("A등급")
#if 90 >= score > 80:
    #print("B등급")
#if 80 >= score > 70:
    #print("C등급")
#if 70 >= score > 60:
    #print("D등급")


#다중 분기

#score = 100

#if 100 >= score > 90:
    #print("A등급")
#elif score > 80:
    #print("B등급")
#elif score > 70:
    #print("C등급")
#elif score > 60:
   # print("D등급")
#else:
    #print("B등급")
    
# 이 놀이공원은 나이마다 다르게 비용을 청구합니다.
# 1 ~ 12살까지는 어린이비용을 받아서 5000원이고
# 13 ~ 50살까지는 성인비용을 10000원을 받습니다.
# 51세거나 이보다 많은 나이의 경우에는 3000원 받습니다.
# 나이에 따라 얼마를 내야하는지 출력하는 프로그램을 만드세요

#age = 20

#if age < 13:
    #print("5000원 내야합니다.")
#elif age > 50:
    #print("3000원 내야합니다.")
#else:
    #print("10000원 내야합니다.")


hair = "빨강"
pants = "파랑"

if (hair == "빨강") or (pants == "파랑"):
    print("우리가 찾던 사람입니다.")
    
# input() 입력값 반환 함수

#user_input = input("1. 확인 / 2. 취소 번호를 선택해주세요 :")
#
#if user_input.isdigit():
    #user_input = int(user_input)
#else :
    #print("입력을 잘못했습니다.")
#print(user_input)

#user_input = input("0-100사이의 정수를 입력해주세요")
#user_num = int(user_input)

#if 100 >= user_num > 90:
    #print("A등급")
#elif 90 >= user_num > 80:
    #print("B등급")
#elif 80 >= user_num > 70:
    #print("C등급")
#elif 70 >= user_num > 60:
    #print("D등급")
#else:
    #print("F등급")
    
    #user_input = input("나이를 정수로 입력하세요.")
    
    #user_num = int(user_input)
    
    #if user_num < 13:
        #print("5000원 내야합니다.")
    #elif    user_num > 50:
        #print("3000원 내야합니다.")
    #else:
        #print("10000원 내야합니다.")
    
    
    
    # 다중필터링: 성적 평가 시스템
    scores = (80, 70, 100, 60)
    avg = (scores[0] + scores[1] + scores[2] + scores[3] / 4) #avg : 에버리지의 줄임말
    under = (scores[0] < 50) or (scores[1] < 50) or (scores[2] < 50) or (scores[3] < 50)
    
    if avg >= 60:
        print("휴일 부여")
    else:
        print("휴일 없음")
    if under:
        print("보충 수업 있음")
    else:
        print("보충 수업 없음")
    if (100 in scores) and (not under):
        print("상장 수여")
    else:
        print("상장 없음")
    
    
   
    








    