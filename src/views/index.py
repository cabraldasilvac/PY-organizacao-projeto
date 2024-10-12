import sys
from pathlib import Path
from controller.pessoa import Pessoa, PessoaController
from models.pessoa import Pessoa

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

while True:
    escolha = int(input('digite 1 para salvar e 2 para listar'))
    if escolha == 1:
        nome = input('Nome: ')
        sobrenome = input('sobrenome: ')
        idade = input('idade: ')
        cpf = input('cpf: ')

        p1 = Pessoa(nome=nome, sobrenome=sobrenome, idade=idade, cpf=cpf)
        PessoaController.salvar_pessoa(p1)

    elif escolha == 2:
        for i in PessoaController.listar_pessoas():
            print(f'Nome: {i.nome}')

