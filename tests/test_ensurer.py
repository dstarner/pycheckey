import unittest

from pycheckey import KeyEnsurer


class TestKeyEnsurer(unittest.TestCase):

    def test_key_exists_basic(self):
        data = {
            'hello': 'world'
        }
        self.assertTrue(
            KeyEnsurer(data=data, required_keys=['hello']).validate()
        )
