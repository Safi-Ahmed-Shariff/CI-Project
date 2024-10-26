# test_main.py
import unittest
from main import add_numbers

class TestMain(unittest.TestCase):
    def test_add_numbers(self):
        """Test the add_numbers function with sample inputs."""
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
