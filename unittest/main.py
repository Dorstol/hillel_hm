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

    def test_without_params(self):
        with self.assertRaises(TypeError):
            formatted_name()

    def test_empty_params(self):
        self.assertEqual(formatted_name("", ""), " ")

    def test_different_register_params(self):
        self.assertEqual(formatted_name("OlEh", "sOfRoNoV"), "Oleh Sofronov")

    def test_wrong_params(self):
        with self.assertRaises(TypeError):
            formatted_name(31, 10)

    def test_with_1_param(self):
        with self.assertRaises(TypeError):
            formatted_name("Oleh")

    def test_with_2_params(self):
        self.assertEqual(formatted_name("Oleh", "Sofronov"), "Oleh Sofronov")

    def test_with_3_params(self):
        self.assertEqual(formatted_name("Oleh", "Sofronov", "Yurievich"), "Oleh Yurievich Sofronov")


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fibonacci = Fibonacci()
        self.fibonacci_test_data = [
            [1, 1], [2, 1], [3, 2], [4, 3],
            [5, 5], [6, 8], [7, 13], [8, 21],
            [9, 34], [10, 55], [11, 89], [12, 144]
        ]

    def test_fibonacci_test_data(self):
        for n, expected_number in self.fibonacci_test_data:
            actual_number = self.fibonacci(n)
            self.assertEqual(expected_number, actual_number)

    def test_first_fibonacci_number_is_1(self):
        x = self.fibonacci(1)
        self.assertEqual(1, x)

    def test_second_fibonacci_number_is_1(self):
        x = self.fibonacci(2)
        self.assertEqual(1, x)

    def test_5th_fibonacci_number_is_5(self):
        x = self.fibonacci(5)
        self.assertEqual(5, x)

    def test_fibonacci_empty_param(self):
        with self.assertRaises(TypeError):
            self.fibonacci()

    def test_fibonacci_wrong_param(self):
        with self.assertRaises(ValueError):
            self.fibonacci("test")

    def test_fibonacci_negative_param(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-322)

    def test_fibonacci_float_param(self):
        with self.assertRaises(ValueError):
            self.fibonacci(13.2)

    def test_fibonacci_with_2_params(self):
        with self.assertRaises(TypeError):
            self.fibonacci(1, 2)


if __name__ == "__main__":
    unittest.main()
