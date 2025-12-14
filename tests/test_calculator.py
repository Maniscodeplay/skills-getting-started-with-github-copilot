"""Unit tests for the Calculator class."""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test cases for Calculator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition operation."""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(-5, 3) == -2
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        """Test subtraction operation."""
        assert self.calc.subtract(10, 3) == 7
        assert self.calc.subtract(5, 5) == 0
        assert self.calc.subtract(-5, 3) == -8

    def test_multiply(self):
        """Test multiplication operation."""
        assert self.calc.multiply(4, 5) == 20
        assert self.calc.multiply(-4, 5) == -20
        assert self.calc.multiply(0, 100) == 0

    def test_divide(self):
        """Test division operation."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(7, 2) == 3.5
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)

    def test_power(self):
        """Test power operation."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(2, -2) == 0.25

    def test_get_result(self):
        """Test getting the last result."""
        self.calc.add(5, 3)
        assert self.calc.get_result() == 8
