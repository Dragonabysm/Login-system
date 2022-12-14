from rich import print, status, console
from server import addCadastro, Cadastro, verificarCadastro
from hashlib import blake2b
from regex import regex
from time import sleep

# salt for blake2b algorithm
SALT_VAR = b'dragonuser'

print('[b #0d00ff]Login/Cadastro App[/] \n  [b cyan][1][/] Fazer Cadastro\n  [b cyan][2][/] Fazer Login \n')

def validarEmail(email):
    regex_email = regex.Regex('.*@.*\..*')
    if regex_email.match(email, pos=0):
        return True
    return False

console = console.Console()

while True:
    print('[b red on black]>>>[/]', end='')

    try:
        opt = int(input())
    except ValueError:
        print(f'[b red]Digite um valor válido. Error: [i]Não é um número válido[/][/]')
    else:
        if opt == 1:
            email = input('Email: ')
            if not validarEmail(email):
                raise ValueError('Esse email é inválido, tente de novo.')
            senha = input('Password: ')
            senha_hash = blake2b(senha.encode(), usedforsecurity=True, digest_size=48, salt=SALT_VAR).hexdigest()
            cadastro = Cadastro(senha=senha_hash, email=email)
            addCadastro(cadastro)
            espera = status.Status('[b blink]Cadastrando[/]', console=console, refresh_per_second=20)
            espera.start()
            sleep(3)
            espera.stop()
            break

        elif opt == 2:
            email = input('Email: ')
            if not validarEmail(email):
                raise ValueError('Esse email é inválido, tente de novo.')
            senha = input('Password: ')
            senha_hash = blake2b(senha.encode(), usedforsecurity=True, digest_size=48, salt=SALT_VAR).hexdigest()
            
            login = verificarCadastro(email=email, senha_hash=senha_hash)
            espera = status.Status('[b blink]Logando[/]', console=console, refresh_per_second=20)
            espera.start()
            sleep(3)
            espera.stop()
            if login:
                print('Login bem sucedido')
            else:
                raise ValueError('Senha incorreta')
            break

# dinishigor@gmail.com
# sla1