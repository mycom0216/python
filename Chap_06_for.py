#for i in range(5): #슬라이싱, range = 시작값,끝값,증가폭
    #print(i)             
#print(list(range(10)))               
#for i in range(2,5): 
    #print(i)
    
#print(list(range(2,5)))

#print(list(range(0,5,2)))


                
        
     
    
        
#a = 9 #별찍기
#for i in range(a):
    #print("" * (a - (i+1)), end="")
    #print('*' * (i+1))
            
#output = "" #시작
#for i in range(1,10):
                #for j in range(0,i):
                    #output += "*"
                    #output += "\n"
                    #print(output) #끝
                    
                    #output = ""
                    #for i in range(1,15):
                        #for j in range(14,i,-1):
                            #output += ''
                            #for  j in range(0,2,* i -1):
                                #output += '*'
                                #output += '\n'
                                #print(output)

#for i in range(5):
    #print(i)
    
    #output = ""
#for i in range(5,10):
        #for j in range(14,i,-1):
            #output += ''
            #output += "*"
            #output += "\n"
            #print(output)

#for i in range(10):
    #print("안녕하세요")
    
    #13인의아해가도로로질주하오
    #(길은막다른골목이적당하오)
    
    #제1의아해가무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    #제1의아해도무섭다고그리오.
    
#print("13인의아해가도로로질주하오.\n(길은막다른골목이적당하오)\n\n제1의아해가무섭다고그리오.")

#for i in range(2,14):
    #print(f"제[i]의아해도무섭다고그리오.")
    
#target = 2
#for i in range(1,10):
    #print(f"{target} X {target * i} = i")
    
#for i in range(3):
        #for j in range(3):
            #print("안녕하세요")
            
#li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#target = 4
#idx = 0
#switch = 1

#for i in range(3):
    #if switch == 0:
        #break
    #for j in range(3):
        #if li[i][j] == target:
            #print(f"타겟의 전체에서의 인덱스는 {idx}입니다.")
            #switch = 0 
            #break
        #print("타겟이 아닙니다")
        #idx += 1 
        
#size = 2
#for i in range(size):
    #for j in range(size):
        #print("*",end="")
    #print()
        

#size = 6 #삼각형
#for i in range(size):
    #for j in range(i+1):
           #print('*',end="")
    #print()
# print("------------------------------")
#size = 5    #역삼각형
#for i in range(size):
        #for j in range(size-i):
            #print('*', end="")
        #print()
        
size =5

for i in range(size):
    for j in range(size - i - 1): ## 띄어쓰기 간격 중요
        print(" ", end="") ##"" >> 띄어쓰기 매우중요함(띄어쓰기에따라서 위치바뀜)
    for k in range(i + 1): ## 여기도 + >> 사이 띄어쓰기
        print("*", end="") ## 띄어쓰기
    print()

    
    
        
        
        
        
        
        
    
   