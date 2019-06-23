import unittest

class TestTravis(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertNotEqual(1, "1")

if __name__ == "__main__":
    unittest.main()
