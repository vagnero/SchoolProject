#============================================================== IMPORTS ========================================================================
import Funcoes
import os
import glob
from classMTC import *
import Color
dados = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 10]

primeiroNomeDoMenu = "Selecione abaixo as opções do crud desejadas utilizando as setas do teclado e pressione enter para confirmar:\n"
Lista_CRUDs = ["Create (Criar)", "Read (Ler)", "Update (Atualizar)", "Delete (Apagar)", "Calculate (Calcular)", "Exit (Sair)"]
ListaTeste2 = ["Criar arquivo de banco de dados", "Inserir dados", "Voltar"]
        
class Crud:    

    nomeEscolhido = ""                                                      # Atributo de classe criado para pegar o nome que o usuário escolher no menu.
    listaTxt = []                                                           # Lista que armazena todos os arquivos .txt.
    listaMTC = []                                                           # Lista que armazena as medidas de tendência central
    listaNorm = []
    listaBino = []
    listaTitulosFontes = []
    #medidas = Medidas_MTC(dados)
    #self.dados = Medidas

           
#=========================================================================== FUNÇÃO PARA ATUALIZAR A LISTA ===========================================    
    
    # Pega o diretório onde os arquivos estão, Coding room = "/usercode/". gdb = "/home/". O parâmetro tipoDoArquivo, é o nome que o usuário atualizará a lista
    def atualizarLista(self, tipoDoArquivo):
        diretorio = os.getcwd()
        
        # Essa função tem o valor do caminho do diretório com todos os arquivos .txt no final. 
        arquivos = os.path.join(diretorio,"*"+tipoDoArquivo)                          
        
        # Pega todos os arquivos do diretório com (.txt) no fim e os transforma em lista
        arquivosEmLista = glob.glob(arquivos)
        if tipoDoArquivo =="-mtc.txt":                               
            for file in arquivosEmLista: 
                # O replace retira a parte do diretório na lista.
                file = file.replace(diretorio+"/","")                           
                if not file in self.listaMTC:
                    self.listaMTC.append(file)

            # Para manter a palavra voltar no final da lista, é necessário excluíla, pois sem isso a palavra não é atualizada de posição
            if "Voltar" in self.listaMTC: 
                
                # Remove a palavra voltar da lista. 
                self.listaMTC.remove("Voltar")                                  
            
            # Se a palavra voltar não existe na lista, então ela é adicionada no final da lista.
            if not "Voltar" in self.listaMTC:                                   
                self.listaMTC.append("Voltar")
        
        elif tipoDoArquivo =="-bino.txt":
            for file in arquivosEmLista: 
                
                # O replace retira a parte do diretório na lista.
                file = file.replace(diretorio+"/","")                           
                if not file in self.listaBino:
                    self.listaBino.append(file)

            # Para manter a palavra voltar no final da lista, é necessário excluíla, pois sem isso a palavra não é atualizada de posição
            if "Voltar" in self.listaBino: 
                # Remove a palavra voltar da lista. 
                self.listaBino.remove("Voltar")                                  
            
            # Se a palavra voltar não existe na lista, então ela é adicionada no final da lista.
            if not "Voltar" in self.listaBino:                                   
                self.listaBino.append("Voltar")
        elif tipoDoArquivo =="-norm.txt":
            for file in arquivosEmLista: 
                
                # O replace retira a parte do diretório na lista.
                file = file.replace(diretorio+"/","")                           
                if not file in self.listaNorm:
                    self.listaNorm.append(file)

            # Para manter a palavra voltar no final da lista, é necessário excluíla, pois sem isso a palavra não é atualizada de posição
            if "Voltar" in self.listaNorm: 
                # Remove a palavra voltar da lista. 
                self.listaNorm.remove("Voltar")                                  
            
            # Se a palavra voltar não existe na lista, então ela é adicionada no final da lista.
            if not "Voltar" in self.listaNorm:                                   
                self.listaNorm.append("Voltar")
        
#================================================================== FUNÇÃO PARA CRIAR UM TXT ===========================================================  
   
   # Criar Banco de dados e Salvar em um TXT (Números)
    def Create(self, tipoDoArquivo):  
    # Atualiza a lista que está no atributo da classe, como não pode ter nomes repetidos.
        self.atualizarLista(tipoDoArquivo)                                                
    
        # O usuário escreve o nome do arquivo txt, se  ele escrever (.txt), será removido. No fim é adicionado o (.txt)

        titulo = input("Digite o nome do seu arquivo txt: ")+tipoDoArquivo.replace(".txt","")+".txt"  
        if titulo ==tipoDoArquivo:
            print("É preciso digitar algum nome, tente novamente!")
        if not titulo =="-mtc.txt" and not titulo == "-bino.txt" and not titulo =="-norm.txt":

            #O try aqui caça erros na criação do txt, pois se o usuário for criar um que já existe, gerará erros
            try:
                novo = open(titulo,"x")                                    # O open("","x") cria um arquivo txt caso não exista um com o mesmo nome.
            except:
                print("Arquivo já existe! Tente novamente")
            else:
                print("Arquivo criado com sucesso.")
                TITULO = input("Digite um título para os seus dados: ").upper()

                #Se o usuário não digitar nada no título e fonte, eles terão um "nome padrão".
                if len(TITULO)<1:
                    TITULO ="-"
                fonte = input("Digite uma fonte para os dados coletados: ").upper() 
                if len(fonte)<1:
                    fonte = "-"

