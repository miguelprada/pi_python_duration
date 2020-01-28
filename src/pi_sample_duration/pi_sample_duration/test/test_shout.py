import unittest
from pi_sample_duration import shout

class PISampleDurationTest(unittest.TestCase):

    def test_shout_and_repeat(self):
        result = shout.shout_and_repeat('hello goodbye-')
        assert result == 'HELLO GOODBYE-HELLO GOODBYE-'


    def test_shout(self):
        assert shout._shout('have a nice day') == 'HAVE A NICE DAY'

if __name__ == '__main__':
    print("test_shout -- begin")
    unittest.main()
    print("test_shout -- end")
