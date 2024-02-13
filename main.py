import os
import time
import pandas

class Item:
    def __init__(self,nome,preco=0,quantidade=0,) :
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade
    def subTotal(self):
        return self.preco*self.quantidade


def fechar():
    global run,df
    encerrar=int(input('Digite qualquer tecla para continuar ,caso queira encerrar digite 1: '))
    if encerrar==1:
        total=0
        t=0
        while t<5:
            total+=(df.iloc[t,3]).astype(float)
            t+=1
        
        print(f'o total foi de {total}')
        time.sleep(5)
        run=False
        
    
listaDeCompras=[]
c=0
while c<5:
    item=[]
    nome=input('digite o nome do item:')
    i=Item(nome,0,0)
    item=[i.nome,i.preco,i.quantidade,0]
    listaDeCompras.append(item)
    c+=1
os.system('cls')
df=pandas.DataFrame(listaDeCompras)
print(df)

        
run=True

while run:
    indice=int(input('Digite o indice do item que deseja atualizar: '))
    preco=float(input('Digite o preço unitário do item: '))
    quantidade=int(input('digite a quantidade que ira comprar: '))
    df.iloc[indice,1]=preco
    df.iloc[indice,2]=quantidade
    df.iloc[indice,3]=preco*quantidade
    os.system('cls')
    
    fechar()
    os.system('cls')
    print(df)


   

        
