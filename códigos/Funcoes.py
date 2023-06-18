import curses
import os
import glob
import tkinter as tk
import numpy as np
import math
from classMTC import *
from Color import color
import sys #Import para poder alterar configurações do terminal
import termios #Import para poder alterar configurações do terminal
import tty #Import para poder alterar configurações do terminal
from scipy.stats import norm
dados = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 10]

#========================================== Funções das medidadas de tendência central =============================================================

def Media(Lista_Dados):                                             # Função para obter a média, com uma lista como parâmetro.
    Soma_Media = 0.0                                                  # Variável para somar e obter a média de todos os valores do par Lista_Dados.
    for i in Lista_Dados:
        Soma_Media =Soma_Media+float(i)                                  # Soma_Media vai ser igual a Soma_Media + i.
    Soma_Media= Soma_Media/len(Lista_Dados)
    return Soma_Media

def Quartils(dados):
    if len(dados) == 0:
        return [0,0,0]
    dados = sorted(dados)
    
    # Função para calcular o 1º, 2º e 3º quartil
    # Calcula o primeiro quartil
    quartil1 = np.percentile(dados, 25)

    # Calcula o segundo quartil (Mediana)
    quartil2 = np.percentile(dados, 50)

    # Calcula o terceiro quartil 
    quartil3 = np.percentile(dados, 75)
    # print("Com biblioteca")
    
    return [quartil1,quartil2,quartil3]

# Função para obter a moda, com uma lista como parâmetro.   
def Moda(Lista_Dados): 

    # Lista que conterá tuplas, contendo todos os valores com seus respectivos "pesos" (quantas vezes tal valor se repete).
    Lista_Moda=[] 
    Lista_Moda_Res=[] # Lista que conterá as modas.
    
    # Loop onde i passará e se tornará em todos os elementos da Lista_Dados.
    for i in Lista_Dados: 
        
        # A variável contador será o valor que cada número se repete, para tal, foi utilizado a função count com o parâmetro(i).
        contador = Lista_Dados.count(i) 
        
        # Se a tupla (contador,i), não estiver na Lista_Moda, então a tupla será adicionada.
        if (contador,i) not in Lista_Moda:
            
            # Append adicionará a tupla, a condição impede que se adicione tuplas repetidas.
            Lista_Moda.append((contador,i))
    
    # Sort organiza a Lista_Moda do menor para o maior.
    Lista_Moda.sort()
    stop = 0                                        # Variável para poder parar o loop abaixo.
    indice = 0                                      # Variável para ser o indice da lista abaixo.
    valor = 0                                       # Variável para pegar o maior valor da Lista_Moda.
    
    # Enquanto a variável stop for menor do que o tamanho (len) da Lista_Moda, o loop ocorrerá.
    while stop<len(Lista_Moda): 
        
        # Como há tuplas dentro da Lista_Moda, a variável indice mudar as tuplas, enquanto que será manipulado apenas o valor do índice[0].
        if (Lista_Moda[indice][0])>valor: 
            
            # A condicional acima possibilita que seja adquirido a tupla com maior valor da lista.
            valor = (Lista_Moda[indice][0])  
        stop = stop + 1                              # Soma para poder parar o loop.
        indice = indice + 1                          # Soma para poder alterar o valor do índice da Lista_Moda.
    stop2=0                                          # Variável para poder parar o novo loop abaixo.
    indice2=0                                        # Variável para poder manipular a lista abaixo.
    while stop2<len(Lista_Moda):
        
        # Tal condição possibilita a checagem se existe moda (algum valor maior do que o primeiro índice do primeiro valor da tupla).
        if valor>(Lista_Moda[0][0]):                 
            
            # Com essa condição, quando a Lista_Moda_Res chegar no valor da variável "valor", saberemos qual é a moda.
            if (Lista_Moda[indice2][0]) == valor:     
                
                # Aqui será adicionado a Lista_Moda_Res todos os últimos valores repetidos da lista, ou seja, pegará todas as modas da lista.
                Lista_Moda_Res.append(Lista_Moda[indice2][1])
        
        # Caso a condição acima seja falsa, não existe moda na lista.
        else:                           
            Lista_Moda_Res.append("Amodal")         # Ao invés de números, será adicionado uma string com o nome de "Amodal", na lista.
            break                                   # O break parará o loop, para não acrescentar mais nada para a lista.
        stop2 = stop2+1
        indice2 = indice2+1
    resposta=""                                     # Variável para transformar todos os elementos da Lista_Moda_Res em string.
    for i in Lista_Moda_Res:
        
        # Se não tiver a string amodal na lista, a variável i não se transformará nela, logo a condição será verdadeira.
        if not i == "Amodal":           
            
            # Formatação para que a variável i seja uma string com duas casas decimais.
            i = "{:.2f}".format(i) 
            
            # A variável resposta será igual a adição da str(i) com a string ", ". Fazendo com que todos os elementos da listas sejam adicionados.
            resposta = resposta+(i)+", " 
        
        # Caso a condicional acima seja falsa, quer dizer que não há moda na lista, logo a lista é amodal.
        else: 
            resposta = "Amodal" # A variável resposta será igual "Amodal".
    
    # A função rstrip está tirando o último espaçamento da variável resposta, pois nada foi especificado.
    resposta = resposta.rstrip() 
    
    # Aqui, a função está tirando a vírgula no final da String, pois uma virgula foi utilizada como parâmetro.
    resposta = resposta.rstrip(",") 
    
    # Aqui será retornado a variável resposta, conforme a condicional que foi verdadeira ou falsa.
    return resposta 


