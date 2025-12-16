def list_factors(n):
    if abs(n) == 1:
        return [1]

    listed_factors = []
    i = 2

    while (i ** 2) <= abs(n):
        if (n % i) == 0:
            listed_factors.append(i)
            listed_factors.append(abs(int(n / i)))
        i += 1

    return [1] + listed_factors + [abs(n)]


def evaluate_polynomial(coefficients, x):

    value = 0
    for i in range(len(coefficients)):
        value += coefficients[i] * (x ** i)

    return value


def find_integer_roots(coefficients):

    constant_coefficient = coefficients[0]

    possible_roots = list_factors(constant_coefficient)
    integer_roots = []
    for possible_root in possible_roots:
        if evaluate_polynomial(coefficients, possible_root) == 0:
            integer_roots.append(possible_root)
        if evaluate_polynomial(coefficients, -1 * possible_root) == 0:
            integer_roots.append(-1 * possible_root)

    return integer_roots


def find_rational_roots(coefficients):

    constant_coefficient = coefficients[0]
    leading_coefficient = coefficients[len(coefficients) - 1]

    possible_numerators = list_factors(constant_coefficient)
    possible_denominators = list_factors(leading_coefficient)
    possible_roots = []

    for i in range(len(possible_numerators)):
        for j in range(len(possible_denominators)):
            possible_roots.append(possible_numerators[i] / possible_denominators[j])

    possible_roots = list(set(possible_roots))
    rational_roots = []
    for possible_root in possible_roots:
        if abs(evaluate_polynomial(coefficients, possible_root)) < (10 ** -8):
            rational_roots.append(possible_root)
        if abs(evaluate_polynomial(coefficients, -1 * possible_root)) < (10 ** -8):
            rational_roots.append(-1 * possible_root)

    return rational_roots
