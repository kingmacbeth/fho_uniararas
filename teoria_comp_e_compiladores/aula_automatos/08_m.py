def m_eight(estado, simbolo):
    if (estado, simbolo) == ("q0", "a"):
        return "q1"
    if (estado, simbolo) == ("q0", "b"):
        return "q2"
    if (estado, simbolo) == ("q1", "a"):
        return "q2"
    if (estado, simbolo) == ("q1", "b"):
        return "q0"
    if (estado, simbolo) == ("q2", "a"):
        return "q2"
    if (estado, simbolo) == ("q2", "b"):
        return "q2"


estado = "q0"
simbolos = ""

for simbolo in simbolos:
    estado = m_eight(estado, simbolo)

estado_aceitacao = ["q3"]
print("Aceita: ", estado in estado_aceitacao)