#Adiciona o nome do arquivo txt criado, o nome do título e o nome da fonte. Tudo para serem utilizados posteriormentes a partir desse txt.    
                with open("TitulosFontes.av","a+") as add:
                    add.write(titulo+", "+TITULO+", "+fonte+"\n")
                        
            #listaMTC.append(titulo)
                                                                 # Se já existir, o except irá apontar isso
        
        
                
                
        Funcoes.input_loop("Pressione qualquer tecla para voltar!")                            # Input para que o usuário possa ver se foi criado ou não o arquivo txt escrito.

#======================================================= FUNÇÃO PARA CRIAR UM MENU ===========================================================          
    
    # O primeiro parâmetro é para colocar uma lista com os nomes que aparecerão no menu. O segundo é o título do menu.
    def criarMenu(self,listaDeNomes,nomeDoMenu): 

        # Atualiza a lista do objeto, contendo todos os arquivos .txt criados.
        self.atualizarLista("-mtc.txt") 
        self.atualizarLista("-bino.txt")
        self.atualizarLista("-norm.txt")
        # Pega a função que cria menus e gera um menu com os parâmetros da função criarMenu().
        Funcoes.menu(listaDeNomes,nomeDoMenu)

        # A var nome escolhi será igual a função retorno do arquivo Funcoes.py.
        self.nomeEscolhido=Funcoes.retorno()                                


#========================================================== FUNÇÃO PARA INSERIR DADOS NOS TXT'S ===================================================== 
    
    # Função onde é estabelecido dois menus, um para criar um banco de dados e outro para adicionar dados ao banco de dados.
    def criarBanco(self):                                                         
        
        #nomeEscolhidoLocal = self.nomeEscolhido 
        while True:
            listaDoMenu = ["Criar arquivo de banco de dados mtc","Cria arquivo de banco de dados binomial", "Criar arquivo de banco de dados normal","Voltar"]              # Lista para o menu abaixo.
            self.criarMenu(listaDoMenu,"Escolha a opção abaixo desejada:\n")        # Menu com 3 opções.
            if self.nomeEscolhido =="Criar arquivo de banco de dados mtc":          # Se esta opção for escolhida, então é criado um banco de dados.
                self.Create("-mtc.txt")                                              # Função que cria o banco de dados.

            elif self.nomeEscolhido == "Cria arquivo de banco de dados binomial":
                self.Create("-bino.txt")
                break

            elif self.nomeEscolhido == "Criar arquivo de banco de dados normal":
                self.Create("-norm.txt")

            # Se a opção escolhida for voltar, então será retornado falso e quebrará o loop.
            elif self.nomeEscolhido == "Voltar":                        
                return False
                break


#==================================================== FUNÇÃO PARA LER OS DADOS DO TXT'S ============================================================== 
#def Read():   # Ler o TXT

    def lerArquivos(self):
        while True:
            os.system("clear")
            listaDoMenu = ["Exibir dados de MTC", "Exibir dados de probabilidade Binomial", "Exibir dados de probabilidade normal", "Voltar"]
            self.criarMenu(listaDoMenu,"Escolha qual dados deseja ver:\n\n")
            if self.nomeEscolhido =="Voltar":
                break
            
            elif self.nomeEscolhido =="Exibir dados de MTC":
                self.criarMenu(self.listaMTC,"Escolha o arquivo txt que deseja exibir os dados:\n\n")
                if self.nomeEscolhido!="Voltar":
                    informacoesLista=[]
                    with open (self.nomeEscolhido,"r") as ler:
                        for linha in ler.readlines():
                            #linha = linha.replace(",",".")
                            informacoesLista.append(linha.rstrip())
                    Funcoes.imprimirDados(informacoesLista,"Cotações")
                    Funcoes.input_loop("Pressione qualquer tecla para voltar!")
            elif self.nomeEscolhido =="Exibir dados de probabilidade Binomial":
                self.criarMenu(self.listaBino,"Escolha o arquivo txt que deseja exibir os dados:\n\n")
                if self.nomeEscolhido !="Voltar":
                    informacoesLista=[]
                    with open (self.nomeEscolhido,"r") as ler:
                        for linha in ler.readlines():
                            informacoesLista.append(linha.rstrip())
                        Funcoes.imprimirDados(informacoesLista,"Valores binomiais")
                        Funcoes.input_loop("Pressione qualquer tecla para voltar!")
            elif self.nomeEscolhido =="Exibir dados de probabilidade normal":
                self.criarMenu(self.listaNorm,"Escolha o arquivo txt que deseja exibir os dados:\n\n")
                if self.nomeEscolhido != "Voltar":
                    informacoesLista=[]
                    with open (self.nomeEscolhido,"r") as ler:
                        for linha in ler.readlines():
                            informacoesLista.append(linha.rstrip())
                        Funcoes.imprimirDados(informacoesLista,"Valores binomiais")
                        Funcoes.input_loop("Pressione qualquer tecla para voltar!")
