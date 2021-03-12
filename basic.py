
'''
loop
: 아래와 같이 3가지 방법이 있지만, 가독성을 고려해 선택
'''
# 방법1
sum = 0
for i in range(0, 10+1):
    sum += i

# 방법2
sum = sum(i for i in range(0, 10+1))

# 방법3
sum = sum(range(0, 10+1))

'''
generic programming
: generic이란 파라미터의 타입을 나중에 지정되게 해서 재활용성을 높이는 프로그래밍 스타
: python은 동적 타이핑 언어로서 제네릭이 필요하지 않다. 하지만 가독성을 위해 명시적으로 타입을 줄 수 있다.
'''
# 일반적인 사용
def are_equal(a, b):
    return a == b

are_equal(10, 10.0)

# 명시적 타입 표시
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def are_equal(a: T, b: U) -> bool:
    return a == b

are_equal(10, 10.0)

'''
배열 반복
'''
foo = ['A', 'B', 'C']
for f in foo:
    print(f)

'''
구조체
: 복합 자료형으로 C에서 큰 의미가 있었지만,
python에서는 구조체가 없고 클래스 조차 데이터 타입을 지정할 수 없어서 구조체와 같은 자료형을 정의하려면 Named Tuple을 사용해야 한다.
python 3.7부터는 dataclass 데코레이터를 지원하며 이를 활용해 class를 구조체 형태로 정의할 수 있다.
'''
# namedtuple
from collections import namedtuple

MyStruct = namedtuple("MyStruct", "field2 field2 field3")
m = MyStruct("foo", "bar", "baz")

# dataclass
from dataclasses import dataclass

@dataclass
class Product:
    weight: int = None
    price: float = None

apple = Product()
apple.price = 10

'''
클래스
: 실무에서는 거의 항상 쓰이지만, 코딩 테스트에서는 사실상 사용할 일이 많지 않다.
데코레이터를 사용하지 않아도 무방하지만, dataclass 데코레이션을 사용하면 자동으로 구현해주는 내부 함수들이 있다. (TODO)
'''
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area())

'''
* 참고: python 이름의 유래: 70년대 세계를 풍미한 영국의 코미디 그룹 몬티 파이썬 (Monty Python)의 이름에서 따옴

조금 더 있어보이는 파이썬 문법
- 인덴테이션 : 4 spaces가 PEP8 기본
- 네이밍 컨벤션: 스네이크 케이스
'''

# 타입 힌트
# - 동적 프로그래밍 언어로서 타입 명시는 불필요 하지만, 가독성을 위해 python 3.5부터 사용 가능
# - 오류가 발생하진 않으므로 타입 힌트와 변수 지정에 주의가 필요
a: str = "1"
b: int = 1

def fn(a: int) -> bool:
    return a = 0

# 리스트 컴프리헨션 - 기존 리스트를 기반으로 새로운 리스트를 만들어내는 기법
a = [n * 2 for n in range(1, 10+1) if n % 2 == 1]

# 딕셔너리 컴프리헨션
a = {key: value for key, value in original.items()}

# 제네레이터
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield

g = get_natural_number()
for _ in range(0, 100):
    print(next(g))

def generator():
    yield 1
    yield 'string'
    yield True

next(g)
next(g)
next(g)

# range() 함수는 대표적인 제네레이터 함수
list(range(5))
# [0, 1, 2, 3, 4]
range(5)
# range(0, 5)
type(range(5))
# <class 'range'>
for i in range(5):
    print(i, end='')
    # 0 1 2 3 4

# 100만개의 숫자를 생성해야한다면?
a = [n for n in range(1000000)]  # 생성한 값이 담겨있음
b = range(1000000)  # 생성 조건이 담겨있음

import sys

sys.getsizeof(a)
# 8697464
sys.getsizeof(b)
# 48 -> 조건만 가지고 있기 때문에 몇 개의 숫자를 만들어 내야 하는 조건이든 메모리 점유율은 동일

b[999]
# 999 -> 인덱스로 접근해도 바로 값이 생성되기 때문에 리스트와 거의 동일하게 사용할 수 있음

# enumerate: 여러가지 자료형을 인덱스를 포함한 enumerate 객체로 리턴
a = [1,2,3,2,45,2,5]
enumerate(a)
# <enumerate object at ...>
list(enumerate(a))
# [(0,1), (1,2), (2,3), (3,2), (4,45), (5,2), (6,5)]

# 나눗셈 연산자
5 / 3  # 1.6666...
5 // 3  # 1 = int(5 / 3)
5 % 3  # 2
divmod(5, 3)  # (1, 2)

# locals(): 로컬 스코프에 정의된 모든 변수 출력 가능! 디버깅에 큰 도움!
import pprint
pprint.pprint(locals())
