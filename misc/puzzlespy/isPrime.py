import sys
print(sys.executable)
print(sys.version)
sys.

def isPrime(number):
    for divisor in range(2, number):  # Divisors range from 2 to number - 1 (excluding 1 and itself)
        if(number % divisor == 0):  # If the number is DIVISIBLE by the divisor
            print("{} IS NOT a prime number!".format(number))
            break  # break the loop right away because we don't need to go through all divisors
    else:  # Enter else statement of for loop if 'break is not executed', if the number is not divisible by any divisors
        print("{} IS a prime number".format(number))


def main():
    isPrime(1)
    isPrime(2)
    isPrime(4)
    isPrime(7)
    isPrime(25)
    isPrime(108)


if __name__ == "__main__":
    main()
