class ListaDeCompras:
    def __init__(self):
        self.lista = []
    
    def inserir(self):
        while True:
            item = input('Digite o nome do item: ')
            self.lista.append(item)
            continuar = input('Digite 1 para continuar ou 2 para sair: ')
            
            if continuar == '1':
                pass
            elif continuar == '2':
                break 
            else:
                print('Você digitou um valor inválido')
    
    def exibir(self):
        i=0
        while i<len(self.lista):
            print(f'{i+1}.{self.lista[i]}')
            i+=1
    


minhaLista=ListaDeCompras()
minhaLista.inserir()
minhaLista.exibir()