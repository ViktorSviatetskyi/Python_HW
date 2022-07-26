"""
Реализовать иерархию классов геометрических фигур.
Для этого требуется:
- реализовать абстрактный класс, который унаследуют все дочерние классы;
- все классы фигур должны реализовать методы вычисления периметра, площади;
- требуется создать классы для прямоугольника, треугольника, круга, трапеции;
- должны быть определены оба строковых представления для каждой фигуры
(repr, str);
- len для инстанса каждой фигуры должен возвращать периметр;
- определить арифметические операции сложения и вычитания для объектов фигур.
В результате сложения должна получаться суммарная величина периметра,
в случае вычитания - разница периметров фигур.
- фигуры можно сравнивать друг с другом. Например square > triangle.
Для сравнения нужно взять площади.
- классы должны позволять менять основные параметры фигур, при этом требуется
реализовать контроль данных. Если данные не валидны - выбросить исключение
ValueError с сообщением "Data not valid: {new_data}"
(Вместо {new_data} нужно показать какие конкретно данные не валидны).
"""

from abc import ABC, abstractmethod
import math


class GeometricFigure(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calc_perimeter(self):
        pass

    @abstractmethod
    def calc_area(self):
        pass


class Rectangle(GeometricFigure):

    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        if not isinstance(a, float):
            raise ValueError(f'Data not valid: "{a}". Not float')
        if a < 0:
            raise ValueError(f'Data not valid: "{a}". Side must be a positive number')
        else:
            self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        if not isinstance(b, float):
            raise ValueError(f'Data not valid: "{b}". Not float')
        if b < 0:
            raise ValueError(f'Data not valid: "{b}". Side must be a positive number')
        else:
            self._b = b

    def calc_perimeter(self):
        return 2 * (self._a + self._b)

    def calc_area(self):
        return self._a * self._b

    def __str__(self):
        return f'rectangle with sides {self._a} and {self._b}'

    def __repr__(self):
        return f'<Rectangle( {self._a}, {self._b})>'

    def __eq__(self, other):
        return self.calc_area() == other.calc_area()

    def __gt__(self, other):
        return self.calc_area() > other.calc_area()

    def __lt__(self, other):
        return self.calc_area() < other.calc_area()

    def __add__(self, other):
        return self.calc_perimeter() + other.calc_perimeter()

    def __sub__(self, other):
        return self.calc_perimeter() - other.calc_perimeter()


class Triangle(GeometricFigure):

    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        if not isinstance(a, float):
            raise ValueError(f'Data not valid: "{a}". Not float')
        if a < 0:
            raise ValueError(f'Data not valid: "{a}". Side must be a positive number')
        else:
            self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        if not isinstance(b, float):
            raise ValueError(f'Data not valid: "{b}". Not float')
        if b < 0:
            raise ValueError(f'Data not valid: "{b}". Side must be a positive number')
        else:
            self._b = b

    @property
    def c(self):
        return self._side_c

    @c.setter
    def c(self, side_c):
        if not isinstance(side_c, float):
            raise ValueError(f'Data not valid: "{side_c}". Not float')
        if side_c < 0:
            raise ValueError(f'Data not valid: "{side_c}". Side must be a positive number')
        if (side_c > self._a + self._b) or (side_c < abs(self._a - self._b)):
            raise ValueError(f'Data not valid: "{side_c}". Side C must be smaller then  {self._a + self._b} '
                             f'and bigger then {abs(self._a - self._b)}')
        else:
            self._side_c = side_c

    def calc_perimeter(self):
        return self._a + self._b + self._c

    def calc_area(self):
        """Heron's formula"""
        s = (self._a + self._b + self._c) / 2
        return round(math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c)), 2)

    def __str__(self):
        return f'triangle with sides {self._a}, {self._b} and {self._c}'

    def __repr__(self):
        return f'<Triangle({self._a}, {self._b} ,{self._c})>'

    def __eq__(self, other):
        return self.calc_area() == other.calc_area()

    def __gt__(self, other):
        return self.calc_area() > other.calc_area()

    def __lt__(self, other):
        return self.calc_area() < other.calc_area()

    def __add__(self, other):
        return self.calc_perimeter() + other.calc_perimeter()

    def __sub__(self, other):
        return self.calc_perimeter() - other.calc_perimeter()