# Função de dispersão para determinar o grau de variação dos números de uma lista com relação à sua média
def Dispersao(dados):
    dispersao=[]
    media = Media(dados)
    for i in dados:
        desvios = media - i
        dispersao.append(desvios)
    return dispersao
    
def Variância(dados):
    dispersao = Dispersao(dados)
    tam = len(dispersao) -1
    soma = 0
    variancia = 0
    for i in dispersao:
        i = i*i
        soma += i
        variancia = soma/tam
    return variancia
    
def Desvpad(dados):
    variancia = Variância(dados)
    desviopad = math.sqrt(Variância(dados))    
    return desviopad

#=================================================== Funções para realizar o cálculo binomial ==============================================================
#Função onde n é o número de elementos e p a probabilidade.
def probBin(n, p, titulo, fonte):
    separador  = "="
    espaco = " "
    nk = 0.0
    #Listas que armazenam os valores float e os valores percentuais.
    listaValores=[]
    listaValoresPercentual=[]
    listaGeral = []

    #Var no formato f string para criar uma tabela, ela já inicia com a parte de cima.
    string =f"Título: {titulo.upper()}\n{separador*60}\nValores binomiais {espaco*17}Valores percentuais\n"

    for k in range(0,n):
        #nk é a valor que que realiza a primeira etapa do cálculo.
        nk = math.factorial(n)/(math.factorial(k)*(math.factorial(n-k)))
        
        #res é a variável que contém a fórmula do cálculo binomial.
        res = ((nk)*(p**k)*((1-p)**(n-k)))
        
        #nesta parte é criado uma var percentual, para converter o a var res em um valor percentual com a strin "%".
        valorPercentual = round((res*100),2)

        #Após, é adicionado os dois valores para as duas respectivas listas.
        listaValores.append(res)  
        listaValoresPercentual.append(str(valorPercentual)+"%")

#Este loop for, está ocorrendo simultaneamente graças ao in zip, que pega duas listas, sendo a var  "valor" correndo na primeira e a var porcento na segunda.
    for valor, porcento in zip(listaValores, listaValoresPercentual):
        valor = str(valor)

#Acima o valor do tipo float foi transformado em String, daí se o loop abaixo adiciona espaços para organizar a tabela, caso a var valor seja menor do que o tamanho 30.    
        while len(valor)<30:
            valor = valor+" "
        #if len(porcento)<6:
            #porcento = " "+porcento
        string = string+f"{valor} {espaco*10} {porcento} \n"
    return string+f"{separador*60}\nFonte: {fonte.upper()}"
        


