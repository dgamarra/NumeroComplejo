class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # Suma de números complejos: (a + bi) + (c + di) = (a + c) + (b + d)i
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        # Resta de números complejos: (a + bi) - (c + di) = (a - c) + (b - d)i
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        # Multiplicación de números complejos: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        # División de números complejos: (a + bi) / (c + di) = [(ac + bd) + (bc - ad)i] / (c^2 + d^2)
        denominator = other.real**2 + other.imag**2
        if denominator == 0:
            raise ValueError("Cannot divide by zero complex number")
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)

    def __str__(self):
        # Representación en cadena del número complejo
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

# Ejemplo de uso:
c1 = Complex(2, 3)
c2 = Complex(1, 4)

print(f"Suma: {c1 + c2}")
print(f"Resta: {c1 - c2}")
print(f"Multiplicación: {c1 * c2}")
print(f"División: {c1 / c2}")
