import src.decorators
from src.decorators import my_function
import unittest

def test_log(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


class Testlog(unittest.TestCase):

    def test_log(self):
        self.assertEqual(src.decorators.my_function(1, 2), 3)


if __name__ == '__main__':
    unittest.main