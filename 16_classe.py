"""
Classe é uma estrutura que representa conjuntamente dados e
algoritmos. Uma classe pode ser comparada a uma "assadeira",
com a qual se pode produzir diferentes tipos de "assados"
(objetos), variando os "ingredientes" (dados) e o "modo de
fazer" (algoritmos). Apesar dessas variações, todos os objetos
criados a partir de uma mesma classe terão sempre algumas
características comuns impostas por esta.
"""
class FormaGeometrica:
    """
    Por convenção, nomes de classes seguem o formato PascalCase
    (primeira letra de cada palavra em maiúsculo).
    Uma classe pode ter, dentro de si, tanto dados quanto funções
    (estas, representando os algoritmos). Uma função especial,
    chamada __init__, é chamada sempre que se tenta criar um novo
    objeto a partir de uma classe. Essa função especial é chamada
    de CONSTRUTOR.
    No contexto de classes e programação orientada a objetos:
    ~> funções passam a ser chamadas MÉTODOS; seu primeiro parâmetro
       é sempre self, o qual representa o próprio objeto
    ~> variáveis passam a ser chamadas ATRIBUTOS
    """

    def __init__(self, base, altura, tipo):
        """ Método construtor """

        # Validações dos dados iniciais
        if type(base) not in [int, float]:
            raise Exception("ERRO: o parâmetro 'base' deve ser numérico.")
        if type(altura) not in [int, float]:
            raise Exception("ERRO: o parâmetro 'altura' deve ser numérico.")
        if tipo not in ["R", "T", "E"]:
            raise Exception("ERRO: o parâmetro 'tipo' deve ter um dos seguintes valores: 'R', 'T' ou 'E'.")

        self.base = base
        self.altura = altura
        self.tipo = tipo