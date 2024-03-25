import os
import time
import pandas as pd

listaDeCompras=[]

class Item:
    def __init__(self,nome,preco=0,quantidade=0) :
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade
    def subTotal(self):
        return self.preco*self.quantidade


while True:
    nome_item = input("Digite o nome do item: ")
    item = Item(nome_item)
    dadosItem=[item.nome,item.preco,item.quantidade,item.subTotal()]
    listaDeCompras.append(dadosItem)

    continuar = input("Deseja continuar (s/n)? ")
    if continuar.lower() != 's':
        break

df=pd.DataFrame(listaDeCompras)
df.columns = ['Nome', 'Preco', 'Quantidade', 'Subtotal']

print(df.to_string(index=False))
