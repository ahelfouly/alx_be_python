class Calculator:
    def __init__(self, calculation_type="Arithmetic Operations")
        self.calculation_type = calculation_type

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b