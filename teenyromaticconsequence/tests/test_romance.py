"""Romance Tests."""
from unittest import TestCase
from teenyromaticconsequence.romance import romance


class RomanceTest(TestCase):
    """Romatic Tests."""

    def test_romance(self):
        """Unittest of romance."""
        self.assertEqual(romance(2, 3), 6)
