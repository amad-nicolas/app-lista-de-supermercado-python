import os
import time
import pandas as pd

listaDeCompras=[]



while True:
    nome_item = input("Digite o nome do item: ")
    dadosItem=[nome_item,0,0,0]
    listaDeCompras.append(dadosItem)

    continuar = input("Deseja continuar (s/n)? ")
    if continuar.lower() != 's':
        break

df=pd.DataFrame(listaDeCompras)
df.columns = ['Nome', 'Preco', 'Quantidade', 'Subtotal']

while True:
    os.system('cls')
    print(df.to_string(index=False))
    indice=int(input('Digite o indice do item ao qual editar:'))
    preco=float(input('Digite o preço : '))
    quantidade=float(input('Digite a quantidade : '))
    
    df.iloc[indice,1]=preco
    df.iloc[indice,2]=quantidade
    df.iloc[indice,3]=preco*quantidade
    
    continuar = input("Deseja continuar (s/n)? ")
    if continuar.lower() != 's':
        break


df.to_csv('listaDeCompras.csv',index=False)