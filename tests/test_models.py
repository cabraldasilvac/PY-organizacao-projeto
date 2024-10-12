import sys
sys.path.append('.')
from src.models import pessoa

def test_concatenacao_nome_sobrenome():
    p1 = pessoa.Pessoa('Wanderley','Cabral', 58, '123.456.789.11')
    assert p1.nome_completo() == 'Wanderley Cabral'