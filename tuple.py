my_tuple = (1,2,3,4)

print("원본 튜블:", my_tuple )

try:
    my_tuple[0] = 10
except TypeError as e:
    print("튜플 수정시도 결과:", e)