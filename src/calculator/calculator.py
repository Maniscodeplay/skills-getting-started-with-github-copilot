"""Main calculator class with arithmetic operations."""


class Calculator:
    """A simple calculator class that performs basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with a result value."""
        self.result = 0

    def add(self, a, b):
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        """Subtract two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The difference of a and b
        """
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        self.result = a * b
        return self.result

    def divide(self, a, b):
        """Divide two numbers.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            The quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result

    def power(self, base, exponent):
        """Calculate the power of a number.
        
        Args:
            base: The base number
            exponent: The exponent
            
        Returns:
            The result of base raised to exponent
        """
        self.result = base ** exponent
        return self.result

    def get_result(self):
        """Get the last calculated result.
        
        Returns:
            The last result value
        """
        return self.result
