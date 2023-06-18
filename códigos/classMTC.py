
#dados = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 10]

# ========================= BIBLIOTECAS ===============================
import numpy as np 
from scipy import stats
from Color import color
import Funcoes as func

# Criando uma classe/objeto para retornar todas as medidas
class Medidas_MTC: 
    def __init__(self,dados):
        self.dados = dados
        self.Fonte = ("").upper()
        self.Titulo = ("").upper()
        self.media = 0.0
        self.quartils = [0,0,0]
        self.quartil_1 = self.quartils[0]
        self.quartil_2 = self.quartils[1]
        self.quartil_3 = self.quartils[2]
        self.mediana = self.quartil_2
        self.moda = "Amodal"
        self.variancia = 0.0
        self.desvPad = 0.0
        if len(self.dados) > 0:
            self.Calcular()

    # Função para salvar o TXT
    def Salvar(self):
        texto = ""
        for text in self.dados:
            texto = texto + str(text) + "\n"
        
        if self.Titulo == "":
            self.Titulo == "Banco de Dados " + str(datetime.now())
        
        with open(self.Titulo+'.txt',"w") as arquivo:
            arquivo.writelines(texto)
            self.arquivo = self.Titulo+'.txt'
            
        self.Calcular()

    # Função para calcular as medidas toda vez q a função for chamada
    def Calcular(self):
        self.media = func.Media(self.dados)
        self.quartils = func.Quartils(self.dados)
        self.quartil_1 = self.quartils[0]
        self.quartil_2 = self.quartils[1]
        self.quartil_3 = self.quartils[2]
        self.mediana = self.quartil_2
        self.moda = str(func.Moda(self.dados)).strip('[]')
        self.variancia = func.Variância(self.dados)
        self.desvPad = func.Desvpad(self.dados)
    # Função para mostrar o resultado personalizado em forma de tabela colorida
    def Mostrar_MTC(self, colorido = True):
        sep = "="*30
        if colorido:
            return f"""            
Título: {color(self.Titulo, 'verde', negrito=True)[:30]:^45} 
{color(sep,'roxo',negrito=True)}      
{color('Média: ', 'verde',negrito=True):<30} | {round(self.media,2)}
{color('Mediana: ', 'verde',negrito=True):<30} | {round(self.mediana,2)}
{color('1° Quartil: ', 'verde',negrito=True):<30} | {round(self.quartil_1,2)}
{color('3° Quartil: ', 'verde',negrito=True):<30} | {round(self.quartil_3,2)}
{color('Moda: ', 'verde',negrito=True):<30} | {self.moda}
{color('Variância: ', 'verde',negrito=True):<30} | {round(self.variancia,2)}
{color('Desvio padrão: ', 'verde',negrito=True):<30} | {round(self.desvPad,2)}
{color(sep,'roxo',negrito=True)}
Fonte: {self.Fonte}\n""" 

        # Imprime os resultados em um txt, de forma personalizada em forma de tabela sem cor
        else:   
            sep = "="*45
            return f'''
Título: {self.Titulo[:30]:^45}
{sep}
{"Média: ":<30} | {round(self.media,2)}
{"Mediana: ":<30} | {round(self.mediana,2)}
{"1° Quartil: ":<30} | {round(self.quartil_1,2)}
{"3° Quartil: ":<30} | {round(self.quartil_3,2)}
{"Moda: ":<30} | {self.moda}
{"Variância: ":<30} | {round(self.variancia,2)}
{"Desvio padrão: ":<30} | {round(self.desvPad,2)}
{sep}
Fonte: {self.Fonte}'''

# medidas = Medidas_MTC(dados)
# print(medidas.Mostrar_MTC())
