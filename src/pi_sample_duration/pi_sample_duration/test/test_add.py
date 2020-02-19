

import unittest
from pi_sample_duration import add


class PISampleDurationTest(unittest.TestCase):

    def test_my_add(self):
        assert add.my_add([9, 0, 2], [0, 1]) == [9, 0, 2, 0, 1]
        assert add.my_add('beverly ', 'hills') == 'beverly hills'


if __name__ == '__main__':
    print("test_add -- begin")
    unittest.main()
    print("test_add -- end")