#================================================= FUNÇÃO PARA SUBSTITUIR UM INDEX DA LISTA ================================================================= 

    def Substituir(self,nomeEscolhidoArquiv):
        while True:
            os.system("clear")
            dados = []
            
            print("Dados antigos: ", dados)
            
            #Será aberto o arquivo que o usuário escolher (no menu) e será imprimido todos os dados para ele escolher qual dado será trocado
            with open (nomeEscolhidoArquiv,"r+") as ler:
                for linha in ler.readlines():
                    linha = linha.rstrip()
                    dados.append(linha)
                for contador, i in enumerate(dados):
                    print (contador+1,i)
                print("")
            # Usuário vai entrar com input (index a ser substituido). Como há 3 tipos diferentes de dados, foi criado 3 condicionais para alterar os respectivos dados.
            if "-mtc.txt" in self.nomeEscolhido:
                try:
                    index = int(input("Digite o índice do dado que deseja substituir: \n"))
                except:
                    index = 0
                if index>0 and index<=len(dados):
                    try:
                        resp = float(input("Digite o novo valor: \n"))                    
                        dados[int(index)-1] = str(resp)
                        Funcoes.alterarLinha(nomeEscolhidoArquiv,(int(index)-1),str(resp))
                        print("Valor alterado com sucesso! Novos dados: ", dados)  
                    except:
                        print("Ocorreu algum erro! Tente novamente! \n")
                else:
                    print("Ocorreu um erro! Índice inexistente.\n")
                if Funcoes.input_loop("Pressione esc para voltar, ou qualquer tecla para continuar alterando dados: \n") == True:
                    break
            elif "-bino.txt" in self.nomeEscolhido:
                try:
                    index= int(input("Digite o índice do dado que deseja substituir: \n"))
                except:
                    index = 0
                if index>0 and index<=len(dados):
                    try:
                        resp1 = int(input("Digite o novo valor de n: "))
                        resp2 = float(input("Digite o valor de p: \n"))
                        dados[int(index)-1] = (str(resp1)+", "+str(resp2))
                        Funcoes.alterarLinha(nomeEscolhidoArquiv,(int(index)-1),str(resp1)+", "+str(resp2))
                        print("Valores alterados com sucesso! Novos dados: ", dados)
                    except:
                        print("Ocorreu algum erro! Tente novamente!\n")
                else:
                    print("Ocorreu um erro! Índice inexistente.\n")
                if Funcoes.input_loop("Pressione esc para voltar, ou qualquer tecla para continuar alterando dados: \n") == True:
                    break
            
            elif "-norm.txt" in self.nomeEscolhido:
                try:
                    index = int(input("Qual valor você gostaria de substituir, pelo índíce? \n"))
                except:
                    index = 0
                if index>0 and index<=len(dados):
                    try:
                        resp1 = float(input("Digite o valor desejado: "))
                        resp2 = float(input("Digite a média: "))
                        resp3 = float(input("Digite o desvio padrão: \n"))
                        dados[int(index)-1] = (str(resp1)+", "+str(resp2)+", "+str(resp3))
                        Funcoes.alterarLinha(nomeEscolhidoArquiv,(int(index)-1),str(resp1)+", "+str(resp2)+", "+str(resp3))
                        print("Valores alterados com sucesso! Novos dados: ", dados)
                    except:
                        print("Ocorreu algum erro! Tente novamente!\n")
                else:
                    print("Ocorreu um erro! Índice inexistente.\n")
                if Funcoes.input_loop("Pressione esc para voltar, ou qualquer tecla para continuar alterando dados: \n") == True:
                    break
#==================================================== FUNÇÃO PARA ADICIONAR DADOS PARA O TXT ============================================================== 
    #def Update():                                                                   
    def atualizarDados(self):
        while True:
            os.system("clear")
            listaMenu = ["Adicionar dados", "Alterar dados", "Voltar"]
            self.criarMenu(listaMenu," Escolha a opção desejada:\n\n")
            if self.nomeEscolhido =="Voltar":
                break
            elif self.nomeEscolhido =="Alterar dados":
                while True:
                    os.system("clear")
                    listaMenu = ["Alterar medidas de tendência central", "Alterar probabilidade binomial", "Alterar probabilidade normal", "Voltar"]
                    self.criarMenu(listaMenu,"Selecione qual tipo de arquivo deseja alterar os dados:\n\n")
                    if self.nomeEscolhido =="Voltar":
                        break  

