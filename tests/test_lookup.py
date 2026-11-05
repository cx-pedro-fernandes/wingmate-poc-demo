import unittest
from lookup import find_customer


class CustomerTests(unittest.TestCase):
    def test_known_customer(self):
        self.assertEqual(find_customer("Alice"), [(1, "Alice")])

    def test_unknown_customer(self):
        self.assertEqual(find_customer("Nobody"), [])

    def test_query_treats_input_as_data(self):
        self.assertEqual(find_customer("' OR 1=1 --"), [])


if __name__ == "__main__":
    unittest.main()
