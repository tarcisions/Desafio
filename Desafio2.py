def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

num = int(input("Digite um número: "))
sequencia_fibonacci = [0, 1]
while sequencia_fibonacci[-1] < num:
    sequencia_fibonacci.append(sequencia_fibonacci[-1] + sequencia_fibonacci[-2])

if num in sequencia_fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci!")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci!")