#============Esta parte do códigio cria menus com 3 escolhas, mtc, bino e normal. Isto caso seja escolhido a opção alterar dados no menu anterior===========#
                    elif self.nomeEscolhido =="Alterar medidas de tendência central":
                        while True:
                            self.criarMenu(self.listaMTC,"Escolha o arquivo que deseja alterar dados:\n\n")
                            if self.nomeEscolhido =="Voltar":
                                break
                            else:
                                self.Substituir(self.nomeEscolhido)
                    elif self.nomeEscolhido == "Alterar probabilidade binomial":
                        while True:
                            self.criarMenu(self.listaBino,"Escolha o arquivo que deseja alterar dados:\n\n")
                            if self.nomeEscolhido =="Voltar":
                                break
                            else:
                                self.Substituir(self.nomeEscolhido)
                    elif self.nomeEscolhido =="Alterar probabilidade normal":
                        while True:
                            self.criarMenu(self.listaNorm,"Escolha o arquivo que deseja alterar dados:\n\n")
                            if self.nomeEscolhido =="Voltar":
                                break
                            else:
                                self.Substituir(self.nomeEscolhido)

#============================Já essa parte é para caso o usuário escolha a opção adicionar dados===========================#  
            elif self.nomeEscolhido =="Adicionar dados":
                while True:
                    os.system("clear")
                    listaDoMenu = ["Atualizar medidas de tendência central", "Atualizar probabilidade binomial", "Atualizar probabilidade normal", "Voltar"]
                    self.criarMenu(listaDoMenu,"Escolha qual banco de dados deseja atualizar:\n\n")
                    if self.nomeEscolhido =="Voltar":                
                        break


#==================================================Condicional para Adicionar dados MTC==================================================
                    # Se a opção escolhida for inserir dados, o usuário escolherá um txt para adicionar dados do tipo float.
                    elif self.nomeEscolhido =="Atualizar medidas de tendência central":
                        # Cria um menu com todos os arquivos txt criados.                              
                        self.criarMenu(self.listaMTC,"Escolha o arquivo txt que deseja adicionar dados:\n"+"\n") 

                        # Se o nome escolhido for diferente de voltar, então serão adicionados dados ao arquivo txt escolhido.
                        if self.nomeEscolhido!="Voltar":                                    
                            
                            # Abre o arquivo txt, com o nome que o usuário escolheu no menu e entra no modo de adicionar.
                            with open (self.nomeEscolhido,"a") as add:  

                                # Loop onde o usuário irá adicionar números que deseja adicionar no txt selecionado.
                                while True: 
                                    os.system("clear")                                                
                                    AdicionarItens = input("Digite os números que deseja adicionar: \n")

                                    # Essa função verifícia se o número que o usuário inseriu é float, caso não, retorna falso, se sim, retorna true.
                                    verificar= Funcoes.isfloat(AdicionarItens)              
                                    if verificar ==True:
                                        numero = float(AdicionarItens)
                                        add.write(str(numero)+"\n")
                                        print("Dados adicionados com sucesso!\n")
                                    # O loop continuará até o usuário inserir alguma letra ou pressionar apenas o enter.
                                    else:                                                   
                                        print("\nOcorreu algum erro, por favor tente novamente\n")
                                        
                                    if Funcoes.input_loop("Pressione esc para sair, ou qualquer tecla para continuar adicionando.") == True:
                                        break

#==================================================Condicional para Adicionar dados BINO==================================================
                    elif self.nomeEscolhido =="Atualizar probabilidade binomial":
                        #Cria um menu com todos os arquivos txt criados.                              
                        self.criarMenu(self.listaBino,"Escolha o arquivo binomial que deseja adicionar dados:\n"+"\n") 

                        # Se o nome escolhido for diferente de voltar, então serão adicionados dados ao arquivo txt escolhido.
                        if self.nomeEscolhido!="Voltar":                                    
                            
                            # Abre o arquivo txt, com o nome que o usuário escolheu no menu e entra no modo de adicionar.
                            with open (self.nomeEscolhido,"a") as add:  

                                # Loop onde o usuário irá adicionar números que deseja adicionar no txt selecionado.
                                while True:       
                                    #print("Caso queria sair da adição de valores, basta inserir valores errados em ambos os campos!\n")                                          
                                    AdicionarN = input("Digite o valor de n, para realizar o cálculo binomial: \n")
                                    AdicionarP = input("Digite o valor de p (entre 0 e 1), para realizar o cálculo binomial: \n")
                                    # Essa função verifícia se o número que o usuário inseriu é float, caso não, retorna falso, se sim, retorna true.
#O verificar, verifica se o usuário colocou números float nos input, e também é verificado se p é maior do que 0 e menor do que 1. Caso seja diferente disso, a função retorna falso.
                                    verificar= Funcoes.isBinomial(AdicionarN, AdicionarP)              
                                    
                                    if verificar ==True:
                                        numeroN = int(AdicionarN)
                                        numeroP= float(AdicionarP)
                                        add.write(str(numeroN)+", "+str(numeroP)+"\n")
                                        print("Dados adicionados com sucesso!\n")
                                    else:
                                        print("Ocorreu algum erro! Tente novamente.\n")
                                    #Para sair do loop, é necessário pressioar esc, caso queira ficar, é necessário pressionar qualquer outra tecla.
                                    if Funcoes.input_loop("Pressione esc para sair, ou qualquer tecla para continuar adicionando.") ==True:
                                        break
                                    
