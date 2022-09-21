# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque )
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급
 
# 지능형 리스트(Comprehending Lists)


chars = '@#$%^%^&'
code_list1 = []

for s in chars :
    # 유니코드 리스트 
    code_list1.append(ord(s))
print(code_list1)                       # [64, 35, 36, 37, 94, 37, 94, 38] 유니코드

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
print(code_list2)                       # [64, 35, 36, 37, 94, 37, 94, 38] 유니코드

# Comprehending Lists + Map , Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))


print(code_list1)                       # [64, 35, 36, 37, 94, 37, 94, 38]                      
print(code_list2)                       # [64, 35, 36, 37, 94, 37, 94, 38]
print(code_list3)                       # [64, 94, 94]
print(code_list4)                       # [64, 94, 94]
print([chr(s) for s in code_list1])     # ['@', '#', '$', '%', '^', '%', '^', '&']
print([chr(s) for s in code_list2])     # ['@', '#', '$', '%', '^', '%', '^', '&']
print([chr(s) for s in code_list3])     # ['@', '^', '^']
print([chr(s) for s in code_list4])     # ['@', '^', '^']

print()
print()

# Generator
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(tuple_g)                          # <generator object <genexpr> at 0x10064a2d0>
print(next(tuple_g))                    # 64

print(array_g)                          # array('I', [64, 35, 36, 37, 94, 37, 94, 38])
print(array_g.tolist())                 # [64, 35, 36, 37, 94, 37, 94, 38]

# 제네레이터 예제
print(('%s' % c+ str(n) for c in ['A', 'B', 'C', 'D']for n in range(1,21)))         # <generator object <genexpr> at 0x1031b22d0>

for s in('%s' % c+ str(n) for c in ['A', 'B', 'C', 'D']for n in range(1,21)) :
    print(s)                            # A1, A2 ......... D20


print()
print()
# 리스트 주의
marks1 = [['~'] * 3 for _ in range(4)]              
marks2 = [['~'] * 3 ] * 4                           # 같은 주소를 4개 복사가되어서 변경시 문제가 생길 수 있음.


print(marks1)                                       # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print(marks2)                                       # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]

print()

# 수정
marks1[0][1] = 'X'
print(marks1)                                       # [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]

marks2[0][1] = 'X'
print(marks2)                                       # [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]