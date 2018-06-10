
#로또번호 생성기

import random  

num = int(input("로또 게임 수를 입력하시오 : ")) 

print("로또 자동 번호 입니다.")
print("----------------------------------------------------")

# 입력한 게임 수 만큼 반복
for x in range(1, num+1):
    lotto =[0,0,0,0,0,0]

    lotto[0] = random.randrange(1,46,1)

    lotto[1] =lotto[0]
    lotto[2] =lotto[0]
    lotto[3] =lotto[0]
    lotto[4] =lotto[0]
    lotto[5] =lotto[0] 


    # 중복 된 수가 발생되지 않도록 채번
    while (lotto[0] == lotto[1]):
        lotto[1] = random.randrange(1,46,1)

    while (lotto[0] == lotto[2] or lotto[1] == lotto[2]):
        lotto[2] = random.randrange(1,46,1)

    while (lotto[0] == lotto[3] or lotto[1] == lotto[3] or lotto[2] == lotto[3]):
        lotto[3] =random.randrange(1,46,1)

    while (lotto[0] == lotto[4] or lotto[1] ==lotto[4] or lotto[2] ==lotto[4] or lotto[3] ==lotto[4]):
        lotto[4] =random.randrange(1,46,1)

    while (lotto[0] == lotto[5] or lotto[1] ==lotto[5] or lotto[2] ==lotto[5] or lotto[3] == lotto[5] or lotto[4] == lotto[5]):
        lotto[5] =random.randrange(1,46,1)

        #결과를 정렬
        lotto.sort()

        #결과 출력
        print(lotto)