#==================================================Condicional para Adicionar dados NORM==================================================
                    elif self.nomeEscolhido =="Atualizar probabilidade normal":
                        self.criarMenu(self.listaNorm,"Escolha o arquivo normal que deseja adicionar dados:\n"+"\n") 

                        # Se o nome escolhido for diferente de voltar, então serão adicionados dados ao arquivo txt escolhido.
                        if self.nomeEscolhido!="Voltar":                                    
                            
                            # Abre o arquivo txt, com o nome que o usuário escolheu no menu e entra no modo de adicionar.
                            with open (self.nomeEscolhido,"a") as add:  

                                # Loop onde o usuário irá adicionar números que deseja adicionar no txt selecionado.
                                while True:                                                 
                                    adicionarValor = input("Adicione o valor para o cálculo de probabilidade normal: ")
                                    adicionarMedia = input("Adicione a média: ")
                                    adicionarDesvioPad = input("Adicione o desvio padrão: ")
                                    verificar = Funcoes.isNormal(adicionarValor,adicionarMedia,adicionarDesvioPad)
                                    # Essa função verifícia se o número que o usuário inseriu é float, caso não, retorna falso, se sim, retorna true.
                                    if verificar ==True:
                                        adicionarValor = float(adicionarValor)
                                        adicionarMedia = float(adicionarMedia)
                                        adicionarDesvioPad = float(adicionarDesvioPad)
                                        add.write(str(adicionarValor)+", "+str(adicionarMedia)+", "+str(adicionarDesvioPad)+"\n")
                                        print("Dados adicionados com sucesso!\n")
                                    else:
                                        print("Ocorreu algum erro! Tente novamente.\n")
                                    if Funcoes.input_loop("Pressione esc para sair, ou qualquer tecla para continuar adicionando.") ==True:
                                        break    
  

#====================================== FUNÇÃO PARA DELETAR DADOS INDVIDUAIS DO TXT ========================================================================= 

#Esta função com um parâmetro, serve para que usuário possa apagar dados (um por um) do txt escolhido.
    def deletarDadosIndiv(self,nomeEscolhidoArquiv):
        informacoesLista=[] 

        #Abaixo é aberto o arquivo txt no modo de leitura, onde o loop for lê todas as linhas (uma de cada vez) e adiciona para a informacoesLista.
        with open (nomeEscolhidoArquiv,"r") as ler:
            for linha in ler.readlines():
                linha = linha.rstrip()
                informacoesLista.append(linha)

        #Loop para exibir o input e a lista disponível para ser deletada.
        while True:
            os.system("clear")
            for contador, i in enumerate(informacoesLista):
                print (contador+1,i)
            deletar = input("Digite o índice do valor que deseja deletar ou pressione enter (sem digitar números) para sair: \n")

            #A condicional abaixo verifíca se o usuário digitou um número, caso sim, ele transforma o input em int.
            if deletar.isdecimal():
                deletar = int(deletar)
            
            #Essa var abaixo assume true or false, pois a função "isint()", verífica se o número coloca é inteiro ou não.
            verificar = Funcoes.isint(deletar)
            if verificar == False:
                print("Ocorreu um erro! Dados inválidos!\n")
                if Funcoes.input_loop("Pressione esc para sair, ou qualquer tecla para tentar novamente.") == True:
                    break
            else:
                #Se for true, será deletado o número escolhido pelo usuário. Mas só se esse número for igual ao índice escolhido.
                if int(deletar)>0 and int(deletar)<=len(informacoesLista):
                    Funcoes.delete_line(self.nomeEscolhido,deletar)
                #O pop deleta itens pelo index.
                    informacoesLista.pop(deletar-1)
                    print("Dados apagados com sucesso!\n")
                    if Funcoes.input_loop("Pressione esc para parar de apagar dados, ou qualquer tecla para continuar apagando.") == True:
                        break

#========================================= FUNÇÃO PARA DELETAR TODOS OS DADOS DO TXT =========================================================================

    #Esta função deleta todos os dados dentro do arquivo txt.
    def deletarTodosOsDados(self,nomeEscolhidoArquiv):
        os.system("clear")
        with open(nomeEscolhidoArquiv,'r+') as delete:
            delete.truncate(0)
            print("Dados deletados com sucesso!\n")
            Funcoes.input_loop("Pressione qualquer tecla para voltar!")

#================================================ FUNÇÃO PARA DELETAR O ARQUIVO TXT =========================================================================

#Esta função deleta o arquivo txt, ela também deleta o titulo e a fonte armazenados no arquivo "TitulosFontes.av".
    def deletarArquivoCompleto(self,nomeEscolhidoArquiv):
        os.system("clear")
        #Deleta o arquivo que o usuário escolheu do sistema.
        os.remove(nomeEscolhidoArquiv)

        with open("TitulosFontes.av","r+") as ler:

            #Neste for loop, indice tem valor numérico e linha o valor String de cada linha do arquivo aberto
            for indice, linha in enumerate(ler,1):
                if nomeEscolhidoArquiv in linha:
                    #Se o nome do arquivo que foi deletado estiver neste arquivo aberto, então esta linha será deletada. 
                    Funcoes.delete_line("TitulosFontes.av",indice)
        print("Arquivo apagado com sucesso!\n")
        Funcoes.input_loop("Pressione qualquer tecla para voltar!")
