class Produto:
    def __init__(self,nome:str,preco:float,categoria:str):
        self.nome= nome
        self.preco= preco
        self.categoria=categoria

    def detalhes(self):
        print('='*40)
        print(f'Nome do produto: {self.nome}')
        print(f'Preço: R$ {self.preco:.2f}')
        print(f'Categoria: {self.categoria}')
        print('='*40)
        
