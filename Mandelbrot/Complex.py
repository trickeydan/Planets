
class Complex():

    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self,complex):
        return Complex(self.real + complex.real,self.imaginary + complex.imaginary)

    def __str__(self):
        return str(self.real) + " + " + str(self.imaginary) + "i"

    def squared(self):
        real = self.real **2 - self.imaginary ** 2
        imaginary = 2 * self.real * self.imaginary
        return Complex(real,imaginary)

    def modulus(self):
        pythag =  self.real **2 + self.imaginary ** 2
        return pythag ** 0.5