#=============================================== FUNÇÃO PARA DELETAR TODOS OS TIPOS DE DADOS NOS TXT ======================================================== 
    #Esta função tem o propósito de ter 3 opções disponíveis para apagar arquivos, um, todos ou o arquivo em si.
    
    def deletarArquivos(self):
        #Menu principal onde é escolhido qual arquivo será apagado.
        while True:
            os.system("clear")
            listaDeDeletar =["Apagar o arquivo que contém os dados", "Apagar todos os dados no arquivo", "Apagar dados escolhidos no arquivo","Apagar relatório txt gerado","Voltar"]
            listaDoMenu = ["Apagar dados de MTC", "Apagar dados de probabilidade binomial", "Apagar dados de probabilidade normal", "Voltar"]

            #Pega a função criarMenu para criar um menu.
            self.criarMenu(listaDoMenu,"Escolha quais dados deseja apagar:\n"+"\n")
            if self.nomeEscolhido =="Voltar":
                break

#==========================================================Condicional deletar MTC=======================================================
            elif self.nomeEscolhido =="Apagar dados de MTC":
                while True:
                    self.criarMenu(listaDeDeletar,"Escolha o que você deseja apagar:\n"+"\n")
                    if self.nomeEscolhido == "Voltar":
                        break    
                    elif self.nomeEscolhido =="Apagar dados escolhidos no arquivo":
                        while True:
                        #Cria um menu com todos os arquivos -mtc.txt, onde o usuário irá escolher um deles para deletar.
                            self.criarMenu(self.listaMTC,"Escolha o arquivo mtc que deseja apagar dados:\n"+"\n")
                            if self.nomeEscolhido!="Voltar":
                                self.deletarDadosIndiv(self.nomeEscolhido)
                            else:
                                break
                    #Se o usuário escolher apagar todos os dados, será selecionado a função que limpa todos os dados do txt.
                    elif self.nomeEscolhido == "Apagar todos os dados no arquivo":
                        while True:
                            self.criarMenu(self.listaMTC,"Escolha o arquivo mtc que deseja apagar todos os dados:\n"+"\n")
                            if self.nomeEscolhido =="Voltar":
                                break
                            else:
                                self.deletarTodosOsDados(self.nomeEscolhido)
                    elif self.nomeEscolhido =="Apagar o arquivo que contém os dados":
                        while True:
                            self.criarMenu(self.listaMTC,"Escolha o arquivo mtc que deseja apagar:\n"+"\n")
                            if self.nomeEscolhido =="Voltar":
                                break
                            else:
                                self.deletarArquivoCompleto(self.nomeEscolhido)
                                self.listaMTC.remove(self.nomeEscolhido)
                    elif self.nomeEscolhido == "Apagar relatório txt gerado":
                        os.system("clear")
                        if os.path.exists("Relatório-MTC.txt"):
                            os.remove("Relatório-MTC.txt")
                            print("Arquivo deletado com sucesso!")
                        else:
                            print("Relatório já foi apagado ou não existe!")
                        input("Aperte enter para voltar: ")
#==========================================================Condicional deletar BINO=======================================================
            elif self.nomeEscolhido =="Apagar dados de probabilidade binomial":
                while True:
                    self.criarMenu(listaDeDeletar,"Escolha o que você deseja apagar:\n"+"\n")
                    if self.nomeEscolhido =="Voltar":
                        break
                    elif self.nomeEscolhido =="Apagar dados escolhidos no arquivo":
                        while True:
                            self.criarMenu(self.listaBino,"Escolha o arquivo binomial que deseja apagar dados:\n"+"\n")
                            if self.nomeEscolhido!= "Voltar":
                                self.deletarDadosIndiv(self.nomeEscolhido)
                            else:
                                break
                    elif self.nomeEscolhido =="Apagar todos os dados no arquivo":
                        while True:
                            self.criarMenu(self.listaBino,"Escolha o arquivo binomial que deseja apagar todos os dados:\n"+"\n")
                            if self.nomeEscolhido =="Voltar":
                                break
                            else:
                                self.deletarTodosOsDados(self.nomeEscolhido)
                    elif self.nomeEscolhido =="Apagar o arquivo que contém os dados":
                        while True:
                            self.criarMenu(self.listaBino,"Escolha o arquivo binomial que deseja apagar:\n"+"\n")
                            if self.nomeEscolhido =="Voltar":
                                break
                            else:
                                self.deletarArquivoCompleto(self.nomeEscolhido)
                                self.listaBino.remove(self.nomeEscolhido)
                    elif self.nomeEscolhido == "Apagar relatório txt gerado":
                        os.system("clear")
                        if os.path.exists("Relatório-BINO.txt"):
                            os.remove("Relatório-BINO.txt")
                            print("Arquivo deletado com sucesso!")
                        else:
                            print("Relatório já foi apagado ou não existe!")
                        input("Aperte enter para voltar: ")
