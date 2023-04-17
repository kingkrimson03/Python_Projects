#gerador de senhas aleatorias com tamanho limite determidado pelo usuario

import random
import string

#funcao que gera a senha
def gerador_senha(tamanho = 8):
    letra = string.ascii_letters
    numero = string.digits
    ponto = string.punctuation
    senha = letra + numero + ponto

    senha_usuario = ''

    for i in range(0, tamanho):
        digito = random.choice(senha)
        senha_usuario = digito + senha_usuario

    return senha_usuario

#escolha do usuario para o tamanho da senha
escolha_tamanho = input('DIGITE O TAMANHO DA SENHA: ')
#verificacao se oque o usuario digitou foi um numero
if escolha_tamanho.isdigit():
    escolha_tamanho = int(escolha_tamanho)
else:
    print('DIGITE UM NUMERO VALIDO')
    quit()

#chamada da funcao
resposta = gerador_senha(tamanho=escolha_tamanho)
print(f'SENHA GERADA:\n{resposta}')



    




    

    

