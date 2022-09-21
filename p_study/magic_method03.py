# Specual Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스 (Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드


# 객체 - > 파이썬의 데이터를 추상화
# 모든 객체 -> id , type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from cgi import print_arguments
from math import sqrt
from unicodedata import name

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)          # 3.8078865529319543


# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point','x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3)
# print(pt4)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)

print(l_leng2)          # 3.8078865529319543


# 네임드 튜블 선언 방법
Point1 = namedtuple('Point',['x','y'])
Point2 = namedtuple('Point','x,y')
Point3 = namedtuple('Point','x y')
Point4 = namedtuple('Point','x y x class', rename=True) # Defalut = False

# 출력
print(Point1,Point2,Point3,Point4)  # <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'>

# Dict to Unpacking
temp_dict = {'x':75, 'y':55}



# 객체 생성
p1 =  Point1(x=10, y=35)
p2 =  Point2(20, 40)
p3 =  Point3(45, y=20)
p4 =  Point4(10,20,30,40)
p5 =  Point2(**temp_dict)


print()

print(p1)               # Point(x=10, y=35)
print(p2)               # Point(x=20, y=40)
print(p3)               # Point(x=45, y=20)
# rname 테스트
print(p4)               # Point(x=10, y=20, _2=30, _3=40)
print(p5)               # Point(x=75, y=55)


# 사용
print(p1[0]+p2[1])      # 50
print(p1.x + p2.y)      # 50

# unpacking
x, y = p3

print(x, y)             # 45 20

# 네임드 튜플 메소드
temp = [52, 38]

# _make : 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)               # Point(x=52, y=38)



# _fields : 필드 네임 확인
print(p1._fields,p2._fields,p3._fields,p4._fields) # ('x', 'y') ('x', 'y') ('x', 'y') ('x', 'y')

# _asdict() : OrderedDict 반환
print(p1._asdict)                                  # <bound method Point._asdict of Point(x=10, y=35)>
print(p2._asdict)                                  # <bound method Point._asdict of Point(x=20, y=40)>


# 실 사용 실습
# 반20명, 4개의 반(A,B,C,D)

Classes = namedtuple('Classes',['rank', 'number'])


# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)          # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
print(ranks)            # ['A', 'B', 'C', 'D']

# List Compregension
studebts = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(studebts))    # 80
print(studebts)         # [Classes(rank='A', number='1') ...... Classes(rank='D', number='20') 

# 추천
studebts2 = [Classes(rank, number)
                for rank in 'A B C D'.split()
                    for number in [str(n)
                        for n in range(1,21)]]


print(len(studebts2))    # 80
print(studebts2)         # [Classes(rank='A', number='1') ...... Classes(rank='D', number='20') 