listaTeste = [43,35,34,58,30,30,36]
# print(Desvpad(listaTeste))

#================================================= FUNÇÃO PARA REALIZAR O CÁLCULO NORMAL ===============================================================
def calcular_probabilidade_normal(x, media, desvio_padrao, titulo, fonte):
    separador  = "="
    espaco = " "
    tabela =f"Título: {titulo.upper()}\n{separador*60}\nValores binomiais {espaco*17}Valores percentuais\n"
    probabilidade = norm.cdf(x, media, desvio_padrao)
    probabilidade_nao_conforme = 1 - probabilidade
    probabilidade_conforme = probabilidade
    stringConforme = str(probabilidade_conforme)
    stringNaoConforme = str(probabilidade_nao_conforme)
    while len(stringNaoConforme)<25:
        stringNaoConforme +=" "
    while len(stringConforme)<25:
        stringConforme += " "
    tabela = f'''Título: {titulo.upper()}\n{separador*80}\nValores Decimais {espaco*30}Valores percentuais
Conformes: {stringConforme}{espaco*9}  Conformes: {probabilidade_conforme:.2%} 
Não Conformes:{stringNaoConforme} {espaco*5}  Não Conformes {probabilidade_nao_conforme:.2%}
{separador*80}'''
    

    return tabela


#================================================= FUNÇÕES DO CURSES PARA O MENU =====================================================================

#classes = ["Alterar dados", "Incluir dados", "Excluir dados", "Produzir relatório", "Sair do programa"]
import curses

