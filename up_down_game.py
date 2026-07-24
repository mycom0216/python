target = 34
try_count = 1

while True:
    user_input = input("1~100사이의 숫자를 입력(정수로):")
    
    if not (user_input.isdigit() and (100 >= int(user_input) >= 1)):
        input("잘못된 입력입니다.(Enter)")
        continue
    
    user_num = int(user_input)
    
    if user_num == target:
        input(f"{try_count}회만에 맞추었습니다!(Enter)")
        break
    elif user_num > target:
        input(f"{user_num}은/는 Down!(Enter)")
    else:
        input(f"{user_num}은/는 Up!(Down)")
        try_count += 1
    if user_num == target:
        input(f"{try_count}회만에 맞추었습니다!(Enter)")
        break
    elif user_num > target:
        input(f"{user_num}은/는 Down!(Enter)")
        min_max[1] = user_num - 1
    else:
        input(f"{user_num}은/는 Up!(Down)")
        min_max[0] = user_num + 1
        try_count += 1