class Circle(GeometricFigure):

    def __init__(self, radius: float):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if not isinstance(radius, float):
            raise ValueError(f'Data not valid: "{radius}". Not float')
        if radius < 0:
            raise ValueError(f'Data not valid: "{radius}". Side must be a positive number')
        else:
            self._radius = radius

    def calc_perimeter(self):
        return round(2 * self.radius * math.pi, 2)

    def calc_area(self):
        return round(self.radius ** 2 * math.pi, 2)

    def __str__(self):
        return f'circle with radius {self.radius}'

    def __repr__(self):
        return f'<Circle {self.radius}>'

    def __eq__(self, other):
        return self.calc_area() == other.calc_area()

    def __gt__(self, other):
        return self.calc_area() > other.calc_area()

    def __lt__(self, other):
        return self.calc_area() < other.calc_area()

    def __add__(self, other):
        return self.calc_perimeter() + other.calc_perimeter()

    def __sub__(self, other):
        return self.calc_perimeter() - other.calc_perimeter()


class Trapeze(GeometricFigure):

    def __init__(self, a: float, b: float, c: float, d: float):
        """
        :param a: float, basis of the trapezoid
        :param b: float, basis of the trapezoid
        :param c: float, trapezoidal side
        :param d: float, trapezoidal side
        """
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        if not isinstance(a, float):
            raise ValueError(f'Data not valid: "{a}". Not float')
        if a < 0:
            raise ValueError(f'Data not valid: "{a}". Side must be a positive number')
        else:
            self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        if not isinstance(b, float):
            raise ValueError(f'Data not valid: "{b}". Not float')
        if b < 0:
            raise ValueError(f'Data not valid: "{b}". Side must be a positive number')
        else:
            self._b = b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        if not isinstance(c, float):
            raise ValueError(f'Data not valid: "{c}". Not float')
        if c < 0:
            raise ValueError(f'Data not valid: "{c}". Side must be a positive number')
        else:
            self._c = c

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, d):
        if not isinstance(d, float):
            raise ValueError(f'Data not valid: "{d}". Not float')
        if d < 0:
            raise ValueError(f'Data not valid: "{d}". Side must be a positive number')
        if d > self.a + self.b + self.c:
            raise ValueError(f'Data not valid: "{d}". Side D must be smaller then  '
                             f'{self.a + self.b + self.c} ')
        else:
            self._d = d

    def calc_perimeter(self):
        return self.a + self.b + self.c + self.d

    def calc_area(self):
        """https://uk.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BF%D0%B5%D1%86%D1%96%D1%8F
        """
        return round(math.sqrt(
            (-1 * self.a + self.b + self.c + self.d) *
            (self.a - self.b + self.c + self.d) *
            (self.a - self.b + self.c - self.d) *
            (self.a - self.b - self.c + self.d)
        ) * ((self.a - self.b)/(self.b - self.a)) * 0.25, 2)

    def __str__(self):
        return f'trapeze with sides {self.a}, {self.b}, {self.c} and {self.d}'

    def __repr__(self):
        return f'<Trapeze( {self.a}, {self.b}, {self.c}, {self.d})>'

    def __eq__(self, other):
        return self.calc_area() == other.calc_area()

    def __gt__(self, other):
        return self.calc_area() > other.calc_area()

    def __lt__(self, other):
        return self.calc_area() < other.calc_area()

    def __add__(self, other):
        return self.calc_perimeter() + other.calc_perimeter()

    def __sub__(self, other):
        return self.calc_perimeter() - other.calc_perimeter()


