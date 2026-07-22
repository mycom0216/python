 # 자판기 프로그램을 만든다
    # 1. 사용자가 금액을 입력하면 그 금액이 자판기에 들어간다.
    # 2. 현재 있는 메뉴를 가격과 함께 출력해준다.
    # 3. 메뉴는 다음과 같다. 콜라 : 1000, 사이다 : 900, 이온음료 : 800, 쥬스 : 700, 물 : 500
    # 4. 어떤 메뉴를 고를지 사용자 입력을 받는다.
    # 5. 해당 메뉴를 몇개를 구매할지 입력을 받는다.
    # 6. 해당 메뉴 개수만큼 금액을 차감하여 잔돈을 반환하며, 물건을 제공한다.
    # 7. 단, 금액이 불충분하면, '금액이 부족합니다!' 라는 멘트와 함께, 잔돈을 돌려준다.
    




menu_name = ["코코팜","콜라","사이다","이온음료","쥬스","물"] # 음료이름
menu_price = [1300,1000,900,800,700,500] # 음료가격
user_input = input("1.코코팜 / 2.콜라 / 3.사이다 / 4.이온음료 / 5.쥬스 / 6.물") # 음료항목
user_num = int(user_input) # 사용자가 무엇을 누를것인가 입력받는

if not (1 <= user_num <= len(menu_name)):
    print("숫자 범위가 잘못되었습니다.")
    exit(0) # skip
    
current_name = menu_name[user_num - 1] # 0,1,2,3,4,5 + 1 , 0을 입력하게되면 -1 (index)
current_price = menu_price[user_num - 1] 
print(f"선택한 메뉴는 {current_name}이고 가격은 {current_price}원입니다.")


print("자판기입니다, 어떤 메뉴를 선택하시겠습니까?")
user_item_menu = input("1.코코팜 , 2.콜라, 3.사이다, 4.이온음료, 5.쥬스, 6.물")
user_num = int(user_input)
item_price = [1300,1000,900,800,700,500]
user_count = 10
if not (2 <= user_num <= len(menu_name)):
    print("잘못누르셨습니다.")
    exit(0) 
item_name = menu_name[user_num]
item_price = menu_price[user_num]
print(f"선택한 메뉴는 {item_name}이고 가격은 {item_price}입니다.")


