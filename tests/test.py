import pytest

from app.Calculator import Calculator

class Testcalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 4, 2) == 6

    def test_multiply(self):
        assert self.calc.multiply(self, 4, 2) == 8

    def test_subtraction(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')