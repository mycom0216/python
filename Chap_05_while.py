## for,while
#n = 0

#while n < 4:
    #print("a")
    #n += 1
    
#user_input = input("입력(종료시 '/q'): ")    
    
#while user_input!= "/q":
    #print(user_input)
    #user_input = input("입력(종료시 '/q'): ")
    
    
    
#user_input = input("입력(종료시 '/q'): ")
    
#while user_input!= "/q":
    #if user_input.isdigit():
        #print(f"{user_input}원입니다.")
    #else:
        #print(user_input)
    #user_input = input("입력(종료시 '/q'): ")
    
    
    # 1-10까지 1씩 증가하면서 출력하는 반복문
    
#num = 1
#while num < 11:
            #print(num)
#num += 1
       
     
       
    # 10-0 까지 1씩 감소하면서 출력하는 반복문
#num2 = 10
#while num2 >= 0:
        #print(num2)
        #num2 -= 1  
        
        # 0부터 시작해서 2씩해서 20까지 출력하는 반복문
#num = 0
#while num < 21:         ## 증가
            #print(num)
            #num += 2
        # 20부터 시작해서 4씩 줄어들어서 0까지 출력하는 반복문
            #num2 = 20
            #while num2 >= 0:    ## 감소
                #print(num2)
                #num2 -= 4
            
#user_input = ""
#while True:
    #user_input = input("입력(종료시 '/q'): ")
    #if user_input.isdigit():
        #print(f"{user_input}원입니다.")
        #continue 
    #elif user_input == "/q":
        #break
    #print(user_input)
    
    # 안 녕 하 세 요 를 한글자씩 출력하는 반복문
#text = "안녕하세요"
#idx = 0

#while idx < len(text):
    #print(text[idx])
    #idx += 1
        
        # 1부터 20까지 홀수만 continue를 써서 출력하는 반복문
               
#num = 1 ## 증가
#while num < 20 :      
        #if (num % 2) == 0:
            #num += 1
        #print(num)
        #num += 1
        #continue
    
    # 구구단 2단 2x1 -> 2x9 출력하는 구구단 프로그램 만들기
#num = 2 # 2단
#i = 1 #숫자를 세기 시작 할 변수 생성
    
#while i <= 9: # i가 9가 될때까지 반복
        #print(num, "*", i, "=", num * i)
        #i += 1 # 다음 숫자로 넘어가기(없으면 무한루프)
#target = 2
#while True:
        #while True:
            #user_input = input("2~9 사이의 정수를 입력해 주세요.(/q입력시 종료):")
            
            #if user_input.isdigit() and (9 >= int(user_input) >= 2):
                #target = int(user_input)
                #break
            #elif user_input == "/q":
                #input("프로그램을 종료합니다.")
                #exit(0)
            #else:
                #input("정수로만 이루어져있지 않거나, 범위를 벗어났습니다.(Enter)")

        #num = 1

            #target = 2
            #num = 1
        #while num < 10 :
                #print(f"{target} X {num} - {target * num}")
                #num += 1
    # 다음을 while문을 이용해서 만들어보기
#num = 0
#while num < 5 :
        #print("*", end="")
        #num += 1
        
#num1 = 0
#while num1 < 5:
     #print("*", end="")
        #num2 += 1
        
            #num2 = 0
            #while num2 < 5:
                #print("*", end="")
                #num2 += 1
                #print()
                #num += 1
                
#print((("*" * 5) + "\n") * 5)
                
