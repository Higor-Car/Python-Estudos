class contaBancaria:

    def __init__(self, nomeTitular,saldoConta):
        self.titular=nomeTitular
        self.saldo=saldoConta

    def exibir(self):
        print(f"Titular:{self.titular}")
        print(f"Saldo:{self.saldo:.2f}")

funcionario1= contaBancaria("Cauã",3500)
funcionario2= contaBancaria("Gabryel",3500)

funcionario1.exibir()
funcionario2.exibir()


