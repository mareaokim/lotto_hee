#UP&DOWN게임

import random

#게임을 위한 숫자 생성

rn = random.randrange(1,101,1)
num = -1

t_cnt = 0  #시도횟수

print("1~100 숫자 재기&민기 게임을 시작합니다. !!!")


print("재기재기재기 민기민기민기")

while (rn != num):
    num = int(input("1~100 사이의 숫자를 입력하세요 : "))

    if (num > rn):
        
        print("재기!")
        
    elif (num < rn):

            print("민기!")

            t_cnt +=1


            print("-------------------------------------")


            print(t_cnt,"축하합니다. 철근과 밧줄 세트를 드립니다.")


            




            





