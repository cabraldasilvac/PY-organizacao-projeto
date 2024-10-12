import sys
from pathlib import Path
from models.pessoa import Pessoa
from typing import List

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

class PessoaController:
    pessoa=[]

    @classmethod
    def salvar_pessoa(cls, pessoa: Pessoa):
        cls.pessoa.append(pessoa)

    @classmethod
    def listar_pessoas(cls) -> List[Pessoa]:
        return cls.pessoa