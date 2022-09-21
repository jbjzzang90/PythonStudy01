# 시퀀스형 
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복 허용 X , Set -> 중복 허용 X
# Dict 및 Set 심화

# immutables Dict

# 읽기전용 딕셔너리 만들때 사용 (절대 변경x)
from types import MappingProxyType

# 수정가능
d = {'key1' : 'value1'}


# Read Only 수정불가
d_frozen = MappingProxyType(d)

print(d,id(d))                              # {'key1': 'value1'} 4371284288
print(d_frozen,id(d_frozen))                # {'key1': 'value1'} 4371414416

# 수정 불가
# d_frozen['key2'] = 'value2' Error

# 수정 가능
d['key2'] = 'value2'
print(d)                                    # {'key1': 'value1', 'key2': 'value2'}

print()
print()


s1 = {'Apple', 'Orange','Apple', 'Orange','Kiwi'}
s2 = set(['Apple', 'Orange','Apple', 'Orange','Kiwi'])
s3 = {3}
s4 = set() # Not {}
s5 = frozenset({'Apple', 'Orange','Apple', 'Orange','Kiwi'})

s1.add('Melon')
print(s1)                                   # {'Apple', 'Kiwi', 'Melon', 'Orange'}

# 추가 불가
# s5.add('Melon')

print(s1, type(s1))                         # {'Apple', 'Kiwi', 'Melon', 'Orange'} <class 'set'>
print(s2, type(s2))                         # {'Apple', 'Kiwi', 'Orange'} <class 'set'>
print(s3, type(s3))                         # {3} <class 'set'>
print(s4, type(s4))                         # set() <class 'set'>
print(s5, type(s5))                         # frozenset({'Apple', 'Kiwi', 'Orange'}) <class 'frozenset'>


# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis

print('----'*4)
print(dis('{10}'))
print('----'*4)
print(dis('set([10])'))


# 지능형 집합 (Compreheading Set)
print('----'*4)

from unicodedata import name

print({name(chr(i), '')for i in range(0, 255)})

