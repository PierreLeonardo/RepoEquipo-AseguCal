# test_example.py 
 
def suma(a, b): 
    """Función que suma dos números.""" 
    return a + b 
 
def test_suma(): 
    """Prueba que verifica que la suma funciona correctamente.""" 
    assert suma(2, 3) == 5
