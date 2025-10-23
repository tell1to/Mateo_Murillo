from funciones import sumar

def test_suma_basica():
    assert sumar(2, 2) == 5

def test_suma_negativos():
    assert sumar(-1, -2) == -2



