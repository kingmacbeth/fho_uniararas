from lex import lex
import sys

tokens = ("CONSTANTE_INTEIRA",
          "OPERADOR_ARITMETICO",
          "OPERADOR_ATRIBUICAO",
          "MUDA_LINHA",
          "TIPO_DADOS",
          "IDENTIFICADOR",
          "CONSTANTE_FLOAT",
          "CONSTANTE_INTEIRA",
          "CONSTANTE_CHAR",
          "ABRE_PARENTESES",
          "ABRE_CHAVES",
          "FECHA_PARENTESES",
          "FECHA_CHAVES",
          "FIM_COMANDO",
          "SEPARADOR")

t_OPERADOR_ATRIBUICAO = "\="
t_OPERADOR_ARITMETICO = "\+|\-|\*|\/|\%"
t_CONSTANTE_FLOAT = "-?\d+.\d+"
t_CONSTANTE_INTEIRA = "\d\d*"
t_TIPO_DADOS = "int|char|float"
t_IDENTIFICADOR = "[a-zA-Z]\w*"
t_CONSTANTE_CHAR = "'[^']'"
t_ABRE_PARENTESES = "\("
t_ABRE_CHAVES = "\{"
t_FECHA_PARENTESES = "\)"
t_FECHA_CHAVES = "\}"
t_FIM_COMANDO = "\;"
t_SEPARADOR = ","


def t_MUDA_LINHA(t):
    r"\n"
    t.lexer.lineno += 1


t_ignore = " "


def t_error(t):
    print(t, "nao foi reconhecido!")
    sys.exit(1)


arquivo = open("main.cpp")
conteudo = arquivo.read()
print(conteudo)

l = lex()
l.input(conteudo)

while True:
    t = l.token()
    if not t:
        break
    print(t)
