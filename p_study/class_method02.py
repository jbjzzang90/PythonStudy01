# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : jeong
    Date : 2022.09.05
    """

    # 클래스 변수
    car_count = 0


    def __init__(self, company, details):
        self._comoany=company
        self._details=details
        Car.car_count +=1

    def __str__(self):
        return 'str : {} - {}'.format(self._comoany, self._details)             # print로 출력가능

    def __repr__(self):
        return 'repr : {} - {}'.format(self._comoany, self._details)            # __str__와 비슷
    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._comoany, self._details.get('price')))

# Self 의미 
car1 =Car('Ferrai',{'colir' : 'White','horsepower' : 400,'price' : 8000})
car2 =Car('Bmw',{'colir' : 'black','horsepower' : 270,'price' : 5000})
car3 =Car('Audi',{'colir' : 'Silver','horsepower' : 300,'price' : 6000})

# ID 값
print(id(car1))                                 # 4374560720
print(id(car2))                                 # 4374560432
print(id(car3))                                 # 4374560336

print(car1._comoany == car2._comoany)           # 값 비교
print(car1 is car2)                             # 인스턴스 비교

# dir & __dict__ 확인
print(dir(car1))                                # False 사용할 수 있는 내장함수를 전부 보여줌
print(dir(car2))                                # False

print()
print()

print(car1.__dict__)                            # car1.__dict__ 딕셔너리값 확인
print(car2.__dict__)


# Doctring

print('Car.__doc__ : ',Car.__doc__)             # 코멘트가 있다면 값을 확인할 수 있음.
print()


# 실행
car1.detail_info()                              
car2.detail_info()                              



# 비교
print(car1.__class__,car2.__class__)                                        # <class '__main__.Car'> <class '__main__.Car'>
print(id(car1.__class__),id(car2.__class__),id(car3.__class__))             # 4813148736 4813148736 4813148736 같은 class를 사용하기때매 id 값이 같음


# 에러
# Car.detail_info()



# 공유확인
print(car1.car_count)                                                        # 3
print(car2.car_count)                                                        # 3
print(car1.__dict__)                                                         # {'_comoany': 'Ferrai', '_details': {'colir': 'White', 'horsepower': 400, 'price': 8000}}                    
print(car2.__dict__)                                                         # {'_comoany': 'Bmw', '_details': {'colir': 'black', 'horsepower': 270, 'price': 5000}}
print(dir(car1))


# 접근 
print(car1.car_count)                                                        # 3
print(Car.car_count)                                                         # 3


del car2
# 삭제 확인
print(car1.car_count)                                                        # 2
print(Car.car_count)                                                         # 2


# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 동일한 이름으로 변수 생성 가능 인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스 변수)

