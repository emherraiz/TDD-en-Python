def factorial(numero):
    if numero < 0:
        raise ValueError("Factorial tiene que ser mayor que cero")

    elif numero == 0:
        return 1

    else:
        fact = 1
        for i in range(1,numero+1):
            fact = fact * i
        return fact
