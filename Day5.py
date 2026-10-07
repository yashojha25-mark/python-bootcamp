# Prime Numbers from 2 to 50

for num in range(2, 51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        
        
# Fibonacci Sequence

a = 0
b = 1
count = 0

while count < 10:
    print(a)
    a, b = b, a + b
    count += 1