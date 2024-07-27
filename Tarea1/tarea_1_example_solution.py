def operation_selector(num1, num2, op):
    # Definir los códigos de error
    Error_Numero_Invalido = -50
    Error_No_String = -60
    Error_Operador_Invalido = -70
    Exito = 0

    # Verificar si num1 y num2 son enteros y ademas que no sean booleanos, ya que confunde booleanos con 1 y 0
    if (not isinstance(num1, int) or isinstance(num1, bool)) or (not isinstance(num2, int) or isinstance(num2, bool)):
        return (Error_Numero_Invalido, None)

    # Verificar si op es un string
    if not isinstance(op, str):
        return (Error_No_String, None)

    # Verificar si op es uno de los operadores
    if op not in ['+', '-', '*', '&']:
        return (Error_Operador_Invalido, None)

    # Realizar la operación según el valor de op
    if op == '+':
        resultado = num1 + num2
    elif op == '-':
        resultado = num1 - num2
    elif op == '*':
        resultado = num1 * num2
    elif op == '&':
        resultado = num1 & num2

    # Devolver el resultado con código de éxito
    return (Exito, resultado)

def calculo_promedio(lista_valores):
    # Verificar si la lista tiene más de 10 elementos
    if len(lista_valores) > 10:
        return (-90, None)  # Código de error 1: Lista demasiado grande

    # Verificar si todos los valores en la lista son números
    for i in lista_valores:
        if (not isinstance(i, (int, float)) or isinstance(i, bool)):
            return (-80, None)  # Código de error 2: No todos los valores son números, tambien revisa caso de bool

    # Calcular el promedio si todas las validaciones son exitosas
    promedio = sum(lista_valores) / len(lista_valores)
    return (0, promedio)  # Código de éxito 0