# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque )
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급
 

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9))                               # (11, 1)
print(divmod(*(100,9)))                             # (11, 1)
print(*(divmod(100,9)))                             # 11, 1


print()


x, y, *rest = range(10)
print(x, y, rest)                                   # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
x, y, *rest = range(2)
print(x, y, rest)                                   # 0 1 []
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)                                   # 1 2 [3, 4, 5]


print()
print()


# Mutable(가변) vs Immutable(불변)


l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))                                     # (15, 20, 25) 4300675072
print(m, id(m))                                     # [15, 20, 25] 4300983552

l = l * 2
m = m * 2

print(l, id(l))                                     # (15, 20, 25, 15, 20, 25) 4300301376
print(m, id(m))                                     # [15, 20, 25, 15, 20, 25] 4300983488

l *= 2
m *= 2

print(l, id(l))                                     # (15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25) 4300544256
print(m, id(m))                                     # [15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25] 4300983488

print()
print()

# sort vs sorted
# reverse(정렬 반대로), key=Len, key=str.Lower, key=func...

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lomon', 'strawberry', 'coconut']
print('sorted : ',sorted(f_list))                                                   # sorted :  ['apple', 'coconut', 'lomon', 'mango', 'orange', 'papaya', 'strawberry']
print('sorted : ',sorted(f_list, reverse=True))                                     # sorted :  ['strawberry', 'papaya', 'orange', 'mango', 'lomon', 'coconut', 'apple']
print('sorted : ',sorted(f_list, key=len))                                          # sorted :  ['apple', 'mango', 'lomon', 'orange', 'papaya', 'coconut', 'strawberry']
print('sorted : ',sorted(f_list, key=lambda x: x[-1]))                              # sorted :  ['papaya', 'orange', 'apple', 'lomon', 'mango', 'coconut', 'strawberry']
print('sorted : ',sorted(f_list, key=lambda x: x[-1], reverse=True))                # sorted :  ['strawberry', 'coconut', 'mango', 'lomon', 'orange', 'apple', 'papaya']
print('sorted : ',f_list)                                                           # sorted :  ['orange', 'apple', 'mango', 'papaya', 'lomon', 'strawberry', 'coconut']

# sort : 정렬 후 객체 직접 변경

# 반환 값 확인(None)
print('sort :', f_list.sort(), f_list)                                              # sort : None ['apple', 'coconut', 'lomon', 'mango', 'orange', 'papaya', 'strawberry']
print('sort :', f_list.sort(reverse=True), f_list)                                  # sort : None ['strawberry', 'papaya', 'orange', 'mango', 'lomon', 'coconut', 'apple']
print('sort :', f_list.sort(key=len), f_list)                                       # sort : None ['mango', 'lomon', 'apple', 'papaya', 'orange', 'coconut', 'strawberry']
print('sort :', f_list.sort(key=lambda x : x[-1]), f_list)                          # sort : None ['papaya', 'apple', 'orange', 'lomon', 'mango', 'coconut', 'strawberry']
print('sort :', f_list.sort(key=lambda x : x[-1], reverse=True), f_list)            # sort : None ['strawberry', 'coconut', 'mango', 'lomon', 'apple', 'orange', 'papaya']

# List vs array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)