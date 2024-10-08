# Questão 2

def is_fibonacci(num):
    fib_sequencia = [0, 1]
    while fib_sequencia[-1] < num:
        fib_sequencia.append(fib_sequencia[-1] + fib_sequencia[-2])
    return num in fib_sequencia

# Exemplo com um número previamente definido
num = int(input("Informe um número: "))
pertence_a_fibonacci = is_fibonacci(num)

if pertence_a_fibonacci == True:
    print("O número informado pertence a sequência fibonacci")
else:
    print("O número informado não pertence a sequência fibonacci")
