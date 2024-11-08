"""
Atributos:

pedidos (lista de pedidos)
Métodos:



-       
adicionar_pedido(pedido): Adiciona um novo
pedido à lista.


-       
listar_pedidos_por_status(status): Retorna
pedidos com um status específico usando filter.


-       
pedidos_por_categoria(categoria): Usa map para
gerar um relatório de quantos produtos de uma categoria

específica foram vendidos.


-       
total_vendas(): Retorna o valor total de vendas
utilizando reduce."""

# from .Pedido import Pedido
class GestorPedidos:
    def __init__(self,pedidos):
        self.pedidos=pedidos=[]

    def adicionar_pedido(self,pedido):
        self.pedidos.append(pedido)

    def listar_pedidos_por_status(self,status):
        return filter(lambda pedido: pedido.status == status,self.pedidos)
    
    def total_vendas(self):
        return print(self.pedidos)
    
pedido=GestorPedidos("moto")
pedido.adicionar_pedido("carro")
pedido.total_vendas()

    