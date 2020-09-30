# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random

class SimuladordeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim' or resposta == 's':
            self.GerarValorDoDado()
        elif resposta == 'nao' or resposta == 'n' or resposta == 'não':
            print('Obrigado por jogar')
        else:
            print('Favor digitar sim ou não')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladordeDado()
simulador.Iniciar()