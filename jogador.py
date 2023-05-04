import random



class Jogador():
    def __init__(self):
        self.nome = input ("Sob qual nome você deseja lutar??")
        
        self.altura = input ("Qual sua altura? (cm)")
        self.peso =  input ("E qual seu peso?")



def velocidade (self):
    altura = float(self.altura)
    if altura in range (170):
        velocidade = random.randrange(8,11)
        return velocidade
    elif altura in range (170, 180):
        velocidade = random.randrange(6,11)
        return velocidade
    elif altura in range (180,190):
        velocidade = random.randrange(4,8)
        return velocidade
    elif altura  in range (190, 210):
        velocidade = random.randrange (2,6)
        return velocidade
    else:
        velocidade = random.randrange (1,5)
        return velocidade

def forca (self):
    peso = int(self.peso)
    if peso in range (50):
        forca = random.randrange(8,11)
        return forca
    elif peso in range (100, 120):
        forca = random.randrange(6,11)
        return forca
    elif peso in range (85,100):
        forca = random.randrange(4,8)
        return forca
    elif peso in range (70,85):
        forca = random.randrange (2,6)
        return forca
    else:
        forca = random.randrange (1,5)
        return forca
    