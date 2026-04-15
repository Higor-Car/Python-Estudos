class retangulo:

    def __init__(self, receberLargura,receberComprimento):
        self.largura=receberLargura
        self.comprimento=receberComprimento

    def area(self):
        areaTotal = self.comprimento*self.largura
        return(areaTotal)

    def perimetro(self):
        (perimetroTotal) = (self.comprimento*2)+(self.largura*2)
        return(perimetroTotal)

    def exibir(self):
        print(f"Perimetro:{self.perimetro():.2f}")
        print(f"Area:{self.area():.2f}")

retangulo1 = retangulo(10,20)

retangulo1.exibir()