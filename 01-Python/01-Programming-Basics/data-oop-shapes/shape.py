# pylint: disable=too-few-public-methods missing-module-docstring

class Shape:
    """Representa uma forma geométrica com nome e cor"""
    def __init__(self, color, name):
        self.name = name
        self.color = color

    def say_name(self):
        """Retorna o nome da forma"""
        return f'My name is {self.name}.'

class Rectangle(Shape):
    """Representa uma forma do retangulo com nome, cor, largura e altura"""
    def __init__(self, color, name, width, height):
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        """Retorna o nome da forma"""
        return f'My name is {self.name} and I am a rectangle.'

    def area(self):
        """Retorna a area da forma"""
        area = self.width * self.height
        return area

    def perimeter(self):
        """Retorna o perimetro da forma"""
        perimeter = self.width * 2 + self.height * 2
        return perimeter

class Circle(Shape):
    """Representa uma forma do circulo com nome, cor e raio"""
    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        """Retorna o nome da forma"""
        return f'My name is {self.name} and I am a circle.'

    def area(self):
        """Retorna a area da forma"""
        area = 3.14159265358979323846 * (self.radius ** 2)
        return area

    def perimeter(self):
        """Retorna o perimetro da forma"""
        perim = 2 * 3.1415926535897932384 * self.radius
        return perim