rect1 = Rectangle(6.0, 7.0)
rect2 = Rectangle(3.0, 4.0)
print(rect1)
print(repr(rect1))
print(f'{rect1} perimeter = {rect1.calc_perimeter()}')
print(f'{rect1} area = {rect1.calc_area()}')

print(rect2)
print(repr(rect2))
print(f'{rect2} perimeter = {rect2.calc_perimeter()}')
print(f'{rect2} area = {rect2.calc_area()}')

print(f'Is {rect1} equal {rect2}? - {rect1 == rect2}')
print(f'Is {rect1} bigger then {rect2}? - {rect1 > rect2}')
print(f'Is {rect1} smaller then {rect2}? - {rect1 < rect2}')

print(f'Sum of perimeters {rect1} and {rect2} = {rect1 + rect2}')
print(f'Diff of perimeters {rect1} and {rect2} = {abs(rect1 - rect2)}')

print('\n\n\n')

triangle1 = Triangle(6.0, 9.0, 8.0)
triangle2 = Triangle(3.0, 4.0, 5.0)
print(triangle1)
print(repr(triangle1))
print(f'{triangle1} perimeter = {triangle1.calc_perimeter()}')
print(f'{triangle1} area = {triangle1.calc_area()}')

print(triangle2)
print(repr(triangle2))
print(f'{triangle2} perimeter = {triangle2.calc_perimeter()}')
print(f'{triangle2} area = {triangle2.calc_area()}')

print(f'Is {rect1} equal {triangle1}? - {rect1 == triangle1}')
print(f'Is {rect2} bigger then {triangle2}? - {rect2 > triangle2}')
print(f'Is {rect1} smaller then {triangle2}? - {rect1 < triangle2}')

print(f'Sum of perimeters {rect1} and {triangle1} = {rect1 + triangle1}')
print(f'Diff of perimeters {rect1} and {triangle2} = {abs(rect1 - triangle2)}')

print('\n\n\n')

circle1 = Circle(9.0)
circle2 = Circle(12.5)
print(circle1)
print(repr(circle1))
print(f'{circle1} perimeter = {circle1.calc_perimeter()}')
print(f'{circle1} area = {circle1.calc_area()}')

print(circle2)
print(repr(circle2))
print(f'{circle2} perimeter = {circle2.calc_perimeter()}')
print(f'{circle2} area = {circle2.calc_area()}')

print(f'Is {circle1} equal {triangle1}? - {circle1 == triangle1}')
print(f'Is {rect2} bigger then {circle1}? - {rect2 > circle1}')
print(f'Is {rect1} smaller then {circle2}? - {rect1 < circle2}')

print(f'Sum of perimeters {circle2} and {triangle1} = {circle2 + triangle1}')
print(f'Diff of perimeters {triangle1} and {circle1} = {abs(triangle1 - circle1)}')

print('\n\n\n')

trapeze1 = Trapeze(6.0, 12.0, 8.0, 9.0)
trapeze2 = Trapeze(3.0, 11.0, 5.0, 5.0)
print(trapeze1)
print(repr(trapeze1))
print(f'{trapeze1} perimeter = {trapeze1.calc_perimeter()}')
print(f'{trapeze1} area = {trapeze1.calc_area()}')

print(trapeze2)
print(repr(trapeze2))
print(f'{trapeze2} perimeter = {trapeze2.calc_perimeter()}')
print(f'{trapeze2} area = {trapeze2.calc_area()}')

print(f'Is {rect1} equal {trapeze2}? - {rect1 == trapeze2}')
print(f'Is {trapeze2} bigger then {triangle2}? - {trapeze2 > triangle2}')
print(f'Is {trapeze1} smaller then {rect2}? - {trapeze1 < rect2}')

print(f'Sum of perimeters {rect1} and {trapeze2} = {rect1 + trapeze2}')
print(f'Diff of perimeters {trapeze1} and {triangle2} = {abs(trapeze1 - triangle2)}')
