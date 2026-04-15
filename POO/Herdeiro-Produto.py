class Produto:

    def __init__(self,nome,preco,categoria):
        self.nome=nome
        self.preco=preco
        self.categoria=categoria

    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço original: {self.preco}")
        print(f"Preço final: {self.precoFinal}")

class ProdutoComDesconto(Produto):

    def __init__(self,nome,preco,desconto):
        self.precoFinal = preco - (preco*(desconto/100))
        self.desconto=desconto

        super().__init__(nome,preco,"Promoção")

produto1 = ProdutoComDesconto("Macarrão",200,10)
produto1.exibirDados()
