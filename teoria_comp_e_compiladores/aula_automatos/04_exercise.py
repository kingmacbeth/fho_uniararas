def ex_four(estado, simbolo):
    if (estado, simbolo) == ("q0", "a"):
        return "q1"
    if (estado, simbolo) == ("q0", "b"):
        return "q1"
    if (estado, simbolo) == ("q1", "a"):
        return "q2"
    if (estado, simbolo) == ("q1", "b"):
        return "q4"
    if (estado, simbolo) == ("q2", "a"):
        return "q2"
    if (estado, simbolo) == ("q2", "b"):
        return "q3"
    if (estado, simbolo) == ("q3", "a"):
        return "q4"
    if (estado, simbolo) == ("q3", "b"):
        return "q3"
    if (estado, simbolo) == ("q4", "a"):
        return "q4"
    if (estado, simbolo) == ("q4", "b"):
        return "q4"


estado = "q0"
simbolos = ""

for simbolo in simbolos:
    estado = ex_four(estado, simbolo)

estado_aceitacao = ["q3"]
print("Aceita: ", estado in estado_aceitacao)
