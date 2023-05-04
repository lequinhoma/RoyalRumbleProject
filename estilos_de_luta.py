import random

def carrega_lista():
        with open ("estilos_de_luta.txt") as lista:
            lista = []
            for x in lista:
                x=x.strip()
                lista.append(x)
                return lista
def características(self):
    estilo = self.estilo
    if estilo == 1:
        forca += 2
        velocidade -=2
        return forca, velocidade
    elif estilo == 2:
        forca -=2
        velocidade +=3
        return forca,velocidade
    elif estilo==3:
        forca+=1
        velocidade+=1
        return forca,velocidade
    elif estilo ==4:
        força += random.randrange(0,4)
        velocidade -= random.randrange(0,4)
        return forca, velocidade

class EstiloDeLuta():
    def __init__(self):
        lista = carrega_lista()
        print(lista)
        self.estilo = input(f"Qual seu estilo de luta? Escolha um numero")