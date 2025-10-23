from funciones import sumar

def test_suma_con_input_simulado():
    a = 10
    b = 20
    resultado = sumar(a, b)
    assert resultado == 30