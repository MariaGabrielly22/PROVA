# Como funciona o try/except
# O try tenta fazer algo.
# Se der erro, o except pega o erro e mostra uma mensagem.
# Assim, o programa não para.

#Estrutura:
#
# try:
#     # Tenta executar este código
# except:
#     # Se der erro, executa este código em vez de parar
#
# Isso é útil para tratar problemas como:
# - Arquivos que não existem
# - Entradas do usuário inválidas (ex: texto onde se espera número)
# - Erros de conexão, permissão, etc.
#
#  try:
#    Contém o código que será testado. Se não houver erro,
#    o programa segue normalmente.
#
#  except:
#    Executado somente se ocorrer erro dentro do try.
#    Pode capturar erros específicos (ex.: ZeroDivisionError)
#    ou de forma genérica (qualquer erro).
#
#    ZeroDivisionError: Quando o divisor é zero.
#    ValueError: Quando o usuário digita algo que não é um número.
#    Bloco else e finally:
#    else: Executado se nenhuma exceção ocorrer.
#    finally: Executado sempre, independentemente de ocorrer ou não uma exceção.
#
#    else:
#    Executado apenas se o bloco try não gerar erro.
#    É útil quando você quer rodar algo somente se deu tudo certo.
#
#  finally:
#    Executado sempre, independentemente de ter erro ou não.
#    Muito usado para fechar arquivos, desconectar do banco
#    ou liberar recursos importantes.

def ler_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, "r")  
        conteudo = arquivo.read()          
        print("Conteúdo do arquivo:\n", conteudo)
    except FileNotFoundError:              
        print("Erro: Arquivo não encontrado!")
    except Exception as erro:              
        print("Ocorreu um erro:", erro)
    finally:
        try:
            arquivo.close()                
        except:
            pass                          

ler_arquivo("dados.txt")
