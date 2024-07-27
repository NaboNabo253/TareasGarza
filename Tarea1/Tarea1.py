def operation_selector(num1, num2, op):
    # Definir los códigos de error
    Error_Numero_Invalido = 1
    Error_No_String = 2
    Error_Operador_Invalido = 3
    Exito = 0

    # Verificar si num1 y num2 son enteros
    if not isinstance(num1, int) or not isinstance(num2, int):
        return (Error_Numero_Invalido, None)

    # Verificar si op es un string
    if not isinstance(op, str):
        return (Error_No_String, None)

    # Verificar si op es uno de los operadores válidos
    if op not in ('+', '-', '*', '&'):
        return (Error_Operador_Invalido, None)

    # Realizar la operación según el valor de op
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '&':
        result = num1 & num2

    # Devolver el resultado con código de éxito
    return (SUCCESS, result)
