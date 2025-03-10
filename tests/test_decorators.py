import src.decorators
from src.decorators import my_function
import unittest


def test_log(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


class Testlog(unittest.TestCase):

    def test_my_function(self):
        self.assertEqual(src.decorators.my_function(1, 2), 3)
        self.assertEqual(src.decorators.my_function(-1, 2), 1)
        self.assertEqual(src.decorators.my_function(-1, 1), 0)
        self.assertEqual(src.decorators.my_function(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
