
#아래는 파이썬 세트를 사용하여 로또 복권 6개 번호와 보너스 번호를 100장 발행하여 세트에 저장하는 코드입니다.

import random

# 두 세트 생성
set1 = {1, 2, 3, 4, 5}
set2 = {3, 2, 1, 6, 7}

# 두 세트가 동일한지 확인 (모든 요소가 같은지)
#  set1 == set2 두 세트의 요소가 모두 같은지를 확인하며, 모든 요소가 같으면 True를 반환합니다.
print("set1과 set2가 동일한지:", set1 == set2)
# set1.intersection(set2)를 사용하여 두 세트의 교집합을 구하고, 그 교집합의 길이를 확인합니다. 교집합의 길이가 3인 경우에는 두 세트가 동일한 요소를 3개 가지고 있다는 것을 의미합니다.
print(len(set1.intersection(set2))==3) 




# 로또 복권 번호 생성 함수. 복권 1장 발행
def generate_lotto_numbers():
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))
    #     # range(1, 46)은 1부터 45까지의 숫자를 생성합니다.
# list(range(1, 46))은 이 숫자들을 리스트로 변환합니다.
# 따라서 numbers 리스트는 [1, 2, 3, ..., 45]의 형태가 됩니다.
    
    # 무작위로 숫자 6개 선택하여 세트로 변환 (중복 없음) 1부터 45까지의 숫자 중에서 중복되지 않게 6개의 숫자를 선택하여 로또 번호를 생성
    lotto_numbers = set(random.sample(numbers, 6)) 
    
    # 무작위로 숫자 1개 선택하여 보너스 번호 생성
    bonus_number = random.choice(numbers)
    
    return lotto_numbers, bonus_number



# 로또 복권 번호와 보너스 번호를 받아서 당첨 여부를 확인
# 로또 번호와 보너스 번호가 당첨 번호와 일치하는지를 확인하여 당첨 등수를 출력합니다.
def check_winner(lotto_numbers, lotto_bonus_number,winning_numbers,winning_bonus_number,idx):
    if lotto_numbers == winning_numbers and lotto_bonus_number == winning_bonus_number:
        print(f"{idx}번째 로또 복권: 1등 당첨!")
    elif lotto_numbers == winning_numbers:
        print(f"{idx}번째 로또 복권: 2등 당첨! (보너스 번호 불일치)")
    elif lotto_bonus_number == winning_bonus_number:
        print(f"{idx}번째 로또 복권: 3등 당첨! (5개 일치 + 보너스 번호 일치)")
    elif len(lotto_numbers.intersection(winning_numbers)) == 5:
        print(f"{idx}번째 로또 복권: 4등 당첨! (5개 일치)")
    elif len(lotto_numbers.intersection(winning_numbers)) == 4:
        print(f"{idx}번째 로또 복권: 5등 당첨! (4개 일치)")
    else:
        print(f"{idx}번째 로또 복권: 꽝")

# 당첨 번호 생성
# generate_lotto_numbers() 함수를 호출하여 로또 당첨 번호 (winning_numbers)와 보너스 번호 (winning_bonus_number)를 생성
# 당첨 번호 생성  100장의 로또 번호를 생성/각 로또 번호와 보너스 번호는 튜플로 구성되고, 이를 리스트에 저장합
winning_numbers, winning_bonus_number = generate_lotto_numbers()
print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number)


lotto_list=[] #튜플 리스트



# 100장의 로또 번호 생성하여 당첨 여부 판별
# for 루프는 1부터 100까지 100번 반복됩니다 (idx는 1부터 100까지).
# 각 반복마다 generate_lotto_numbers() 함수를 호출하여 로또 번호 (lotto_numbers)와 보너스 번호 (lotto_bonus_number)를 생성

for idx in range(1, 101): #생성 #1~100까지 반복
    lotto_numbers, lotto_bonus_number = generate_lotto_numbers() #복권 한장 발행할때마다(반복때마다 generate_lotto_numbers() 함수를 호출하여 로또 번호 (lotto_numbers)와 보너스 번호 (lotto_bonus_number)를 생성
    lotto_list.append((lotto_numbers,lotto_bonus_number))#생성된 로또 번호와 보너스 번호를 튜플로 묶어 lotto_list에 추가
    ##(복권번호, 보너스번호) 튜플로 저장
    ##[(0,0),(0,0),(,)]등으로 100장 복권 저장 append할때마다 튜플로 들어감

# 100장의 복권 가져와(꺼내서) 당첨 번호와 비교
# for idx in range(1, 101) in enumerate(lotto_list, 1): 
#//range(1, 101)은 숫자의 리스트
# enumerate(lotto_list, 1)은 리스트의 항목에 번호를 붙여줌 둘을 동시에 사용할 수 없음

# enumerate() 함수를 사용하여 1부터 100까지의 인덱스와 100장의 로또 번호를 순회하며 당첨 여부를 확인합니다.
for idx, (lotto_numbers, lotto_bonus_number) in enumerate(lotto_list, 1): #꺼냄(출력) 인덱스 시작값을 1로 지정하여 튜플의 인덱스는 1부터 순서대로 부여됨/enumerate(lotto_list, 1)는 리스트 항목에 번호를 붙여주는데, 여기서 인덱스는 1부터 시작합니다.
    # Check_winner(lotto_numbers, lotto_bonus_number, )
    #print(f'Ticket.{idx}, 번호 : {lotto_numbers}, 보너스번호 : {lotto_bonus_number}')
    # check_winner() 함수를 호출하여 각 로또 번호와 보너스 번호가 당첨 번호와 일치하는지 확인하고, 당첨 등수를 출력합니다.
    check_winner(lotto_numbers, lotto_bonus_number,winning_numbers,winning_bonus_number,idx)
    
    # 로또 번호와 보너스 번호가 당첨 번호와 일치하는지 확인
    # if lotto_numbers == winning_numbers and lotto_bonus_number == winning_bonus_number:
    #     print(f"{idx}번째 로또 복권: 1등 당첨!")
    # elif lotto_numbers == winning_numbers:
    #     print(f"{idx}번째 로또 복권: 2등 당첨! (보너스 번호 불일치)")
    # elif lotto_bonus_number == winning_bonus_number:
    #     print(f"{idx}번째 로또 복권: 3등 당첨! (5개 일치 + 보너스 번호 일치)")
    # elif len(lotto_numbers.intersection(winning_numbers)) == 5:
    #     print(f"{idx}번째 로또 복권: 4등 당첨! (5개 일치)")
    # elif len(lotto_numbers.intersection(winning_numbers)) == 4:
    #     print(f"{idx}번째 로또 복권: 5등 당첨! (4개 일치)")
    # else:
    #     print(f"{idx}번째 로또 복권: 꽝")


    # 로또 번호와 보너스 번호가 당첨 번호와 일치하는지 확인
    # 1.당첨 번호
    # 2. 100장 복권 발행할때 당첨 확인절차

