"""Atributos:

produtos (lista de instâncias Produto), quantidade (dicionário que mapeia

cada produto à sua quantidade), cliente (str), status (str – valores possíveis:
"Novo", "Processando", "Enviado").

Métodos:

-       
total_pedido(): Calcula o total do pedido
aplicando map e reduce nos produtos e suas

quantidades.


-       
detalhes_pedido(): Retorna os detalhes do pedido
(produtos, quantidade, cliente, status).
"""
from Produto import Produto

class Pedido():
    def __init__(self,quantidade,cliente:str,status:str):
        self.produtos = Produto 
        self.quantidade=quantidade
        self.cliente=cliente
        self.status=status

    #metodo total_pedido() que calcula o total do pedido aplicando map e reduce nos produtos e suas quantidades
    def total_pedido(self):
        total = 0
        for produto, quantidade in zip(self.produtos, self.quantidade.values()):
            preco_total = quantidade * produto.preco
            total += preco_total
        return total
    
    
    def detalhes_pedido(self):
        print('='*40)
        print(f'Produtos: {self.produtos}')
        print(f'Quantidade: {self.quantidade}')
        print(f'Cliente: {self.cliente}')
        print(f'Status: {self.status}')
        print('='*40)

