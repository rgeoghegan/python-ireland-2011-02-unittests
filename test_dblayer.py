import unittest
import dblayer

class TestDbLayer(unittest.TestCase):
    def test_average_length(self):
        db = dblayer.DBLayer("test.sqlite")

        self.assertEqual(
            6.0, db.average_length()
        )

    def test_probability(self):
        db = dblayer.DBLayer("test.sqlite")
        self.assertEqual(
            0.090909, db.probability(11.0)
        )

    def test_insert_widget(self):
        db = dblayer.DBLayer("temp_test.sqlite")
        w = dblayer.Widget(20)
        db.insert_widget(w)
        self.assertEqual(
            7.16666, db.average_length()
        )

if __name__ == "__main__":
    unittest.main()
