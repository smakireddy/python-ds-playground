import unittest


def add(x, y):
    return x + y


class TestSkewness(unittest.TestCase):
    def test_sample(self):
        result = add(10, 5)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
