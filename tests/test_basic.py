import unittest

class TestBasic(unittest.TestCase):
    def test_true(self):
        """A simple test that always passes"""
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()