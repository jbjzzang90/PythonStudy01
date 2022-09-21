# Specual Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스 (Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

# 기본형
print(int)                                  # <class 'int'>
print(float)                                # <class 'float'>


# 모든 속성 및 메소드 출력
print(dir(int))     
print(dir(float))


n = 10

print(n + 100)                              # 110
print(n.__add__(100))                       # 110
# print(n.__doc__) 코멘트
print(n.__bool__, bool(n))                  # <method-wrapper '__bool__' of int object at 0x1043c0210> True
print(n * 100, n.__mul__(100))              # 1000 1000

print()
print()

# 클래스 예제1
class Fruit : 
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price )
    
    def __add__(self, x):
        print('Called >> __add__')
        return self._price + x._price
    
    def __sub__(self, x):
        print('Called >> __sub__')
        return self._price - x._price
 
    def __le__(self, x):
        print('Called >> __le__')
        if self._price <= x._price :
            return True
        else : 
            return False

    def __ge__(self, x):
        print('Called >> __ge__')
        if self._price >= x._price :
            return True
        else : 
            return False



# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1 + s2)                  # 10500

# 일번적인 계산
#print(s1._price + s2._price)

# 매직메소드
print(s1 >= s2)                 # True
print(s1 <= s2)                 # False
print(s1 - s2)                  # 4500
print(s2 - s1)                  # -4500
print(s1)                       # Fruit Class Info : Orange , 7500
print(s2)                       # Fruit Class Info : Banana , 3000
print(dir(Fruit))                



