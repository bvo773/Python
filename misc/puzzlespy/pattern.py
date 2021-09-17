'''
n = 3
*
* *
* * *
'''


def pattern_1(n):
    i = 0
    while (i < n):
        k = 0
        j = i + 1
        while (k < j):
            print('*', end=" ")
            k += 1
        print()
        i += 1


'''
n = 3, i = print ' ', j = print '*', k = condition variable
    *
  * *
* * *
'''


def pattern_2(n):
    k = n - 1
    for row in range(n):
        i = 0
        while (i < k):
            print(' ', end=' ')
            i += 1
        k = k - 1
        j = i
        while (j < n):
            print('*', end=' ')
            j += 1
        print()


def main():
    n = 3
    pattern_1(n)
    print()
    pattern_2(n)


if __name__ == '__main__':
    main()
