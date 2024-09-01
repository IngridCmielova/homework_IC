class BankNumber:
    def __init__(self, real_part, float_part):
        self.real_part = real_part  # Celá část čísla
        self.float_part = float_part  # Desetinná část čísla

    def __eq__(self, other):
        # Porovnání
        return self.real_part == other.real_part and self.float_part == other.float_part

    def __add__(self, other):
        # Sčítání
        real_sum = self.real_part + other.real_part
        float_sum = self.float_part + other.float_part

        if float_sum >= 100:
            real_sum += 1
            float_sum -= 100

        return BankNumber(real_sum, float_sum)

    def __str__(self):
        return f"{self.real_part}.{self.float_part:02d}"


def test_bank_number():
    number1 = BankNumber(10, 50)
    number2 = BankNumber(5, 75)

    # Test rovnosti
    if number1 == BankNumber(10, 50):
        print("Test rovnosti prošel.")
    else:
        print("Test rovnosti selhal.")

    # Test sčítání
    result_add = number1 + number2
    if result_add == BankNumber(16, 25):
        print("Test sčítání prošel.")
    else:
        print("Test sčítání selhal.")

# Spuštění testů
test_bank_number()