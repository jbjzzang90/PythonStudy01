# 함수형 프로그래밍
# 일급 함수 (일금 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 함수 객체

def factorial(n) :
    '''Factorial Function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A : 
    pass


print(factorial(5))                                         # 120
print(factorial.__doc__)                                    # Factorial Function -> n : int
print(type(factorial), type(A))                             # <class 'function'> <class 'type'>
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))    # {'__closure__', '__qualname__', '__annotations__', '__globals__', '__defaults__', '__call__', '__get__', '__code__', '__kwdefaults__', '__name__', '__builtins__'}
print(factorial.__name__)                                   # factorial
print(factorial.__code__)                                   # <code object factorial at 0x1023a3310, file "/Users/jeongbyeongnam/Desktop/PythonStudy002/PythonStudy01/p_study/frist_class.py", line 11>      



print()
print()

# 변수 할당
 
var_func = factorial


print(var_func)                                 # <function factorial at 0x1023f28c0>
print(var_func(10))                             # 3628800
print(list(map(var_func, range(1, 11))))        # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce

print(list(map(var_func, filter(lambda x :  x% 2, range(1,6)))))    # [1, 6, 120]
print([var_func(i)for i in range(1,6) if i % 2])                    # [1, 6, 120]


print()
print()

# reduce
from functools import reduce
from operator import add

print(reduce(add, range(1,11)))             # 55
print(sum(range(1,11)))                     # 55


# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x +t , range(1,11)))

print()
print()


# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str), callable(A), callable(var_func), callable(factorial), callable(3.14))


# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul, 5)      # 5 * ?

# 고정 추가
six = partial(five, 6)

print(five(10))                             # 50
print(six())                                # 30
print([five(i) for i in range(1,11)])       # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(list(map(five, range(1,11))))         # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]








