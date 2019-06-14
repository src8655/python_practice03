# 문제1.
# 다음 세 개의 리스트가 있을 때,
# subs = [‘I’, ‘You’]
# verbs = [‘Play’, ‘Love’]
# objs = [‘Hockey’, ‘Football’]
#
# 3형식 문장을 모두 출력해 보세요. 반드시 comprehension을 사용합니다.

subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

# 그냥 함수
for i in subs:
    for j in verbs:
        for k in objs:
            print(i, j, k)

# comprehension 사용했을 때
print([[[[i, j, k] for k in objs] for j in verbs] for i in subs])