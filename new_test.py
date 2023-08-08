import unittest

class TestAbs(unittest.TestCase):
    def test_loginPage1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_loginPage2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()