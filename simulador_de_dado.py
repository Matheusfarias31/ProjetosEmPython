# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladordeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
        # Layout
        self.layout  =  [      
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]
        

    def Iniciar(self):
        # janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)

        # Ler os valores na tela
        self.eventos, self.valores = self.janela.Read()

        # execução
        try:
            if self.eventos == 'sim':
                self.GerarValorDoDado()
                print('Obrigado por jogar!')
            else:
                print('Obrigado por jogar conosco, Volte sempre!')

        except:
            print('Ocorreu um erro com a sua resposta!')
            

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladordeDado()
simulador.Iniciar()