#==========================================================Condicional deletar NORM=======================================================
            elif self.nomeEscolhido =="Apagar dados de probabilidade normal":
                while True:
                    self.criarMenu(listaDeDeletar,"Escolha o que você deseja apagar:\n"+"\n")
                    if self.nomeEscolhido =="Voltar":
                        break
                    elif self.nomeEscolhido =="Apagar dados escolhidos no arquivo":
                        while True:
                            self.criarMenu(self.listaNorm,"Escolha o arquivo normal que deseja apagar dados:\n"+"\n")
                            if self.nomeEscolhido!= "Voltar":
                                self.deletarDadosIndiv(self.nomeEscolhido)
                            else:
                                break
                    elif self.nomeEscolhido =="Apagar todos os dados no arquivo":
                        while True:
                            self.criarMenu(self.listaNorm,"Escolha o arquivo normal que deseja apagar todos os dados:\n"+"\n")
                            if self.nomeEscolhido =="Voltar":
                                break
                            else:
                                self.deletarTodosOsDados(self.nomeEscolhido)
                    elif self.nomeEscolhido =="Apagar o arquivo que contém os dados":
                        while True:
                            self.criarMenu(self.listaNorm,"Escolha o arquivo normal que deseja apagar:\n"+"\n")
                            if self.nomeEscolhido =="Voltar":
                                break
                            else:
                                self.deletarArquivoCompleto(self.nomeEscolhido)
                                self.listaNorm.remove(self.nomeEscolhido)
                    elif self.nomeEscolhido == "Apagar relatório txt gerado":
                        os.system("clear")
                        if os.path.exists("Relatório-NORM.txt"):
                            os.remove("Relatório-NORM.txt")
                            print("Arquivo deletado com sucesso!")
                        else:
                            print("Relatório já foi apagado ou não existe!")
                        input("Aperte enter para voltar: ")
#=========================================================================FUNÇÃO PARA ATUALIZAR A LISTA DE TÍTULOS===============================================================================                    
    def atualizarListaTF(self):
        with open ("TitulosFontes.av","r+") as ler:
            for linha in ler.readlines():
                nome, titulo, fonte = linha.strip().split(',')
                self.listaTitulosFontes.append([nome.strip(), titulo.strip(), fonte.strip()])


#================================================ FUNÇÃO PARA CALCULAR AS CONTAS =============================================================================
    #Nesta função é utilizado a classe classMTC, onde é gerado uma tabela no console e um relatório em seguida.
    def calcular(self):
        while True:
            os.system("clear")
            listaDoMenu = ["Calcular dados de medidas de tendência central", "Calcular dados de probabilidade binomial", "Calcular dados de probabilidade normal", "Voltar"]
            self.criarMenu(listaDoMenu,"Escolha quais tipos de dados deseja calcular:\n"+"\n")
            if self.nomeEscolhido =="Voltar":
                break

#=============================================Condicional onde ocorre o cálculo do MTC=========================================================
            elif self.nomeEscolhido =="Calcular dados de medidas de tendência central":
                while True:
                    self.criarMenu(self.listaMTC,"Escolha qual arquivo deseja calcular:\n\n")
                    if self.nomeEscolhido =="Voltar":
                        break
                    else:
                        #Lista onde será pego e convertido todos os dados numéricos de um txt para float.
                        listaLocal = []

                        #Abre o arquivo escolhido no menu em modo de leitura e transforma cada dado em float (também troca pontos por vírgulas).
                        with open(self.nomeEscolhido,"r") as ler:
                            linhas = ler.readlines()
                            for i in linhas: #i é uma linha do txt
                                i = float(i.rstrip().replace(",","."))
                                listaLocal.append(i)

                        medidas = Medidas_MTC(listaLocal)
                        with open("TitulosFontes.av","r+") as lerTF:
                            self.atualizarListaTF()
                            for nomeArq, titulo, fonte in self.listaTitulosFontes:
                                nomeVerificar = nomeArq
                                if nomeVerificar == self.nomeEscolhido:
                                    medidas.Titulo = titulo
                                    medidas.Fonte = fonte
                        
                        print(medidas.Mostrar_MTC())
                        Funcoes.input_loop("Pressione qualquer tecla para voltar!")
                        with open ("Relatório-MTC.txt","a+") as add: # Escrever no TXT
                            try:
                                add.write(medidas.Mostrar_MTC(colorido=False))
                                add.write(15*"\n\n")    
                            except:
                                "Não há dados no arquivo! Tente adicionar dados para realizar o cálculo."
                
#=============================================Condicional onde ocorre o cálculo do BINOMIAL=========================================================
            elif self.nomeEscolhido =="Calcular dados de probabilidade binomial":
                while True:
                    
                    os.system("clear")
                    self.criarMenu(self.listaBino,"Escolha qual arquivo deseja calcular:\n\n")
                    if self.nomeEscolhido =="Voltar":
                        break
                    else:
                        
                        valorN = 0.0
                        valorP =0.0
                        listaLocal=[]
                        with open(self.nomeEscolhido,"r+") as ler:
                            linhas = ler.readlines()

                            #O primeiro loop serve para exibir qual item o usuário quer calcular.
                            for (n ,p) in enumerate(linhas,1):
                                print(n,p)
