def m_seven(estado, simbolo):
    if (estado, simbolo) == ("q0", "a"):
        return "q0"
    if (estado, simbolo) == ("q0", "b"):
        return "q0"


estado = "q0"
simbolos = ""

for simbolo in simbolos:
    estado = m_seven(estado, simbolo)

estado_aceitacao = ["q0"]
print("Aceita: ", estado in estado_aceitacao)
