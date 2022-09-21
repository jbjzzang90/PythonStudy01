# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리



class Car():
    """
    Car class
    Author : jeong
    Date : 2022.09.05
    Desctiption : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.2


    def __init__(self, company, details):
        self._comoany=company
        self._details=details

    def __str__(self):
        return 'str : {} - {}'.format(self._comoany, self._details)             # print로 출력가능

    def __repr__(self):
        return 'repr : {} - {}'.format(self._comoany, self._details)            # __str__와 비슷

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._comoany, self._details.get('price')))
    
    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {},price : {}'.format(self._comoany, self._details.get('price'))


    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {},price : {}'.format(self._comoany, self._details.get('price')*Car.price_per_raise)
    # Calss Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')
    # static method
    @staticmethod
    def is_bmw(inst) :
        if inst._comoany == 'Bmw':
            return 'OK! This cat is {}'.format(inst._comoany)
        return 'Sorry. This car is not Bmw'



# Self 의미 
car1 =Car('Ferrai',{'colir' : 'White','horsepower' : 400,'price' : 8000})
car2 =Car('Bmw',{'colir' : 'black','horsepower' : 270,'price' : 5000})


# 전체정보
car1.detail_info()                  # Current ID : 4308860400 Car Detail Info : Ferrai 8000
car2.detail_info()                  # Current ID : 4308860304 Car Detail Info : Bmw 5000

# 가격정보 (직접접근)
print(car1._details.get('price'))   # 8000
print(car1._details['price'])       # 8000


# 가격정보 (인상 전)
print(car1.get_price())         # Before Car Price -> company : Ferrai,price : 8000
print(car2.get_price())         # Before Car Price -> company : Bmw,price : 5000


# 가격 인상(클래스 메소드 사용)
Car.price_per_raise = 1.4

# 가격 인상(인상 후)
print(car1.get_price_culc())    # After Car Price -> company : Ferrai,price : 11200.0
print(car2.get_price_culc())    # After Car Price -> company : Bmw,price : 7000.0

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.9)

# 가격 인상(인상 후)
print(car1.get_price_culc())   # After Car Price -> company : Ferrai,price : 15200.0
print(car2.get_price_culc())   # After Car Price -> company : Bmw,price : 9500.0


# 인스턴스 호출(Static)
print(car1.is_bmw(car1))       # Sorry. This car is not Bmw
print(car2.is_bmw(car2))       # OK! This cat is Bmw
# 클래스 호출(Static)
print(Car.is_bmw(car1))        # Sorry. This car is not Bmw
print(Car.is_bmw(car2))        # OK! This cat is Bmw




