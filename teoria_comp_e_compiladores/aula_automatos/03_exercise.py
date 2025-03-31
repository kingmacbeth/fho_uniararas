def ex_three_a(estado, simbolo):
    if (estado, simbolo) == ("q0", "a"):
        return "q1"
    if (estado, simbolo) == ("q0", "b"):
        return "q2"
    if (estado, simbolo) == ("q1", "a"):
        return "q4"
    if (estado, simbolo) == ("q1", "b"):
        return "q0"
    if (estado, simbolo) == ("q2", "a"):
        return "q3"
    if (estado, simbolo) == ("q2", "b"):
        return "q4"
    if (estado, simbolo) == ("q3", "a"):
        return "q4"
    if (estado, simbolo) == ("q3", "b"):
        return "q4"
    if (estado, simbolo) == ("q4", "a"):
        return "q4"
    if (estado, simbolo) == ("q4", "b"):
        return "q4"


def ex_three_b(estado, simbolo):
    if (estado, simbolo) == ("q0", "a"):
        return "q1"
    if (estado, simbolo) == ("q1", "b"):
        return "q2"
    if (estado, simbolo) == ("q2", "a"):
        return "q3"
    if (estado, simbolo) == ("q2", "b"):
        return "q4"
    if (estado, simbolo) == ("q3", "b"):
        return "q2"
    if (estado, simbolo) == ("q4", "a"):
        return "q5"


estado_a = "q0"
estado_b = "q0"

simbolos = ""

for simbolo in simbolos:
    estado_a = ex_three_b(estado, simbolo)
    estado_b = ex_three_a(estado, simbolo)

estado_aceitacao = ["q3", "q5"]

if estado_a in estado_aceitacao:
    print("Aceita: ", True)
elif estado_b in estado_aceitacao:
    print("Aceita: ", True)
else:
    print("Aceita: ", False)
