# range not include the end number, so end with end + 1

def is_prime(number):
    if number in (1, 2):
        return True
    for idx in range(2, number):
        if number % idx == 0:
            return False
    return True

def print_primes(begin, end):
    for number in range(begin, end + 1):
        if is_prime(number):
            print(f"{number} is a prime")

begin = 1
end = 100
print_primes(begin, end)
