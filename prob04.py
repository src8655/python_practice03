# 문제4.
# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
import random

mins, maxs = 1, 9


# 정답리스트
answer_list = set()

# 문제만들기
number1 = random.randrange(maxs) + mins
number2 = random.randrange(maxs) + mins
answer = number1 * number2

# 문제
print('{0} x {1} = ?'.format(number1, number2))
print()

# 정답을 추가
answer_list.add(answer)

# 겹치지 않는 총 9개의 정답리스트를 만들때까지 반복
while len(answer_list) != 9:
    rand = random.randrange(maxs) + mins * random.randrange(maxs) + mins
    answer_list.add(rand)

# 섞기
answer_list = list(answer_list)
random.shuffle(answer_list)

# 정답리스트
cnt = 1
for a in answer_list:
    print(a, end='\t')
    if cnt == 3:
        print()
        cnt = 0
    cnt += 1
print()

# 입력받기
while True:
    number = input('answer: ')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('[정수를 입력해 주세요]')
print()

# 결과
if number == answer:
    print('정답')
else:
    print('오답')
