def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator  # Čitatel
        self.denominator = denominator  # Jmenovatel
        self.simplify()

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# Testy
def test_fraction():
    f1 = Fraction(1, 2)  # 1/2
    f2 = Fraction(3, 4)  # 3/4

    # Test zjednodušení
    f3 = Fraction(2, 4)  # 2/4 by mělo být zjednodušeno na 1/2
    assert f3 == Fraction(1, 2), f"Chyba: 2/4 nebylo zjednodušeno na 1/2, ale na {f3}"

    # Test sčítání
    result_add = f1 + f2  # 1/2 + 3/4 = 5/4
    assert result_add == Fraction(5, 4), f"Chyba: Sčítání selhalo, dostali jsme {result_add}"

    # Test odečítání
    result_sub = f2 - f1  # 3/4 - 1/2 = 1/4
    assert result_sub == Fraction(1, 4), f"Chyba: Odečítání selhalo, dostali jsme {result_sub}"

    # Test násobení
    result_mul = f1 * f2  # 1/2 * 3/4 = 3/8
    assert result_mul == Fraction(3, 8), f"Chyba: Násobení selhalo, dostali jsme {result_mul}"

    # Test dělení
    result_div = f1 / f2  # (1/2) / (3/4) = 2/3
    assert result_div == Fraction(2, 3), f"Chyba: Dělení selhalo, dostali jsme {result_div}"

    print("Testy byly úspěšné")

# Spuštění testů
test_fraction()