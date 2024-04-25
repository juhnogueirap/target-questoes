num = int(input('Insira o valor que deseja conferir se pertence à sequência de Fibonacci: '))
fib = [0, 1]

for i in range(2, num):
    prox_fib = fib[i - 2] + fib[i - 1]
    fib.append(prox_fib)
    if prox_fib == num:
        print(fib)
        print('\nO número pertence à sequência de Fibonacci')
        exit()

print('\nO número não pertence à sequência de Fibonacci')