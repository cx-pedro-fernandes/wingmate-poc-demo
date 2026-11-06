import unittest
from lookup import find_customer


class CustomerTests(unittest.TestCase):
    def test_known_customer(self):
        self.assertEqual(find_customer("Alice"), [(1, "Alice")])

    def test_unknown_customer(self):
        self.assertEqual(find_customer("Nobody"), [])

    def test_query_treats_input_as_data(self):
        self.assertEqual(find_customer("' OR 1=1 --"), [])

    def test_union_injection_is_data(self):
        payload = "x' UNION SELECT id, name FROM customers --"
        self.assertEqual(find_customer(payload), [])

    def test_stacked_statement_injection_is_data(self):
        # A stacked statement must not execute (and must not raise).
        self.assertEqual(find_customer("x'; DROP TABLE customers; --"), [])

    def test_quote_in_name_is_handled(self):
        self.assertEqual(find_customer("O'Brien"), [])


if __name__ == "__main__":
    unittest.main()
