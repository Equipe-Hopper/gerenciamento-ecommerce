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
from .Produto import Produto

class Pedido(Produto):
    def __init__(self, produtos,quantidade,cliente:str,status:str):
        self.produtos = produtos =[]
        self.quantidade=quantidade={}
        self.cliente=cliente
        self.status=status

    def total_pedido(self):
        pass
    def detalhes_pedido(self):
        print('='*40)
        print(f'Produtos: {self.produtos}')
        print(f'Quantidade: {self.quantidade}')
        print(f'Cliente: {self.cliente}')
        print(f'Status: {self.status}')
        print('='*40)
        