def menu(listaMenu, tituloDoMenu):
    stdscr = curses.initscr() # Inicializa a janela padrão
    curses.curs_set(0) # Oculta o cursor na tela
    curses.start_color() # Inicializa o uso de cores
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK) #Adiciona e define pares de cores dentro do curses (com numeração 1).
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.keypad(True) # Permite capturar teclas especiais
    
    option = 0
    window_height, window_width = stdscr.getmaxyx()
    
    while True:
        stdscr.refresh()
        stdscr.clear()

        stdscr.addstr(tituloDoMenu, curses.A_BOLD | curses.A_UNDERLINE) # Adiciona o título do menu com formatação em negrito e sublinhado

        num_visible_options = window_height - 13

        start_index = max(0, option - num_visible_options // 2)
        end_index = min(len(listaMenu), start_index + num_visible_options)

        # Adiciona cada item do menu na tela
        for i in range(start_index, end_index):
            stringNome = listaMenu[i]
            selecao = curses.color_pair(2) if i == option else curses.color_pair(1)
            stdscr.addstr(f"{i + 1}. {stringNome}\n", selecao)

        c = stdscr.getch() # Espera o input do usuário

        # Atualiza a opção selecionada com base na tecla pressionada (cima ou baixo).
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(listaMenu) - 1:
            option += 1
        elif c == curses.KEY_UP and option == 0:
            option = len(listaMenu) - 1
        elif c == curses.KEY_DOWN and option == len(listaMenu) - 1:
            option = 0
        elif c == curses.KEY_PPAGE:  # Page Up
            option = max(0, option - num_visible_options)
        elif c == curses.KEY_NPAGE:  # Page Down
            option = min(len(listaMenu) - 1, option + num_visible_options)

        window_height, window_width = stdscr.getmaxyx()

        if len(listaMenu) > window_height - 2:
            scrollbar_pos = int((window_height - 2) * option / len(listaMenu))  # Calcula a posição da barra de rolagem
            stdscr.addstr(scrollbar_pos + 1, window_width - 2, "▒") # Adiciona a barra de rolagem vertical

        if c == curses.KEY_ENTER or c == 10:
            break

        window_height, window_width = stdscr.getmaxyx()

    # Encerra a execução do menu e armazena a opção escolhida e seu nome
    global nomeEscolhido
    nomeEscolhido = listaMenu[option]
    stdscr.refresh()
    curses.endwin() # Encerra a biblioteca `curses`

# Função para retornar o valor da var nomeEscolhido, em forma de string.
def retorno ():                                                 
    return nomeEscolhido


#=======================================FUNÇÕES PARA VALIDAR A ENTRADA DOS NÚMEROS=================================================
#Entrada do MTC.
def isfloat(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False
def isint(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False

#Essa função verifica retorna true se o usuário inserir um int e um float maior do que 0 e menor do que 1.
def isBinomial(n,p):
    try:
        int(n)
        float(p)
        if int(n) and float(p):
            if float(p)>0.0 and float(p)<1.0:
                return True
            else:
                return False
    except ValueError:
        return False
def isNormal(v,m,d):
    try:
        float (v)
        float (m)
        float (d)
        if float(v) and float(m) and float (d):
            return True
        else:
            return False
    except ValueError:
        return False
#====================================================Função para o usuário sair de um loop pressionando enter=====================================================
def input_loop(stringAlerta):
    user_input = "" #Variável onde terá o valor do input do usuário
    configOriginal = termios.tcgetattr(sys.stdin) #Retorna a configuração original do terminal.
    try:
        # Set terminal to raw mode
        tty.setraw(sys.stdin.fileno()) #Esta função faça com que o enter não funcione no input.
        
        while True:
            print(stringAlerta+"\n")
            char = sys.stdin.read(1) #Lê somente 1 character do input do usuário
            os.system("clear")
            if ord(char) == 27:  # O ord(char) == 27, chega se foi pressionado esc, caso sim, o loop é quebrado
                return True
                break
            
            else:
                #Caso não, o loop continuará!
                return False
                #user_input += char
    #Finally se certifica que o terminal seja restaurado para a sua versão original.
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, configOriginal)
#==================================================== Funções para alterar valor de uma linha ============================================================

#Função com 3 parâmetros, nome do txt, índice que deseja alterar o valor e o novo valor para substituir o antigo
def alterarLinha(nomeDoArquivo, indice, novoValor):
    # Lê todo o conteúdo no nome que o usuário colocar.
    with open(nomeDoArquivo, 'r') as arquivo:
        linha = arquivo.readlines()

    # Troca a linha desejada somente se o tamanho do txt for maior que o índice colocado e se o índice for maior/igual a zero.
    if len(linha) > indice >= 0:
        linha[indice] = novoValor + '\n'

        # Escreve o valor modificado no arquivo txt selecionado
        with open(nomeDoArquivo, 'w') as arquivo:
            arquivo.writelines(linha)


#=================================================== Funções para deletar dados do txt ==============================================================
#Essa função deleta uma linha especificada pelo usuário.
def delete_line(filename, line_number):
    # Read the file into a list
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove the desired line
    if line_number < 1 or line_number > len(lines):
        print("Inválido número de índice!")
        return

    del lines[line_number - 1]
    with open(filename, 'w') as file:
        file.writelines(lines)

def imprimirDados(lista, string):
    # Verifica se a lista está vazia
    if not lista:
        print("A lista está vazia.")
        return

    # Obtém o tamanho máximo dos dados para alinhar os valores
    tamanho_maximo = max(len(str(dado)) for dado in lista)

    # Imprime os dados organizados
    print(string)
    for i, valor in enumerate(lista, start=1):
        # Calcula o espaço em branco necessário para centralizar o valor
        espacos = (tamanho_maximo - len(str(valor))) // 2

        # Formata o valor com espaços em branco antes e depois
        valor_formatado = f"{espacos * ' '}{valor}{espacos * ' '}"
        # Se o tamanho do valor for ímpar, adiciona um espaço em branco extra no final
        if len(valor_formatado) < tamanho_maximo:
            valor_formatado += ' '
        
        i = str(i)+":"
        tamanhoLista = str(len(lista))
        if len(i)<len(tamanhoLista)+1:
            i = i+" "
        # Imprime o número e o valor formatado
        print(f"{i} {valor_formatado}")
    

# Exemplo de us

