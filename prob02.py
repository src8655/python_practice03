# 문제2.
# range() 함수와 유사한 frange() 함수를 작성해 보세요. frange() 함수는 실수 리스트를 반환합니다.


def frange(val, base=None, step=None):
    if base is None:
        start = 0.0
        stop = val
        step = 0.1
    else:
        start = val
        stop = base
        if step is None:
            step = 0.1

    l = []
    while True:
        l.append(start)
        start += step

        # 음수도 허용
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
    return l


print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))
print(frange(3.0, 1.0, -0.5))
