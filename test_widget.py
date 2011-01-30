import unittest
import dblayer

class TestWidget(unittest.TestCase):
    def test_creation(self):
        widget = dblayer.Widget(42)
        self.assertEqual(42, widget.length)

if __name__ == "__main__":
    unittest.main()
