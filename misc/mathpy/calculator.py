print ("Calcultor initializing...Hello World, I am a CalculatorBin")


def factor_of(x):
    try:
        if (x.is_integer()):
            for factor in range(1, x + 1):
                if(x % factor is 0):
                    print(factor)
    except TypeError:
        print("Not an integer value")


def add(x, y):
    result = x + y
    return result


def mult(x, y):
    result = x * y
    return round(result, 2)


if __name__ == "__main__":
    factor_of(10.0)
