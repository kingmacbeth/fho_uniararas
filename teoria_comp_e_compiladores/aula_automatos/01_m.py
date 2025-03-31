def m_one(estado, simbolo):
    if (estado, simbolo) == ("q0", "a"):
        return "q1"
    if (estado, simbolo) == ("q0", "b"):
        return "q1"
    if (estado, simbolo) == ("q1", "a"):
        return "q1"
    if (estado, simbolo) == ("q1", "b"):
        return "q1"


estado = "q0"
simbolos = ""

for simbolo in simbolos:
    estado = m_one(estado, simbolo)

estado_aceitacao = ["q0"]
print("Aceita: ", estado in estado_aceitacao)
