from abc import ABC, abstractmethod
import math

class Forma(ABC):
    def __init__(self):
        self.area = 0  # Atributo para armazenar a área

    @abstractmethod
    def calcular_area(self):
        """Método abstrato para calcular a área. Deve ser implementado pelas subclasses."""
        pass

    def mostrar_area(self):
        """Método concreto que exibe a área calculada, especificando a forma."""
        print(f"A área do {self.__class__.__name__.lower()} é: {self.area}")

class Quadrado(Forma):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.calcular_area()  # Calcula e armazena a área

    def calcular_area(self):
        """Implementação do cálculo da área para um quadrado."""
        self.area = self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio
        self.calcular_area()  # Calcula e armazena a área

    def calcular_area(self):
        """Implementação do cálculo da área para um círculo."""
        self.area = math.pi * (self.raio ** 2)

class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
        self.calcular_area()  # Calcula e armazena a área

    def calcular_area(self):
        """Implementação do cálculo da área para um retângulo."""
        self.area = self.base * self.altura

class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
        self.calcular_area()  # Calcula e armazena a área

    def calcular_area(self):
        """Implementação do cálculo da área para um triângulo."""
        self.area = (self.base * self.altura) / 2

# Exemplo de uso
quadrado = Quadrado(5)
circulo = Circulo(12)
retangulo = Retangulo(5, 3)
triangulo = Triangulo(4, 6)

quadrado.mostrar_area()  # Saída: A área do quadrado é: 25
circulo.mostrar_area()    # Saída: A área do circulo é: 452.3893421169302
retangulo.mostrar_area()   # Saída: A área do retângulo é: 15
triangulo.mostrar_area()   # Saída: A área do triângulo é: 12.0
