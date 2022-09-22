import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


class TestFormatName(unittest.TestCase):
    def test_format_name_equal(self):
        self.assertEqual(formatted_name("Oleh", "sofronov"), "Oleh Sofronov")
        self.assertEqual(formatted_name("oleh", "Sofronov"), "Oleh Sofronov")
        self.assertEqual(formatted_name("oleh", "sofronov"), "Oleh Sofronov")
        self.assertEqual(formatted_name("oleh", "sofronov", "Yurievich"), "Oleh Yurievich Sofronov")

    def test_format_name_raiseerror(self):
        self.assertRaises(TypeError, formatted_name('1', 2))
        self.assertRaises(TypeError, formatted_name(1, 2))
        self.assertRaises(TypeError, formatted_name('oleh'))
        self.assertRaises(TypeError, formatted_name())


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fibonacci_instance = Fibonacci()

    def test_fibonacci(self):
        self.assertEqual(self.fibonacci_instance(10), 55)
        self.assertEqual(self.fibonacci_instance(0), 0)
        self.assertEqual(self.fibonacci_instance(16), 987)
        self.assertEqual(self.fibonacci_instance(8), 21)

    def test_fibonacci_error(self):
        self.assertRaises(TypeError, self.fibonacci_instance())
        self.assertRaises(TypeError, self.fibonacci_instance(21, 32))
        self.assertRaises(TypeError, self.fibonacci_instance('Hello World!'))
        self.assertRaises(TypeError, self.fibonacci_instance(True))