#O segundo loop serve para que cada número seja convertido para int e float, dentro de uma lista removendo todos os elementos string deles.
                            for item in linhas:
                                elementos = item.strip().split(',')
                                elemento1 = int(elementos[0])
                                elemento2 = float(elementos[1])
                                #Os dois elementos são adicionados para uma lista, para serem pegos posteriormente.
                                listaLocal.append([elemento1,elemento2])
                        print(listaLocal)
                        try:
                            index = int(input ("Qual probabilidade binomial armazenada você gostaria de calcular? "))
                        except:
                            index = 0
                        #As var obtém os valores que foram selecionados, pelo índice acima.
                        
                        #Para evitar erros, foi necessário ter a condicional abaixo, onde vas variáveis abaixo só terão valor se for selecionado um índice que exista na lista.
                        if len(listaLocal)>0 and index <=len(listaLocal):
                            valorN = int(listaLocal[index-1][0])
                            valorP = float(listaLocal[index-1][1])
                    
                            tituloLocal = ""
                            fonteLocal = ""
                            with open("TitulosFontes.av","r+") as lerTF:
                                self.atualizarListaTF()
                                for nomeArq, titulo, fonte in self.listaTitulosFontes:
                                    nomeVerificar = nomeArq
                                    if nomeVerificar == self.nomeEscolhido:
                                        tituloLocal = titulo
                                        fonteLocal = fonte

                            tabela = Funcoes.probBin(valorN,valorP,tituloLocal,fonteLocal)
                            negrito = '\033[1m'
                            with open ("Relatório-BINO.txt","a+") as add: # Escrever no TXT
                                if len(listaLocal)>0:   
                                    add.write(tabela)
                                    add.write(15*"\n\n")

                            print(tabela)
                        else:
                            print("Ocorreu um erro! Índice inexistente.")
                        Funcoes.input_loop("Pressione qualquer tecla para voltar!")

#=============================================Condicional onde ocorre o cálculo do NORMAL=========================================================
            elif self.nomeEscolhido =="Calcular dados de probabilidade normal":   
                while True:
                    os.system("clear")
                    self.criarMenu(self.listaNorm,"Escolha qual arquivo deseja calcular:\n\n")
                    if self.nomeEscolhido =="Voltar":
                        break
                    else:
                        valor = 0.0
                        valorMedia =0.0
                        valorDesvio = 0.0
                        listaLocal=[]
                        with open(self.nomeEscolhido,"r+") as ler:
                            linhas = ler.readlines()

                            #O primeiro loop serve para exibir qual item o usuário quer calcular.
                            contador = 1
                            for v, m, d in (line.split(',') for line in linhas):
                                print(contador, v, m, d)
                                contador = contador+1
#O segundo loop serve para que cada número seja convertido para float, dentro de uma lista removendo todos os elementos string deles.
                            for item in linhas:
                                elementos = item.strip().split(',')
                                elemento1 = float(elementos[0])
                                elemento2 = float(elementos[1])
                                elemento3 = float(elementos[2])
                                
                                #Os três elementos são adicionados para uma lista, para serem pegos posteriormente.
                                listaLocal.append([elemento1,elemento2,elemento3])
                        print(listaLocal)
                        try:
                            index = int(input ("Qual probabilidade binomial armazenada você gostaria de calcular? "))
                        except:
                            index = 0
                        if index>0 and index <=len(listaLocal):
                            #As var obtém os valores que foram selecionados, pelo índice acima.
                            valor = float(listaLocal[index-1][0])
                            valorMedia = float(listaLocal[index-1][1])
                            valorDesvio = float(listaLocal[index-1][2])

                            tituloLocal = ""
                            fonteLocal = ""
                            with open("TitulosFontes.av","r+") as lerTF:
                                self.atualizarListaTF()
                                for nomeArq, titulo, fonte in self.listaTitulosFontes:
                                    nomeVerificar = nomeArq
                                    if nomeVerificar == self.nomeEscolhido:
                                        tituloLocal = titulo
                                        fonteLocal = fonte

                            tabela = Funcoes.calcular_probabilidade_normal(valor,valorMedia,valorDesvio,tituloLocal,fonteLocal)
                            negrito = '\033[1m'
                            with open ("Relatório-NORM.txt","a+") as add: # Escrever no TXT
                                add.write(tabela)
                                add.write(15*"\n\n")
                            print(tabela)
                        else:
                            print("Ocorreu um erro! Índice inexistente.")
                        input("Pressione enter para voltar: ")


teste = Crud()                                                                     # Instancie # Enquanto True, esse menu estará em loop.   

# EnquaiarMenu(Lista_CRUDs,"Selecione abaixo as opções do crud desejadas utilizando as setas do teclado e pressione enter para confirmar:\n")  

# Se o usuário escolher a opção criar, então outro loop será gerado.


