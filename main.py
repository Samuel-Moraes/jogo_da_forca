import random


def jogar():

  palavra_secreta = selecionaPalavraSecreta()

  letrasAcertadas = inicializaLetrasAcertadas(palavra_secreta)

  # Variaveis para validar se o chute esta ou não correto
  enforcou = False
  acertou = False
    
  erros = 0 # Variavel utilizada para validar a quantidade de vidas

  while(not enforcou and not acertou):
    vidas = 6 - erros
    print("")
    print("jogando...")
    print("Você possui " , vidas, " vidas" )
    print(letrasAcertadas)
    print("")

    chute = pedeChute()
    print("")
      # Estrutura lógica de validação da letra que foi chutada

    if(chute in palavra_secreta):
      marcaChuteCorreto(chute, letrasAcertadas, palavra_secreta)

    else:
      erros += 1
      print("A palavra não possui a letra digitada")
      print("")
        

    enforcou = erros == 6
    acertou = "_" not in letrasAcertadas

    print(letrasAcertadas)
  
  if(acertou):
    imprime_mensagem_vitoria()
    menu()

  else:
    imprime_mensagem_derrota()
    menu()

  print("Fim do jogo")

def imprime_mensagem_abertura():
  print("Desenvolvido por Samuel Moraes")
  print("")
  print("###################################")
  print("### Bem vindo ao jogo da Forca! ###")
  print("###################################")
  print("")

def inicializaLetrasAcertadas(palavra_secreta):
  # Neste retorno, trara um _ para cada letra da palavra que foi selecionada
  return ["_" for letra in palavra_secreta]

def pedeChute():
  chute = input("Digite uma letra: ")
  chute = chute.strip().upper()
  return chute

def marcaChuteCorreto(chute, letrasAcertadas, palavra_secreta):
  # Esta função é reponsável por validar se a letra chutada existe na palavra secreta
  index = 0
  for letra in palavra_secreta:
    if(chute == letra):
      letrasAcertadas[index] = letra
    index += 1

def imprime_mensagem_vitoria():
  print("")
  print("Parabens, você concluiu o jogo com sucesso")
  print("")

def imprime_mensagem_derrota():
  print("")
  print("Você foi enforcado! x.x")
  print("")

def seleciona_genero():
  
  print("")
  print('#################################################')
  print('# DIGITE O NUMERO REFERENTE AO GENERO ESCOLHIDO #')
  print('#################################################')
  print('# 1 - ESTADOS E CIDADES BR                      #')
  print('# 2 - BEBIDAS                                   #')
  print('# 3 - NOMES                                     #')
  print('# 4 - COMIDAS                                   #')
  print('# 5 - DIVERSOS                                  #') 
  print('#################################################')
  print("")

  genero = input("OPÇÃO DESEJADA: ")

  return genero

def selecionaPalavraSecreta():
  palavraArquivo = []
  tipos_genero = [1,2,3,4,5]
  tmp_genero = 0

  genero = seleciona_genero()

  if genero in tipos_genero:
    tmp_genero = genero

  else:
    tmp_genero = 6

  if tmp_genero == 1: # Estados e cidades brasileiros
    arquivo = open("estados.txt", "r")
    
    for palavra in arquivo:
      palavra = palavra.strip()
      palavraArquivo.append(palavra)



  elif tmp_genero == 2: # Bebidas
    arquivo = open("bebidas.txt", "r")
    
    for palavra in arquivo:
      palavra = palavra.strip()
      palavraArquivo.append(palavra)



  elif tmp_genero == 3: # Nomes
    arquivo = open("nomes.txt", "r")
    
    for palavra in arquivo:
      palavra = palavra.strip()
      palavraArquivo.append(palavra)



  elif tmp_genero == 4: # Comidas
    arquivo = open("comidas.txt", "r")

    for palavra in arquivo:
      palavra = palavra.strip()
      palavraArquivo.append(palavra)



  elif tmp_genero == 5: # Diversos
    arquivo = open("palavras.txt", "r")   

    for palavra in arquivo:
      palavra = palavra.strip()
      palavraArquivo.append(palavra)

  elif tmp_genero == 6:
    print("")
    print("Valor não corresponde a nenhum tipo de genero, assim sendo, atribuiu-se o genero diversos")

    arquivo = open("palavras.txt", "r")   

    for palavra in arquivo:
      palavra = palavra.strip() # Strip ira remover os espaços em ates e depois da palavra
      palavraArquivo.append(palavra)
    print('')

  # Linha é responsavel do sorteio da palavra
  numero = random.randrange(0,len(palavraArquivo))

  palavra_secreta = palavraArquivo[numero].upper()

  arquivo.close()
  return palavra_secreta

def tela_inicial():
  imprime_mensagem_abertura()
  menu_jogo()

def menu_jogo():

  print('''
  #########################################
  #             MENU DO JOGO              #
  #########################################
  # 1 - Jogar                             #
  # 2 - Cadastrar uma nova palavra        #
  # 3 - Consultar as regras e informações #
  # 0 - Sair                              #
  #########################################
  ''')
  opcao_menu = input('  # Digite a opção desejada: ')
  menu_valido = [1,2,3,4]

  try:
    opcao_menu = int(opcao_menu)

  except:
    print('')
    tratar_menu()

    pass

  if opcao_menu in menu_valido:
      if opcao_menu == 1:
       jogar()
      elif opcao_menu == 2:
       cad_nova_palavra()
      elif opcao_menu == 3:
       regras_jogo()

  elif opcao_menu == 0:
    pass
  else:
    tratar_menu()

def regras_jogo():
  print('')
  print('########################')
  print('# REGRAS E INFORMAÇÕES #')
  print('''########################

  01 - As dicas são os generos selecionados
  02 - Não é aceito nenhum tipo de número, sera considerado erro
  03 - Não é permitido chutar a palavra completa, apenas uma letra por vez
  04 - Ç não é considerado caractere, substitua por C, do contrario sera considerado erro
  05 - Palavras que possuem espaços são consideradas juntas ex: Bom dia -> bomdia

  ''')
  menu_jogo()

def cad_nova_palavra():
  print('''
  ################################################
  # BEM VINDO A TELA DE CADASTRO DE NOVA PALAVRA #
  ################################################
  # Todas as palavras cadastradas ficarão no     # 
  # genero Diversos, não existe restrição,       #
  # cadastre o que quiser!                       #
  ################################################
  ''')

  nova_palavra = str(input('# Digite a palavra que deseja inserir: '))
  nova_palavra = nova_palavra + '\n'
  arquivo = open("palavras.txt", "a")
  arquivo.write(nova_palavra)

  arquivo.close()
  
  print('')
  print('Palavra cadastrada com sucesso!')
  print('')
  menu()

def tratar_menu():
  print('''A opção escolhida não existe, favor digitar novamente''')
  menu_jogo()

  
  


if(__name__ == '__main__'):
  tela_inicial()
